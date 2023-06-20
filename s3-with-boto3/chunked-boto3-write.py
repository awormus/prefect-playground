from prefect import flow, task, logging
import boto3

@task
def create_list_of_numbers(listsize=100000):
    """This function creates a list of numbers"""
    l = logging.get_logger()
    l.info("Creating list of numbers")

    return [x for x in range(1, listsize)]

def divide_chunks(list, chunks):
    # looping till length l
    for i in range(0, len(list), chunks):
        yield list[i:i + chunks]

@task
def write_chunked_to_s3(numbers, batchsize=1000):
    """Takes a list of numbers and chunks them into s3"""

    l = logging.get_logger()
    l.info("Writing chunked to S3")

    s3 = boto3.client('s3')
    bucket = "emilytest"
    s3_path = "chunked.txt"

    chunks = divide_chunks(numbers, batchsize)

    for chunk in chunks:
        chunk_str = "\n".join(map(str, chunk))
        l.info(chunk_str)

@flow(name="Chunked Boto3 Write")
def run_flow():
    numbers = create_list_of_numbers()
    chunked = write_chunked_to_s3(numbers)


if __name__ == "__main__":
    run_flow()