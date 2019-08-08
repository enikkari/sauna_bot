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
        'content-type': "application/json",
        'X-flowdock-wait-for-message': "true"
    }

    resp = requests.post(url, json=payload, headers=headers)
    logger.info(resp.json())


def post_to_slack(slack_token: str, channel_name: str, message: str) -> None:
    message_no_spaces = message.replace(' ', '%20')
    url = f"https://slack.com/api/chat.postMessage?token={slack_token}&channel={channel_name}&text={message_no_spaces}&pretty=1"
    resp = requests.get(url)
    logger.info(resp.json())
