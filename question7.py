import boto3
import json
def main():
iam=boto3.client('iam')
ec2=boto3.client('ec2',region_name="us-east-1")
ec2_instance=''
path='/'
ProfileName=""
RoleName=""
description="testing bucket policy"
trust_policy={
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "createRole",
      "Effect": "Allow",
      "Principal": {
        "Service": "ec2.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
 	]
}
tags=[
    {
        'Key': '',
        'Value': ''
    }
]
try:
    
    #creating a role
    response = iam.create_role(
        Path=path,
        RoleName=RoleName,
        AssumeRoleS3_FA_Policyument=json.dumps(trust_policy),
        Description=description,
        MaxSessionDuration=3600,
        Tags=tags
    )

    print(response)
#creating a policy

        S3_FA_Policy={"Version": "2012-10-17",
     "Statement": [
       	{
       	   	"Effect": "Allow",
       	   	"Action": "s3:*",
       	   	"Resource": "*"
        }
    ]
   	
        }
        policy= iam.create_policy( PolicyName="S3_FA",S3_FA_Policyument=json.dumps(S3_FA_Policy) )
       	attaching_policy=iam.attach_role_policy(RoleName=RoleName,PolicyArn=policy['Policy']['Arn'])

instance_profile= iam.create_instance_profile( InstanceProfileName=ProfileName, Path=path)  #creating the profile instance
response= iam.add_role_to_instance_profile(InstanceProfileName=ProfileName,RoleName=RoleName) #attach role to the instance
associate=ec2.describe_iam_instance_profile_associations(Filters=[{'Name': 'instance-id','Values': [ec2_instance,]}]) #Associating instance profile with ec2
AssociationId=associate['IamInstanceProfileAssociations'][0]['AssociationId']
print(instance_profile)
res =ec2.replace_iam_instance_profile_association(
    IamInstanceProfile={
        'Arn': instance_profile['InstanceProfile']['Arn'],# place your arn instance_profile here 
        'Name': ProfileName
    },
    AssociationId=AssociationId
)
except Exception as e:
        print("Error")
        raise e
if __name__=='__main__':
        main()
