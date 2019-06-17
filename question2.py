import boto3
client = boto3.client('s3')                
client.download_file('akash-peassignement-2', 'sample1.txt', 'f1',ExtraArgs={'VersionId':'5XKbeOEX29MoNTh_fdBj3JLtReSOkAxJ'}) #parameter passes are the bucketname, file to be downloaded, destination where to be downloaded, version id of the the file

