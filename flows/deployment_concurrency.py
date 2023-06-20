from a_flow_with_concurrency import flow_with_parameters
from prefect.deployments import Deployment
from prefect.server.schemas.schedules import IntervalSchedule

# https://docs.prefect.io/2.10.13/api-ref/server/schemas/schedules/

# create a deployment

deploy = Deployment.build_from_flow(
    flow=flow_with_parameters,
    name="A Flow with Concurrency",
    parameters=dict(something="Sending a couple of words to the flow")
)

if __name__ == "__main__":
    deploy.apply()
