from prefect import flow, task, logging
import boto3

@task
def download_file_from_s3(bucket: str, s3_path: str):
    l = logging.get_logger()
    l.info("Reading from S3")
    l.info(f"Data provided: s3://{bucket}/{s3_path}")

    s3 = boto3.client('s3')
    l.info("Path: " + s3_path)

    with open(s3_path, 'wb') as x:
        s3.download_fileobj(bucket, s3_path, x)

    return s3_path

@flow(name="Simple Boto3 Read")

def run_flow():
    one = download_file_from_s3("emilytest", "test20230606.txt")

if __name__ == "__main__":
    run_flow()