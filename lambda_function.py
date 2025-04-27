import boto3
import csv

# Initialize S3 and SES clients
s3_client = boto3.client('s3')
ses_client = boto3.client('ses')

def lambda_handler(event, context):
    bucket_name = 'mass-email-gokul'

    try:
        # Fetch CSV file
        csv_file = s3_client.get_object(Bucket=bucket_name, Key='contacts.csv')
        lines = csv_file['Body'].read().decode('utf-8').splitlines()

        # Fetch HTML email template
        email_template = s3_client.get_object(Bucket=bucket_name, Key='email_template.html')
        email_html = email_template['Body'].read().decode('utf-8')

        # Read contacts from CSV
        contacts = csv.DictReader(lines)

        for contact in contacts:
            # Personalize email
            personalized_email = email_html.replace('{{FirstName}}', contact['FirstName'])

            # Send email via SES
            response = ses_client.send_email(
                Source='gokul501.gk@gmail.com',
                Destination={
                    'ToAddresses': [contact['Email']]
                },
                Message={
                    'Subject': {
                        'Data': 'Your Weekly Tiny Tales Mail!',
                        'Charset': 'UTF-8'
                    },
                    'Body': {
                        'Html': {
                            'Data': personalized_email,
                            'Charset': 'UTF-8'
                        }
                    }
                }
            )

            print(f"Email sent to {contact['Email']}: Response {response}")

    except Exception as e:
        print(f"An error occurred: {e}")
