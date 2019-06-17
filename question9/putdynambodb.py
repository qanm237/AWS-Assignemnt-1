from __future__ import print_function 
import boto3
import json
import decimal
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if abs(o) % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

table = dynamodb.Table('gnames')  #connecting to the database already created
#adding items
gname= "Mini-Militia"
gid = 2013
rate=5
response = table.put_item(
   Item={
        'gname': gname,
        'gid': gid,
	'rate': rate,
        'info': {
            'plot':"Nothing happens at all.",
            'rating': decimal.Decimal(0)
        }
    }
)

print("Item successfully added:")
print(json.dumps(response, indent=4, cls=DecimalEncoder))

