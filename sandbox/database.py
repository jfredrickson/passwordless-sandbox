import os
import boto3
import time

DYNAMODB_ENDPOINT = os.environ.get("DYNAMODB_ENDPOINT")
SESSIONS_TABLE = os.environ["SESSIONS_TABLE"]
EXPIRATION_DELTA = 1 * 1 * 1 * 60 # days * hours * minutes * seconds

dynamodb = boto3.resource("dynamodb", endpoint_url=DYNAMODB_ENDPOINT)

sessions_table = dynamodb.Table(SESSIONS_TABLE)

def create_session(session_id, email):
    sessions_table.put_item(
        Item={
            "session_id": session_id,
            "email": email,
            "expiration": int(time.time()) + EXPIRATION_DELTA
        }
    )
