# ⚡️ AWS Lambda Cheat Sheet for E-Commerce

A **modular collection** of AWS Lambda functions to automate common backend tasks in e-commerce platforms.

---

## 🧩 Functions Overview

| 📄 File                          | 🔧 Purpose                                                                 |
|----------------------------------|---------------------------------------------------------------------------|
| [`send_order_email.py`](send_order_email.py)         | ✉️ Send order confirmation email via **Amazon SES**                      |
| [`trigger_inventory_sync.py`](trigger_inventory_sync.py) | 🚚 Start **ECS Fargate task** to sync inventory with suppliers           |
| [`generate_sales_report.py`](generate_sales_report.py) | 📊 Generate and upload **daily sales report** to **Amazon S3**          |
| [`suspicious_login_alert.py`](suspicious_login_alert.py) | 🚨 Alert on suspicious login activity via **Amazon SNS**                |

---

## 🛠️ Setup Instructions

To deploy these functions:

1. Ensure your AWS environment includes necessary permissions:

   - ✅ **SES** – for sending emails
   - ✅ **ECS** – to run Fargate tasks
   - ✅ **S3** – for storing reports
   - ✅ **SNS** – for notifications

2. You can deploy using:

   - 🖥️ **AWS Console** (quick setup)
   - 🧪 **AWS SAM** (Serverless Application Model)
   - 📦 **Terraform** or **Serverless Framework**

---

## 🌐 Recommended IAM Permissions

> You can use a dedicated IAM role per function or a shared role with scoped policies.

```json
{
  "Version": "*****",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "ses:SendEmail",
        "ecs:RunTask",
        "s3:PutObject",
        "sns:Publish"
      ],
      "Resource": "*"
    }
  ]
}
