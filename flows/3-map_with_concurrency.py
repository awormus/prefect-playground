from prefect import flow, task
import time
import random


@task
def print_nums(nums):
    for n in nums:
        print(n)

@task(tags=['concurrency_5'])
def square_num(num):
    random_number = random.randint(2, 20)
    print(f"  ... sleeping {random_number}")
    time.sleep(random_number)
    print(f"  ... slept {random_number}")
    return num**2

@task
def foo_bar(squared_nums):
    return squared_nums

@task
def bar_foo(squared_nums):
    return squared_nums

@flow
def map_flow(nums):
    print_nums(nums)
    squared_nums = square_num.map(nums) 
    bar = foo_bar(squared_nums)
    foo = bar_foo(bar)

    print(foo)

map_flow([1,2,3,4,5,6,7,8,13])