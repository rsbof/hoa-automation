import time
import logging
from logging.handlers import RotatingFileHandler
from typing import Optional
import uiautomator2 as u2
from uiautomator2 import Device, UiObject


def run(args):
    match args.command:
        case 'run':
            sh = logging.StreamHandler()
            sh.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(message)s'))
            logger = logging.getLogger()
            logger.setLevel(logging.INFO)
            logger.addHandler(sh)

            d = u2.connect()
            logging.info("Device connected: %s", d.info)

            d.press(0x7a)
            d(index=1, className='android.widget.TextView', text='Buy').click()
            while True:
                for category in ['material', 'equipped']:
                    time.sleep(1)
                    d.press(0x7a)
                    time.sleep(1)
                    d(index=0, className='android.widget.Image',text=category).click()
                    if category == 'equipped':
                        buy_items(d, 'Arena Token')
                    else:
                        buy_items(d)

                d.press(0x7b)
                restock(d)
        case _:
            raise ValueError(f"the command '{args.command}' does not supported.")

def buy_items(d: Device, item_name: str = None):
    try:
        scrollable_view = d(scrollable=True)
        item_count = scrollable_view.info['childCount']
        start = 14
        end = item_count - 5
        logging.info("Available %s items", (end - start) + 1)
        for i in range(start, end):
            item = scrollable_view.child(index=i, className='android.view.View')
            if not item.exists:
                continue
            name = item.child(index=2, className='android.widget.TextView')
            if not name.exists:
                continue
            top = item.info['bounds']['top']
            d.swipe(0, top, 0, 0)
            if not item_name is None:
                if not name.get_text() == item_name:
                    continue

            buy_all = item.child(className='android.view.View', descriptionContains='BUY ALL') \
                    .child(className='android.widget.TextView', textContains='BUY ALL')
            if buy_all.exists:
                # hold 0.5sec
                logging.info(f"Buying item: {name.get_text()}")
                buy_all.swipe('right', steps=100)
    except Exception as e:
        logging.exception("An error occurred in buy_items")

def restock(d: Device):
    try:
        logging.info("Restocking items")
        scrollable_view = d(scrollable=True)
        restock = scrollable_view.child(className='android.view.View', description='HOLD TO RESTOCK')
        restock.swipe('right', steps=100)
    except Exception as e:
        logging.exception("An error occurred in restock")

if __name__ == "__main__":
    main()
