import json
import boto3

def lambda_handler(event, context):
    s3 = boto3.resource('s3')
    copy_source = {
      'Bucket': 'akash-peassignement-1',                 #Source bucket name
      'Key': 's3.json'                                   #Source file to be  copied
        }
    bucket = s3.Bucket('austin-pe-ques2')                #Destination bucket name
    bucket.copy(copy_source, 's3copy.json')              #Name of the file after being copied
  
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }




