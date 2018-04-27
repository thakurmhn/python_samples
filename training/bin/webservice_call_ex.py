#!/bin/python3.6
import boto3
my_sqs=boto3.resource('sqs',region_name='us-west-2',aws_access_key_id='AKIAI2RGGNUGOSBAWBAQ',aws_secret_access_key='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')

q=my_sqs.create_queue(QueueName='test_queue',Attributes={'DelaySeconds':'5'})
print(q.url)
print(q.attributes.get('DelaySeconds'))
for q1 in my_sqs.queues.all():
  print(q1.url)
