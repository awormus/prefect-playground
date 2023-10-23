from prefect import flow, task, logging
import boto3

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import random
import string
import datetime
    

# Generate some random but realistic text
@task
def generate_text():
    l = logging.get_logger()
    l.info("Generating text")
    # generate random data
    random.seed(datetime.datetime.now())
    random_text = ''.join(random.choice(string.ascii_letters) for x in range(1000))

    # break the random text into word sized chunks

    return random_text


@task
def send_email(sender, recipient, subject, attachments, message):
    l = logging.get_logger()
    l.info("Sending email")
    l.info(f"Data provided: {sender}, {recipient}, {subject}, {attachments}, {message}")

    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = recipient
    msg['Subject'] = subject

    msg.attach(MIMEText(message, 'plain'))

    if attachments is not None:
        for attachment in attachments:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment)
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', "attachment; filename= %s" % attachment)
            msg.attach(part)

    # create a boto3 ses client

    try:
        ses = boto3.client('ses')
        ses.send_raw_email(
            Source=sender,
            Destinations=[
                recipient
            ],
            RawMessage={'Data': msg.as_string()}
        )
    except Exception as e:
        l.info(e)
        return False

    return True


@flow(name="Send a simple email using SES")
def run_flow(sender: str, recipient: str, subject: str, attachments: list, message: str = None):
    l = logging.get_logger()
    l.info("preparing email :D")

    message = generate_text()
    email = send_email(sender=sender, recipient=recipient, subject=subject, attachments=attachments, message=message)

if __name__ == "__main__":
    run_flow(   sender="noreply@wormus.com", 
                recipient="aaron@wormus.com", 
                attachments=[], 
                subject="This is a an example subject")