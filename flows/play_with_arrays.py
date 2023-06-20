from prefect import task, flow

@task
def run_single_task(task_name: str):
    print(task_name)

    return task_name



@flow(name="Run Tasks")
def run_tasks():
    task1 = run_single_task(task_name="task1")
    task2 = run_single_task(task_name="task2", wait_for=[task1])
    task3 = run_single_task(task_name="task3", wait_for=[task2])

if __name__ == "__main__":
    run_tasks()