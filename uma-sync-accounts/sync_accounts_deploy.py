from prefect.deployments import Deployment
from sync_accounts import run_flow
from prefect.server.schemas.schedules import CronSchedule

if __name__ == "__main__":

    deployment = Deployment.build_from_flow(
        flow=run_flow,
        name="Sync Accounts", 
        work_queue_name="default",
        schedule=(CronSchedule(cron="5 * * * *", timezone="America/New_York")),
        description="Process to update Account. If this fails please contact Steve."

    )
    deployment.apply()