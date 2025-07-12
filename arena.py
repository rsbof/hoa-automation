import time
import uiautomator2 as u2

def run():
    d = u2.connect()
    skill = d(text="DELAY STRIKE III")
    rematch = d(text='REMATCH')
    while True:
        if skill.exists:
            skill.click()
        else if rematch.exists:
            rematch.click()
        time.sleep(0.5)

run()
