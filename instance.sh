#!/bin/bash 

for i in {1..3}; do
  aws ec2 run-instances \
    --image-id ami-05572e392e80aee89 \
    --instance-type t2.micro \
    --region us-west-2 \
    --tag-specifications "ResourceType=instance,Tags=[{Key=Name,Value=aws-session-instance-loop-${i}}]"
done
