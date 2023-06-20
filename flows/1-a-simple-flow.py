from prefect import flow, task, get_run_logger

@task(name="Say Hello")
def say_hello():
    return "hello"

@task(name="Say World")
def say_world():
    return "world"

@task(name="Say Hello, World")
def say_hello_world(hello, world):
    logger = get_run_logger()
    retval = f"{hello}, {world}"
    logger.info(retval)
    
    return retval



@flow(name="My First Flow")
def my_first_flow():
    logger = get_run_logger()
    logger.info("Starting my first flow")

    hello = say_hello()
    world = say_world()
    hello_world = say_hello_world(hello, world)

if __name__ == "__main__":
    my_first_flow()