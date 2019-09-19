# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
from bot_logics.bot_logic import _get_todays_message, get_this_week_params
import re
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s %(name)s:%(lineno)d - %(message)s")
logger = logging.getLogger(__name__)


@app.route("/")
def index():
    return sauna()

# Here is the new beautiful page
@app.route("/displaysauna")
def displaysauna():
    params = get_this_week_params()
    first_shift = params["first_shift"]
    second_shift = params["second_shift"]
    week = params["weeknumber"]
    inspiration = params["inspiration"]
    return render_template('displaysauna.html',
                           first_shift=first_shift,
                           second_shift=second_shift,
                           week=week,
                           inspiration=inspiration)


@app.route("/refreshingsauna")
def foundation():
    return render_template('refreshingpage.html', text=_get_todays_message(ping_channel=False))


@app.route("/sauna")
def sauna():
    return render_template('sauna.html', text=_get_todays_message(ping_channel=False))


if __name__ == "__main__":
    logger.info('Start host')
    app.run(host='0.0.0.0', port=8000)
