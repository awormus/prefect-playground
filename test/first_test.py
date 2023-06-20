import requests
from prefect import flow, task, logging
from prefect.blocks.system import Secret

secret_block = Secret.load("mysql-connection-string")

@task
def print_secret(secret):
    x = logging.get_logger()
    x.warning(secret)
    return(secret)

@flow(name="SQL to Email Reports")
def call_api(url:str):
    s = secret_block.get()
    y = print_secret(s)

if __name__ == "__main__":
    api_result = call_api("http://time.jsontest.com/")
    # print(api_result)
