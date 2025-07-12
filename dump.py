import uiautomator2 as u2

if __name__ == "__main__":
    d = u2.connect()
    print(d.dump_hierarchy())
