from prefect.blocks.system import JSON
from prefect import flow, task, get_run_logger

json_data = JSON.load("uno")

@flow(name="Read a Custom JSON Block")
def read_json():
    logger = get_run_logger()

    # Why would I have to call value here?
    # It looks very much like the documentation is incorrect.
    
    x = json_data.value
    logger.info(x)

if __name__ == "__main__": 
    read_json()