import logging
import datetime as dt

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s - %(levelname)s %(name)s:%(lineno)d - %(message)s")
logger = logging.getLogger(__name__)


class Sauna:
    sauna_turned_on_at: dt.datetime = None
    sauna_stays_on_n_hours = 6

    def turn_on_sauna(self) -> None:
        self.sauna_turned_on_at = dt.datetime.now()
        logging.info(f'Sauna turned on at {self.get_sauna_turn_on_time()}')

    def is_sauna_on(self) -> bool:
        if (self.sauna_turned_on_at != None) and \
                                dt.datetime.now() - dt.timedelta(self.sauna_stays_on_n_hours) < self.sauna_turned_on_at:
            return True
        return False

    def get_sauna_turn_on_time(self) -> str:
        return str(self.sauna_turned_on_at)
