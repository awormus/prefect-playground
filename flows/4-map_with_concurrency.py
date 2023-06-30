from prefect import flow, task
import time
import random
from prefect.task_runners import ConcurrentTaskRunner


@task
def print_nums(nums):
    for n in nums:
        print(n)

@task(tags=['concurrency_5'])
def square_num(num):
    print(f"  ... sleeping {num}")
    time.sleep(num)
    print(f"  ... slept {num}")
    return num**2

@task
def foo_bar(squared_nums):
    return squared_nums

@task
def bar_foo(squared_nums):
    return squared_nums

@flow(task_runner=ConcurrentTaskRunner())
def map_flow():
    foo = "bar"

    one = square_num.submit(10)
    two = square_num.submit(9)
    three = square_num.submit(8)
    four = square_num.submit(7)
    five = square_num.submit(6)
    six = square_num.submit(5)
    seven = square_num.submit(4)
    eight = square_num.submit(3)
    nine = square_num.submit(2)

    nums = [one, two, three, four, five, six, seven, eight, nine]
 
    print_nums(nums)
    bar = foo_bar(nums)
    foo = bar_foo(bar)

    print(foo)

map_flow()