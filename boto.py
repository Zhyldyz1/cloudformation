import boto3

# Initialize the CloudFormation client
cloudformation = boto3.client('cloudformation', region_name='us-east-1')

# Name of the stack
stack_name = 'my-cloudformation-stack'

# Simple CloudFormation template as a Python multi-line string
template_body = '''
AWSTemplateFormatVersion: '2010-09-09'
Description: Simple CloudFormation Template to Launch EC2 Instance
Resources:
  MyEC2Instance:
    Type: AWS::EC2::Instance
    Properties:
      InstanceType: t2.micro
      ImageId: ami-05572e392e80aee89
      Tags:
        - Key: Name
          Value: MyEC2InstanceFromPython
'''

# Create the stack
response = cloudformation.create_stack(
    StackName=stack_name,
    TemplateBody=template_body,
    Capabilities=[
        'CAPABILITY_NAMED_IAM',  # Needed if your template creates IAM roles/policies (not needed in this very simple one)
    ]
)

print(f"Stack creation started! Stack ID: {response['StackId']}")
