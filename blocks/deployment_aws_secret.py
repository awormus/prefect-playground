from read_aws_secret import my_flow
from prefect.deployments import Deployment

deploy = Deployment.build_from_flow(
    flow=my_flow,
    name="A Flow with Secrets"
)

if __name__ == "__main__":
    deploy.apply()
