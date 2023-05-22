#!/usr/bin/env python3


from controller import BridgeController
from utils.config import configure_from_file


CONFIG_FILE = "../config.ini"


conf = {}


def configure():
    global conf

    conf = configure_from_file(CONFIG_FILE)


def main():

    configure()

    req_start = {
        "action": "start",
        "testbed": "hello",
        "provision": {
            "mote_count": 2,
            "tx_power": 0,
            "tx_intv": 1,
            "hs_len": 0,
            "hopseq": '',
            "analyze_intv": 10
        }
    }

    req_stop = {
        "action": "stop",
        "testbed": "hello"
    }

    while True:

        print('(1) Create testbed\n(2) Destroy Testbed\n')
        option = input('> ')

        if option == '1':
            req = req_start
            print(f'\nCreate testbed: {req}')
        elif option == '2':
            req = req_stop
            print(f'\nDestroy testbed: {req}')
        else:
            print('Invalid option.')
            continue

        res = BridgeController(
            request=req,
            host=conf['addr'],
            port=conf['port'],
            queue=conf['queue']
        ).send()

        print(res)


if __name__ == '__main__':
    main()
