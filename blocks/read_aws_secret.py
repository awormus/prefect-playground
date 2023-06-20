from prefect import task, flow, get_run_logger
from prefect_aws.secrets_manager import read_secret
from prefect_aws import AwsCredentials

# aws_secret_block = AwsSecret.load("aaron-secret")

@task
def print_secret(secret):
    logger = get_run_logger()
    logger.info(f"Secret: {secret}")

@flow
def my_flow():
    aws_credentials = AwsCredentials(
        aws_access_key_id=None,
        aws_secret_access_key=None
    )
    secret = read_secret(secret_name="aaron-secret", aws_credentials=aws_credentials)
    print_secret(secret)

if __name__ == "__main__":
    my_flow()