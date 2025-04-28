import boto3

# Create CloudFormation client
cloudformation = boto3.client('cloudformation', region_name='us-east-1')

# Stack name
stack_name = 'my-iam-role-stack'

# CloudFormation template to create an IAM Role
template_body = '''
AWSTemplateFormatVersion: '2010-09-09'
Description: Simple IAM Role Creation

Resources:
  MySimpleRole:
    Type: AWS::IAM::Role
    Properties:
      RoleName: MySimpleRole
      AssumeRolePolicyDocument:
        Version: '2012-10-17'
        Statement:
          - Effect: Allow
            Principal:
              Service:
                - ec2.amazonaws.com
            Action:
              - sts:AssumeRole
'''

# Create the stack
response = cloudformation.create_stack(
    StackName=stack_name,
    TemplateBody=template_body,
    Capabilities=['CAPABILITY_NAMED_IAM']  # Required for IAM resources
)

print(f"Stack creation started! Stack ID: {response['StackId']}")
