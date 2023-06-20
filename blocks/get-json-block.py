from prefect import flow, get_run_logger
from prefect.blocks.system import JSON

json_block = JSON.load("foo")

@flow
def my_flow():
    logger = get_run_logger()
    x = json_block.get()
    logger.info(x)

if __name__ == "__main__":
    my_flow()