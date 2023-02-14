import boto3

# Connect to EC2
ec2 = boto3.client('ec2')

# Create an EC2 instance
instance = ec2.run_instances(
    ImageId='ami-0c55b159cbfafe1f0',
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro',
    KeyName='Loki-2023'
)

# Get the ID of the new instance
instance_id = instance['Instances'][0]['InstanceId']

# Add a name tag to the instance
ec2.create_tags(
    Resources=[instance_id],
    Tags=[{'Key': 'Name', 'Value': 'Auto-created-server'}]
)

# Stop the instance
ec2.stop_instances(InstanceIds=[instance_id])

# Start the instance
ec2.start_instances(InstanceIds=[instance_id])

# Terminate the instance
ec2.terminate_instances(InstanceIds=[instance_id])
