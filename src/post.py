import boto3
import sqs_extended_client

from dotenv import load_dotenv
import os

load_dotenv()

sqs_name = os.environ.get("QueueName")
bucket_name = os.environ.get("BucketName")

sqs = boto3.resource('sqs')
queue = sqs.get_queue_by_name(QueueName = sqs_name)

sqs_extended_client.large_payload_support = bucket_name

'''
sqs_extended_client = boto3.client("sqs", region_name="us-east-1")
sqs_extended_client.large_payload_support = "S3_BUCKET_NAME" 
sqs_extended_client.use_legacy_attribute = False
'''

# if (__name__ == "__main__") :
