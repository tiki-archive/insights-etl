import boto3
import requests
import json
import os

KGRAPH_URL = "https://tiki-insights.s3.us-east-2.amazonaws.com/api_response.json"
BUCKET_NAME = "tiki-insights"

def main(args):

    # Connect to API and build insight

    # TODO: Authentication w/ kgraph

    response = requests.get(KGRAPH_URL).json()

    # Build specific insight data from response... see samples/most_frequent_subjects to see what we're building
    insight_data = []

    totalEmails = 0
    for subject in response:
        result = subject[0]
        totalEmails += result["occurrences"]

    for subject in response:
        result = subject[0]

        insight_data.append({
            "key": result["subject"],
            "value": round(100 * result["occurrences"] / totalEmails)
        })

    # build insight using specific data
    insight = {'chart_type': 'PIE', 'chart_data': [
        {
            "filter": "Last 24 Hours",
            "data": insight_data
        }
    ]}
    insight_as_json = json.dumps(insight)

    TEST_ENV = os.getenv('TEST')
    AWS_SERVER_PUBLIC_KEY = os.getenv('AWS_SERVER_PUBLIC_KEY')
    AWS_SERVER_SECRET_KEY = os.getenv('AWS_SERVER_SECRET_KEY')

    # Start S3 session
    # session = boto3.Session(
    #     aws_access_key_id=AWS_SERVER_PUBLIC_KEY,:wqI
    #     aws_secret_access_key=AWS_SERVER_SECRET_KEY,
    # )

    # Upload to S3
    # s3 = session.resource('s3')
    # s3.Bucket(BUCKET_NAME).put_object(Key='companies/amazon/most_frequent_subjects.json', Body=insight_as_json)

    return {"body": "Success! " + TEST_ENV + " AWS PK: " + str(AWS_SERVER_PUBLIC_KEY) + ", AWS SK: " + str(AWS_SERVER_SECRET_KEY)}




