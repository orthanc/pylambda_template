import logging
import json

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def handle_event(event, context):
    logger.info('Recieved Event: ' + json.dumps(event))

    response = {
        "statusCode": 200,
        "headers": {
            "x-custom-header": "my custom header value",
        },
        "body": json.dumps(event, indent=4)
    }
    return response
