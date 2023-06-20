import s3fs
from prefect import flow, task, logging

@task
def read_from_s3_file(p: str):
    l = logging.get_logger()
    l.info("Reading from S3")
    l.info("Data provided: " + p)

    s3 = s3fs.S3FileSystem()
    s3_path = 's3://emilytest/' + p

    with s3.open(s3_path, 'r') as f:
        s = f.read()

    l.info(s)

    return s

@task
def write_to_s3_file(s: str, p: str):
    l = logging.get_logger()
    l.info("Writing to S3")
    l.info("Data recieved: " + s)

    s3 = s3fs.S3FileSystem()
    s3_path = 's3://emilytest/' + p

    with s3.open(s3_path, 'w') as f:
        f.write(s)

    return p

@flow(name="Simple Read and Write to S3")
def run_flow():
    one = read_from_s3_file("test20230606.txt")
    data = one + " and goodbye"
    two = write_to_s3_file(data, "test20230606.txt")

if __name__ == "__main__":
    run_flow()