import time
from typing import Optional
import uiautomator2 as u2
from uiautomator2 import Device, UiObject

def main():
    d = u2.connect()
    d.press(0x7a)
    d(index=1, className='android.widget.TextView', text='Buy').click()
    while True:
        for category in ['material', 'equipped']:
            d.press(0x7a)
            time.sleep(1)
            d(index=0, className='android.widget.Image',text=category).click()
            if category == 'equipped':
                buy_items(d, 'Arena Token')
            else:
                buy_items(d)

        d.press(0x7b)
        restock(d)

def buy_items(d: Device, item_name: str = None):
    scrollable_view = d(scrollable=True)
    item_count = scrollable_view.info['childCount']
    start = 14
    end = item_count - 5
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
            buy_all.swipe('right', steps=100)

def restock(d: Device):
    scrollable_view = d(scrollable=True)
    restock = scrollable_view.child(className='android.view.View', description='HOLD TO RESTOCK')
    restock.swipe('right', steps=100)

if __name__ == "__main__":
    main()
