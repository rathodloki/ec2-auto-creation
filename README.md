# Automating AWS EC2 Instance Creation and Management

This Python script uses the Boto3 library to automate the creation and management of AWS EC2 instances. The script can be customized to create and manage instances with different parameters, such as the AMI ID, instance type, and key pair.

## Getting Started

To use this script, you'll need to have Python and the Boto3 library installed. You'll also need to have an AWS account with the necessary permissions to create and manage EC2 instances.

1. Clone or download the repository to your local machine.
2. Install Python and the Boto3 library.
3. Create an IAM user in your AWS account with the necessary permissions to create and manage EC2 instances. Make note of the access key and secret key for the user.
4. Set up your AWS credentials by creating a `~/.aws/credentials` file and adding your access key and secret key. For example:

    ```
    [default]
    aws_access_key_id = YOUR_ACCESS_KEY
    aws_secret_access_key = YOUR_SECRET_KEY
    ```

5. Set up your AWS configuration by creating a `~/.aws/config` file and adding your preferred region. For example:

    ```
    [default]
    region = us-west-2
    ```

6. Customize the script by modifying the parameters for the `run_instances` function. For example, you can change the `ImageId`, `InstanceType`, and `KeyName` to create instances with different specifications.

## Usage

To use the script, simply run it in your terminal using the `python` command:


The script will create an EC2 instance with the specified parameters, add a name tag to the instance, stop, start, and terminate the instance.

## Contributing

If you find a bug or have a suggestion for how to improve the script, please feel free to submit an issue or a pull request. All contributions are welcome!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
