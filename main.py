#!/usr/bin/python3
# coding: utf-8

from libs.getchar import getChar as getchar
from utils import utils as utils_init
from config import config as config_init
from chat import chat as chat_init
u = utils_init()
config = config_init()
chat = chat_init()


def Main():
    u.info('''---
Welcome to CmdlineAI v1!
Copyright (c)2024 wyf9. All rights reserved.
''')

    u.env_debug = config.cget('debug')
    u.debug('Debug ON')

    while True:
        u.info('''---
[Select]
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
                    u.info('Selected: Settings')
                    Settings()
                    break
                case 'n' | 'N':
                    u.info('Selected: NewChat')
                    NewChat()
                case 'c' | 'C':
                    u.info('Selected: ChatList')
                    ChatList()
                case '\x03' | '\x1a':  # ^C / ^Z
                    u.warning('Received ^C/^Z, quitting.')
                    exit(1)
                case _:
                    pass

def Settings():
    u.warning('[Choose] Load configs? (y/...)')
    choose = input('> ')
    if not (choose == 'y' or choose == 'Y'):
        return 0
    u.info('Config now:')
    config.load()
    for name, value in config.cfg.items():
        print(f"'{name}': '{value}'")
    while True:
        print('[Tip] r -> return')
        inp = input('[Select] edit: ')
        if inp == 'r' or inp == 'R':
            break
        else:
            u.info(f"Editing: {repr(inp)}")
            u.info(f"Value now: {repr(config.cget(inp))}")
            print('[Tip] c -> cancel')
            inp_v = input('[Input] Value: ')
            if inp_v == 'c' or inp_v == 'C':
                continue
            else:
                config.cset(inp, inp_v)
                u.info(f"{repr(inp)} set to {repr(config.cget(inp))}")

def NewChat():
    pass

def ChatList():
    pass

if __name__ == "__main__":
    Main()