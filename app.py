# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
from bot_logics.bot_logic import _get_todays_message
import re
import logging
from bot_logics.sauna_state_storage import Sauna

app = Flask(__name__)
sauna_state = Sauna()
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s %(name)s:%(lineno)d - %(message)s")
logger = logging.getLogger(__name__)


@app.route("/")
def index():
    return sauna()


@app.route("/foundation")
def foundation():
    return render_template('foundation.html')


@app.route("/sauna")
def sauna():
    return render_template('sauna.html', text=_get_todays_message(ping_channel=False))


if __name__ == "__main__":
    logger.info('Start host')
    app.run(host='0.0.0.0', port=8000)
