from prefect import flow, get_run_logger
from prefect.blocks.system import Secret

secret_block = Secret.load("foo")

@flow
def my_flow():
    logger = get_run_logger()
    x = secret_block.get()
    logger.info(x)

if __name__ == "__main__":
    my_flow()