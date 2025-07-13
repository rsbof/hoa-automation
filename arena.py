import time
import uiautomator2 as u2

def run(args):
    match args.command:
        case 'run':
            d = u2.connect()
            skill = d.xpath('//*[@text="DELAY STRIKE III"]')
            rematch = d.xpath('//*[@text="REMATCH"]')
            while True:
                skill.click_exists(timeout=2)
                rematch.click_exists(timeout=2)
        case _:
            raise ValueError(f"the command '{args.command}' does not supported.")
