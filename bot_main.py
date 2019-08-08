import os
import schedule, time
import logging

from bot_logic import send_message_to_slack

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s %(name)s:%(lineno)d - %(message)s")
logger = logging.getLogger(__name__)

SLACK_TOKEN = os.environ["SLACK_TOKEN"]


def send_turn_on_sauna_message():
    send_message_to_slack(token=SLACK_TOKEN,
                          channel_name="hki-sauna",
                          ping_channel=True)


def send_general_info():
    send_message_to_slack(token=SLACK_TOKEN,
                          channel_name="helsinki",
                          ping_channel=False)


if __name__ == '__main__':
    schedule.every().friday.at("12:12").do(send_general_info)
    schedule.every().friday.at("15:28").do(send_turn_on_sauna_message)
    while True:
        schedule.run_pending()
        time.sleep(1)
