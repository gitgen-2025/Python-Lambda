# Sends order confirmation email via SES

import boto3

ses = boto3.client('ses')

def lambda_handler(event, context):
    email = event['customer_email']
    order_id = event['order_id']

    ses.send_email(
        Source='noreply@yourstore.com',
        Destination={'ToAddresses': [email]},
        Message={
            'Subject': {'Data': f'Order Confirmation - #{order_id}'},
            'Body': {
                'Text': {
                    'Data': f'Thank you for your purchase!\nYour order #{order_id} is confirmed.'
                }
            }
        }
    )
    return {"status": "email_sent"}
