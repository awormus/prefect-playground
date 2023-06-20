from prefect import flow, task, get_run_logger
import time
import random


@task(name="Say Something")
def say_something(something):
    logger = get_run_logger()
    logger.info(something)
    ''' pick a random number between 2 and 20'''

    random_number = random.randint(2, 20)

    time.sleep(random_number)
    
    return something

@task(name="Split a string into words")
def split_string(something):
    return something.split()

@task(name="Say all")
def say_all(arr: list):
    retval = " ".join(arr)

    return retval

@task(name="notify")
def notify(data: str):
    logger = get_run_logger()
    logger.info(data)
    return

@flow(name=" Flow with Parameters")
def flow_with_parameters(something: str = "hello world"):

    x = []

    words = split_string(something)
    for word in words:
        x.append(say_something(word))

    all = say_all(x)

if __name__ == "__main__":
    flow_with_parameters("this is a test")