import requests
import logging

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s - %(levelname)s %(name)s:%(lineno)d - %(message)s")
logger = logging.getLogger(__name__)


def post_to_flowdock(flowdock_token, flow_token, bot_name, message):
    url = f"https://{flowdock_token}@api.flowdock.com/messages/chat/{flow_token}"

    payload = \
        {"external_user_name": bot_name,
         "content": f"{message}"}
    headers = {
        'content-type': "application/json"
    }

    requests.post(url, json=payload, headers=headers)
