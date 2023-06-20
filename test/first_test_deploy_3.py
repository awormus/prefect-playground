from prefect.deployments import Deployment
from prefect.server.schemas.schedules import CronSchedule

from first_test import call_api

if __name__ == "__main__":
    deployment = Deployment.build_from_flow(
        flow=call_api,
        name="Billing Workflow", 
        parameters={'url': "https://dummyjson.com/products"},
        # work_queue_name="default",
        description="The description seems like a very simple thing bar",
        schedule=(CronSchedule(cron="0 0 * * *", timezone="America/Chicago"))
    )
    deployment.apply()