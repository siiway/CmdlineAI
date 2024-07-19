#!/usr/bin/python3
# coding: utf-8

from utils import utils as utils_init
from libs.getchar import getChar as getchar
from config import config as config_init
config = config_init()
u = utils_init()


def Main():
    u.info('''---
    Welcome to CmdlineAI v1!
    Copyright (c)2024 wyf9. All rights reserved.
    ''')

    u.env_debug = config.cfg['debug']
    u.debug('Debug ON')

    while True:
        u.info('''---
        [Tip]
        n -> New chat
        c -> Chat list
        q -> Quit
        s -> Settings
        ''')

        while True:
            gchr = getchar()
            u.debug(f'getChar: {repr(gchr)}')
            match gchr:
                case 'q' | 'Q':
                    u.info('Quit.')
                    exit(0)
                case 's' | 'S':
                    u.info('Settings')
                    Settings()
                    break
                case 'n' | 'N':
                    u.info('NewChat')
                case 'c' | 'C':
                    u.info('ChatList')
                case '\x03' | '\x1a':  # ^C / ^Z
                    u.warning('Received ^C/^Z, quitting.')
                    exit(1)
                case _:
                    pass

def Settings():
    pass

if __name__ == "__main__":
    try:
        Main()
    except err:
        u.error('An unexcept error. Exiting.')
        