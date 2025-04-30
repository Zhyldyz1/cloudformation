from aws_cdk import (
    aws_ec2 as ec2,
    aws_iam as iam,
    core  # For CDK v1. Use "aws_cdk as cdk" for CDK v2
)

class SecurityStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        # Create a VPC
        vpc = ec2.Vpc(self, "MyVPC", max_azs=2)

        # Create a Security Group
        security_group = ec2.SecurityGroup(
            self, "MySecurityGroup",
            vpc=vpc,
            description="Allow SSH and HTTP",
            allow_all_outbound=True
        )

        # Allow inbound SSH (port 22)
        security_group.add_ingress_rule(
            ec2.Peer.any_ipv4(),
            ec2.Port.tcp(22),
            "Allow SSH access from anywhere"
        )

        # Allow inbound HTTP (port 80)
        security_group.add_ingress_rule(
            ec2.Peer.any_ipv4(),
            ec2.Port.tcp(80),
            "Allow HTTP access from anywhere"
        )

        # IAM Role for EC2
        ec2_role = iam.Role(
            self, "MyEC2Role",
            assumed_by=iam.ServicePrincipal("ec2.amazonaws.com"),
            managed_policies=[
                iam.ManagedPolicy.from_aws_managed_policy_name("AmazonSSMManagedInstanceCore")
            ]
        )

