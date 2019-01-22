import os
import schedule, time
import logging

from bot_logic import send_message

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s %(name)s:%(lineno)d - %(message)s")
logger = logging.getLogger(__name__)


def main():
    flowdock_token = os.environ["FLOWDOCK_TOKEN"]
    flow_token = os.environ["FLOW_TOKEN"]
    bot_name = os.environ["BOT_NAME"]

    send_message(flowdock_token=flowdock_token,
                 flow_token=flow_token,
                 bot_name=bot_name)


if __name__ == '__main__':
    run_at = "12:06"
    logger.info(f'Running time: {run_at}')
    schedule.every().friday.at(run_at).do(main)
    while True:
        schedule.run_pending()
        time.sleep(1)
