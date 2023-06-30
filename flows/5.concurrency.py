from prefect import flow, task
from prefect.task_runners import ConcurrentTaskRunner
import time

'''
https://docs.prefect.io/2.10.16/concepts/task-runners/#:~:text=For%20example%2C%20you%20can%20use%20ConcurrentTaskRunner%20to%20allow%20tasks%20to%20switch%20when%20they%20would%20block.

'''


@task(tags=['concurrency_5'])
def stop_at_floor(floor):
    print(f"elevator moving to floor {floor}")
    time.sleep(floor)
    print(f"elevator stops on floor {floor}")

@flow(task_runner=ConcurrentTaskRunner())
def elevator():
    # for floor in range(10, 0, -1):
    stop_at_floor.submit(10)
    stop_at_floor.submit(9)
    stop_at_floor.submit(8)
    stop_at_floor.submit(7)
    stop_at_floor.submit(6)
    stop_at_floor.submit(5)
    stop_at_floor.submit(4)
    stop_at_floor.submit(3)
    stop_at_floor.submit(2)
    stop_at_floor.submit(1)

elevator()