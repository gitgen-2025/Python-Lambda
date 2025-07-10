# Generates a daily sales report and uploads to S3

import boto3
import datetime

s3 = boto3.client('s3')

def lambda_handler(event, context):
    today = datetime.date.today().isoformat()
    report_data = "Date,Total Orders,Revenue\n" + f"{today},52,1349.99\n"

    s3.put_object(
        Bucket='ecommerce-reports',
        Key=f'sales/daily_report_{today}.csv',
        Body=report_data
    )
    return {"status": "report_uploaded"}
