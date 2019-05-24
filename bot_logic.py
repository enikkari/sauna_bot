from call_apis import post_to_flowdock, post_to_slack
import logging
import datetime as dt

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s %(name)s:%(lineno)d - %(message)s")
logger = logging.getLogger(__name__)


W_GENDER = "Women"
M_GENDER = "Men"


def _get_message(weeknumber):
    first_shift = W_GENDER if weeknumber % 2 == 0 else M_GENDER
    secondshift = M_GENDER if first_shift == W_GENDER else W_GENDER

    message = f"<!channel> It's sauna day! Remember to turn on the sauna!\n\n" \
              f"{first_shift} first (week {weeknumber}):\n\n" \
              f"{first_shift}'s sauna: 17-18:30\n" \
              f"{secondshift}'s sauna: 18:30-20:00\n" \
              f"Mixed: 20:00 -> (and all other times)"
    return message


def send_message_to_flowdock(token, flow_token, bot_name="saunabot"):
    weeknumber = dt.datetime.today().isocalendar()[1]
    logger.info(f'This is week {weeknumber}')
    try:
        message = _get_message(weeknumber)

        post_to_flowdock(token,
                         flow_token,
                         bot_name,
                         message)
    except BaseException as e:
        logger.info(e)


def send_message_to_slack(token, channel_name):
    weeknumber = dt.datetime.today().isocalendar()[1]
    logger.info(f'This is week {weeknumber}')
    try:
        message = _get_message(weeknumber)

        post_to_slack(token,
                      channel_name,
                      message)
    except BaseException as e:
        logger.info(e)
