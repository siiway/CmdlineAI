#!/usr/bin/python3
# coding: utf-8

from libs.getchar import getChar as getchar
from utils import utils as utils_init
u = utils_init()
from config import config as config_init
config = config_init()
from chat import chat as chat_init
# 后面: chat = chat_init(name)
from chatting import chatting as chatting_init
# 后面: chatting = chatting_init(...)

def Main():
    '''
    主程序
    '''
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
                    continue
            break

def Settings():
    '''
    设置界面
    '''
    u.warning('[Choose] Load configs? (y/...)')
    choose = getchar()
    u.debug(f'getChar choose: {repr(choose)}')
    if not (choose == 'y' or choose == 'Y'):
        return 0
    u.info('Config now:')
    config.load()
    for name, value in config.cfg.items():
        print(f"'{name}': '{value}'")
    while True:
        print('[Tip] r -> return')
        inp = input('[Input] edit: ')
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
    '''
    创建新会话
    '''
    print('[Tip] c -> cancel')
    chat_name = input('[Input] Chat name: ')
    if chat_name == 'c' or chat_name == 'C':
        return 0
    else:
        u.info(f'Start chat: {repr(chat_name)}')
        config.load()
        chat = chat_init(chat_name)
        chatting = chatting_init(
            api_base_url = config.cfg['api_base_url'],
            account_id = config.cfg['account_id'],
            api_token = config.cfg['api_token'],
            model = config.cfg['model'],
        )
        conversation = [  # init chat list
            {"role": "system", "content": config.cfg['prompt']},
        ]
        print('''[Tip]
- /s -> Send
- /q -> Quit the chat''')
        while True:
            all_msg = ''
            print('[Input]')
            while True:
                msgn = input(config.cfg['prompt-when-input'])
                match msgn:
                    case '/s': # send
                        break
                    case '/q': # quit
                        u.info('Quitting chat')
                        return 0
                    case _: # default: add msg
                        all_msg += f'{msgn}\n'
            conversation += [{"role": "user", "content": all_msg},]
            u.debug(f'all_msg: {repr(all_msg)}')
            u.info('Querying')
            output = chatting.run(conversation)
            u.debug(f'output: {output}')
            if output['success']:
                print(f'''[Response]
-```
{output['result']['response']}
```-''')
                conversation += [{"role": "assistant", "content": output['result']['response']}]
                chat.save(conversation)
            else:
                u.error(f'''Error!
All Response:
{u.format_dict(output)}''')
                conversation.pop() # its a list!!!
                u.debug('Pop last user input')
                continue

def ChatList():
    '''
    会话列表
    '''
    pass

def OpenChat():
    '''
    打开会话
    will move from NewChat()
    '''
    pass

if __name__ == "__main__":
    Main()