import time
import uiautomator2 as u2

def run(args):
    print(args)
    match args.command:
        case 'run':
            d = u2.connect()
            skill = d(text="DELAY STRIKE III")
            rematch = d(text='REMATCH')
            while True:
                if skill.exists:
                    skill.click()
                elif rematch.exists:
                    rematch.click()
                time.sleep(0.5)
        case _:
            raise ValueError(f"the command '{args.command}' does not supported.")
