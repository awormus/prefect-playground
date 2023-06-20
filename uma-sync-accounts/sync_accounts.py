from prefect import flow, task, logging
from prefect.blocks.system import Secret
from prefect.filesystems import S3

@task
def pull_from_hcv(s: str):
    l = logging.get_logger()
    l.info("Getting Data from Database")
    l.info(s)

    # store in s3

    # s3_block = S3.load("account-store")
    retval = '2023/03/'
    # l.warning(s3_block.read_path(path=retval))

    return retval

@task
def upload_to_mysql(a):
    l = logging.get_logger()
    l.info("Setting up to upload to MySQLs")
    l.warning(a)

    pass

@flow(name="Sync Accounts to MySQL")
def run_flow():
    secret_block = Secret.load("sql-connection-string")
    s = secret_block.get()
    one = pull_from_hcv(s)
    three = upload_to_mysql(one)


if __name__ == "__main__":
    run_flow()