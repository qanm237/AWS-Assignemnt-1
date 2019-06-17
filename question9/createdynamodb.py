from __future__ import print_function 
import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')   #connecting to the dynamodb service

#creating the database
table = dynamodb.create_table(
    TableName='gnames',
    KeySchema=[
        {
            'AttributeName': 'gid',
            'KeyType': 'HASH'                              #Creating Partition key
        },
        {
            'AttributeName': 'gname',
            'KeyType': 'RANGE'                             #Creating Sort key
        }
    ],
#Setting the attributes
    AttributeDefinitions=[
        {
            'AttributeName': 'gid',
            'AttributeType': 'N'
        },
        {
            'AttributeName': 'gname',
            'AttributeType': 'S'
        },

    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
)

print("Table status:", table.table_status)             #Printing the status of db created, or failed

