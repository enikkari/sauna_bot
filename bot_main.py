import os
import schedule, time
import logging

from bot_logic import send_message_to_slack

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s %(name)s:%(lineno)d - %(message)s")
logger = logging.getLogger(__name__)


def main():
    slack_token = os.environ["SLACK_TOKEN"]
    channel_name = os.environ["CHANNEL_NAME"]
    # bot_name = os.environ["BOT_NAME"]

    send_message_to_slack(token=slack_token,
                          channel_name=channel_name)


if __name__ == '__main__':
    run_at = "15:30"
    logger.info(f'Running time: {run_at}')
    schedule.every().friday.at(run_at).do(main)
    while True:
        schedule.run_pending()
        time.sleep(1)
