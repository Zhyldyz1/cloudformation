import boto3

ec2 = boto3.resource('ec2', region_name='us-east-1')

for i in range(1, 4):
    ec2.create_instances(
        ImageId='ami-0e449927258d45bc4',
        InstanceType='t2.micro',
        MinCount=1,
        MaxCount=1,
        TagSpecifications=[
            {
                'ResourceType': 'instance',
                'Tags': [{'Key': 'Name', 'Value': f'MyEC2-{i}'}]
            }
        ]
    )