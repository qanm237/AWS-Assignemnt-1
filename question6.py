{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": "account:*",
            "Resource": "*",
            "Condition": {
                "IpAddress": {
                    "aws:SourceIp": "210.75.12.75/16" #example IP/CIDR where it is allowed, this can be the organisation ip
                }
            }
        }
    ]
}


