import boto3
import sqs_extended_client

sqs = boto3.resource('sqs')
queue = sqs.get_queue_by_name(QueueName='test')


'''
sqs_extended_client = boto3.client("sqs", region_name="us-east-1")
sqs_extended_client.large_payload_support = "S3_BUCKET_NAME" 
sqs_extended_client.use_legacy_attribute = False
'''

if (__name__ == "__main__") :
    
    
