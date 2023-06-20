from prefect import flow, task, logging

@task
def do_first_thing(z: str):
    l = logging.get_logger()
    l.info("Doing first thing")
    l.info(z)

    return z


@flow(name="Secondary Test With Params")
def run_flow(one: str, two: str):
    three = do_first_thing(one)
    four = do_first_thing(two)

    return three, four

if __name__ == "__main__":
    run_flow("hello", "world")
