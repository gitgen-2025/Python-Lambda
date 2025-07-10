# Sends an alert via SNS if a login occurs from an untrusted IP

import boto3

sns = boto3.client('sns')

TRUSTED_IPS = ['192.0.2.1', '203.0.113.5']  # Example IPs

def lambda_handler(event, context):
    ip = event.get('ip_address')

    if ip not in TRUSTED_IPS:
        sns.publish(
            TopicArn='arn:aws:sns:us-east-1:123456789012:suspicious-logins',
            Subject='Suspicious login detected',
            Message=f"Login from unknown IP: {ip}"
        )

    return {"status": "check_complete"}
