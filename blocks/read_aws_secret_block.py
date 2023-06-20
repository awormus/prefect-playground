from prefect import task, flow, get_run_logger
from prefect_aws.secrets_manager import read_secret
from prefect_aws import AwsSecret

@task
def print_secret(secret):
    logger = get_run_logger()
    logger.info(f"Secret: {secret}")

@flow
def my_flow():
    secrets_manager = AwsSecret.load("aaron-secret")
    print(secrets_manager.read_secret())

if __name__ == "__main__":
    my_flow()