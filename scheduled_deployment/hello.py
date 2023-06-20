from prefect import task, flow, get_run_logger

@task(name="Hello World")
def hello_world(name: str):
    logger = get_run_logger()
    logger.info(f"Hello World! {name}")

@flow(name="Hello World Flow")
def process_data(name: str):
    hello_world(name)


if __name__ == '__main__':
    process_data(name='John Doe')
