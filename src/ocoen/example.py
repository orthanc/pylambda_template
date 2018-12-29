import logging
import json

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def handle_event(event, context):
    logger.info('Recieved Event: ' + json.dumps(event))
