from prefect.deployments import Deployment
from first_test import call_api

if __name__ == "__main__":

    deployment = Deployment.build_from_flow(
        flow=call_api,
        name="my-first-deployment", 
        work_queue_name="default",
    )
    deployment.apply()