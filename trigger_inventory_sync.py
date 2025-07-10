# Launches an ECS Fargate task to sync inventory

import boto3

ecs = boto3.client('ecs')

def lambda_handler(event, context):
    response = ecs.run_task(
        cluster='ecommerce-cluster',
        launchType='FARGATE',
        taskDefinition='inventory-sync-task',
        networkConfiguration={
            'awsvpcConfiguration': {
                'subnets': ['subnet-xxxxxxx'],
                'assignPublicIp': 'ENABLED'
            }
        }
    )
    return {"status": "inventory_sync_started", "response": response}
