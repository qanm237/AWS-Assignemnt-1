from __future__ import print_function 
import boto3
import json
import decimal
from boto3.dynamodb.conditions import Key, Attr

# Helper class to convert a DynamoDB item to JSON.
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

table = dynamodb.Table('gnames')

print("Game year")

response = table.query(
    KeyConditionExpression=Key('gid').eq(2013)      #quering condition
)

for i in response['Items']:
    print(i['gid'], ":", i['gname'],i['rate'])



