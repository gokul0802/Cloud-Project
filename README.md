# Cloud-Project
# **Mass Email Sender with AWS Lambda & SES**

## Description
This project is a fully automated mass email sender built using AWS services such as **S3**, **SES**, **Lambda**, **EventBridge**, **CloudWatch Logs**, and **IAM**. The system is designed to read contacts from a CSV file stored in an S3 bucket, personalize the emails using an HTML template, and send the emails to the contacts using Amazon SES.

The project leverages AWS Lambda for processing, EventBridge for scheduling, and CloudWatch for monitoring and logging.

## **Features**
- **AWS Lambda**: Handles the logic for reading contacts, personalizing the email, and sending them via SES.
- **Amazon S3**: Stores the contacts CSV file and the email HTML template.
- **Amazon SES**: Sends personalized emails to the contacts.
- **EventBridge**: Triggers the Lambda function to run on a schedule (e.g., weekly, monthly).
- **CloudWatch Logs**: Monitors and logs the Lambda function execution for troubleshooting and debugging.
- **IAM Policies**: Proper IAM roles and permissions ensure that Lambda has the necessary access to SES, S3, and CloudWatch.

## **Components**
1. **CSV File in S3**: A CSV file containing contact information (`FirstName` and `Email`).
2. **Email Template in S3**: An HTML email template with placeholders (e.g., `{{FirstName}}`).
3. **AWS Lambda**: A Lambda function that reads the CSV, personalizes the email, and sends it via SES.
4. **SES**: Amazon Simple Email Service (SES) for sending emails.
5. **EventBridge**: A scheduled rule to trigger the Lambda function periodically.
6. **CloudWatch Logs**: Logs the function’s execution and status.

## **Technologies Used**
- **AWS Lambda**
- **Amazon SES (Simple Email Service)**
- **Amazon S3**
- **Amazon EventBridge**
- **Amazon CloudWatch Logs**
- **IAM Roles and Policies**
- **Python**

## **Setup Instructions**

### 1. **Create an S3 Bucket**
   - Create an S3 bucket to store your CSV file and email template.
   - Upload your `contacts.csv` file and `email_template.html` to the S3 bucket.

### 2. **Create IAM Role**
   - Create an IAM role for your Lambda function with the necessary policies to interact with S3, SES, and CloudWatch.
   - Attach the role to the Lambda function.

### 3. **Deploy Lambda Function**
   - Deploy the `lambda_function.py` code to AWS Lambda.
   - Make sure your Lambda function has the correct permissions for accessing SES, S3, and CloudWatch.

### 4. **Set up Amazon SES**
   - Verify your email domain with Amazon SES.
   - Use SES to send emails from a verified email address.

### 5. **Configure EventBridge**
   - Create a scheduled rule on Amazon EventBridge to trigger the Lambda function periodically (e.g., weekly).

### 6. **Monitor Logs**
   - Use CloudWatch Logs to monitor the execution and troubleshoot any errors.

## **Project Workflow**
1. **CSV File**: A CSV file containing contacts (`FirstName` and `Email`) is stored in an S3 bucket.
2. **Email Template**: An HTML email template with placeholders like `{{FirstName}}` is fetched from the S3 bucket.
3. **Lambda Execution**: AWS Lambda fetches the contacts, personalizes the email content by replacing the placeholders with actual names, and sends the emails through SES.
4. **EventBridge Trigger**: The Lambda function is triggered automatically at a scheduled time using EventBridge.
5. **Logs**: Logs are captured in CloudWatch for monitoring and debugging.

## **Important Links**
- [AWS S3 Documentation](https://docs.aws.amazon.com/s3/)
- [Amazon SES Documentation](https://docs.aws.amazon.com/ses/)
- [AWS Lambda Documentation](https://docs.aws.amazon.com/lambda/)
- [Amazon EventBridge Documentation](https://docs.aws.amazon.com/eventbridge/)
- [CloudWatch Logs Documentation](https://docs.aws.amazon.com/cloudwatch/)
- [IAM Roles and Policies Documentation](https://docs.aws.amazon.com/IAM/)

## **Contributing**
Feel free to open an issue or submit a pull request if you have any improvements or suggestions.

## **License**
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

By using AWS services like SES, Lambda, and S3, this project provides a powerful and scalable solution for mass email sending with minimal effort. Happy emailing!

