from send_email import run_flow
from prefect.deployments import Deployment

deploy = Deployment.build_from_flow(
    flow=run_flow,
    name="Send Steve a Report",
    tags=["Steve", "Reports"],
    parameters=dict(sender="noreply@wormus.com", 
                recipient="aaron@wormus.com", 
                attachments=[], 
                subject="Steve's Report 🏌️")
)

if __name__ == "__main__":
    deploy.apply()
