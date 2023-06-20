from hello import process_data
from prefect.deployments import Deployment
from prefect.server.schemas.schedules import IntervalSchedule

# https://docs.prefect.io/2.10.13/api-ref/server/schemas/schedules/

# create a deployment

deploy = Deployment.build_from_flow(
    flow=process_data,
    name="Scheduled Deployment John Stevens",
    schedule=IntervalSchedule(interval=39),
    tags=["John"],
    parameters=dict(name="John Stevens"),
)

if __name__ == "__main__":
    deploy.apply()
