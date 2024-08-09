#!/usr/bin/python3
# coding: utf-8

from chatting import chatting as chatting_init
from chat import chat as chat_init
from chat import chatlist as chatlist_init
from config import config as config_init
import os
from datetime import datetime
from colorama import Fore, Style
from libs.getchar import getChar as getchar
from utils import utils as utils_init
u = utils_init()
config = config_init()
chatlist = chatlist_init()
# 后面: chat = chat_init(name)
# 后面: chatting = chatting_init(...)


def Main():
    '''
    主程序
    '''

    yearnow = datetime.now().year
    u.infos(
        'Welcome to CmdlineAI v1.1!',
        f'Copyright (c){yearnow} wyf9. All rights reserved.')

    u.env_debug = config.cget('debug')
    u.debug('Debug ON')

    while True:
        u.infos(
            '[Select]',
            'n -> New chat',
            'c -> Chat list',
            'q -> Quit',
            's -> Settings')

        while True:
            gchr = getchar()
            u.debug(f'getChar: {repr(gchr)}')
            match gchr:
                case 'q' | 'Q':
                    u.debug('Quit.')
                    exit(0)
                case 's' | 'S':
                    u.debug('Selected: Settings')
                    Settings()
                    break
                case 'n' | 'N':
                    u.debug('Selected: NewChat')
                    NewChat()
                case 'c' | 'C':
                    u.debug('Selected: ChatList')
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
    protect_configs = ['version', 'debug']
    u.warning('[Choose] Load configs? (y/...)')
    choose = getchar()
    u.debug(f'getChar choose: {repr(choose)}')
    if not (choose == 'y' or choose == 'Y'):
        return 0
    u.info('Config now:')
    config.load()
    for name, value in config.cfg.items():
        protect_config_flag = False
        for n in protect_configs:
            if name == n:
                protect_config_flag = True
        if protect_config_flag:
            print(f"'{Fore.RED}{name}{Style.RESET_ALL}': '{value}'")
        else:
            print(f"'{Fore.GREEN}{name}{Style.RESET_ALL}': '{value}'")

    while True:
        print('[Tip] r -> return')
        inp = input('[Input] edit: ')
        if inp == 'r' or inp == 'R':
            break
        protect_config_flag = False
        for i in protect_configs:
            if inp == i:
                protect_config_flag = True
        if protect_config_flag:
            u.error(f"Config {repr(inp)} is in protect list, can't edit.")
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
    config.load()
    print('[Tip] c -> cancel')
    chat_name = input('[Input] Chat name: ')
    if chat_name == 'c' or chat_name == 'C':
        return 0
    else:
        chat_id = chatlist.new(chat_name)
        u.info(f'Start chat: #{chat_id} / `{chat_name}`')
        if config.cfg['prompt'] == '':
            conversation = []
        else:
            conversation = [  # init chat list
                {"role": "system", "content": config.cfg['prompt']},
            ]
        OpenChat(chat_id, conversation)


def ChatList():
    '''
    会话列表
    '''
    chatlist.load()
    lst = chatlist.file['id_list']
    lstnum = 0
    for n in lst:
        try:
            # #1 [2024-08-03 21:06:00] niganma
            # (yellow)#1 (blue)[2024-08-03 21:06:00] (green)niganma
            # print(f'{Fore.GREEN}{n["id"]}{Style.RESET_ALL}')
            print(
                f"#{Fore.YELLOW}{n['id']}{Style.RESET_ALL} {Fore.BLUE}[{n['modtime']}]{Style.RESET_ALL} {Fore.GREEN}{n['name']}{Style.RESET_ALL}")
            lstnum += 1
        except KeyError:
            pass
    if lstnum == 0:
        u.info('None.')
        return 0

    print('[Tip] r -> Return')
    print('[Tip] d [id] -> delete')
    while True:
        raw_chat_id = str(input('[Input] Chat: '))
        if raw_chat_id == 'r' or raw_chat_id == 'R':
            break
        if (raw_chat_id.split(' ', 1)[0] == 'd') and (len(raw_chat_id.split(" ", 1)) > 1):
            u.debug('trydel: yes')
            try:
                real_chat_id = int(raw_chat_id.split(" ", 1)[1])
            except:
                u.error('Invaild input.')
                continue
            u.warning(f'Remove chat #{real_chat_id}? (y/...)')
            gc = getchar()
            if gc == 'y' or gc == 'Y':
                chatlist.remove(real_chat_id)
                u.info(f'Removed #{real_chat_id}')
            else:
                u.info('Cancel.')
                continue
        else:
            u.debug('trydel: no')
            try:
                chat_id = int(raw_chat_id)
            except:
                u.error('Invaild input.')
                continue
            existFlag = False
            for i in chatlist.file['id_list']:
                try:
                    if i['id'] == chat_id:
                        existFlag = True
                        chatobj = i
                except:
                    pass
            if not existFlag:
                u.error(f'#{chat_id} not exist.')
                continue
            else:
                u.info(f'Recover chat #{chat_id}')
                chat_path = os.path.join(u.get_datapath(
                    'data/chat'), raw_chat_id + '.json')
                try:
                    conversation = u.load_json(chat_path)
                except FileNotFoundError:
                    u.error(f'Chat #{chat_id} file `{chat_path}` not exist.')
                    u.warning('Remove this chat in chatlist.json, or create it? (y/c/...)')
                    gc = getchar()
                    match gc:
                        case 'y':
                            chatlist.remove(chat_id)
                            u.info(f'Removed #{chat_id}')
                        case 'Y':
                            chatlist.remove(chat_id)
                            u.info(f'Removed #{chat_id}')
                        case 'c':
                            try:
                                chat_id = int(chat_id)
                            except:
                                u.error('Invaild chat id. cancel.')
                                continue
                            will_create = chatlist.get(chat_id)
                            chat_name = will_create['name']
                            u.info(f'Create chat: #{chat_id} / `{chat_name}`')
                            if config.cfg['prompt'] == '':
                                conversation = []
                            else:
                                conversation = [  # init chat list
                                    {"role": "system", "content": config.cfg['prompt']},
                                ]
                            OpenChat(chat_id, conversation)
                        case 'C':
                            pass
                        case _:
                            u.info('Cancel.')
                            continue
                    # if gc == 'y' or gc == 'Y':
                    #     u.debug('remove in chatlist: ', noret=True)
                    #     u.debug(chatlist.remove(chat_id))
                    #     try:
                    #         os.remove(chat_path)
                    #         u.debug('remove json file: SUCCESS')
                    #     except FileNotFoundError:
                    #         u.debug('remove json file: NOT FOUND')
                    #     u.info(f'Removed #{chat_id}')
                    # else:
                    #     u.info('Cancel.')
                    # continue
                # show history chat
                # system: yellow
                # assistant: blue
                # user: green
                # unknown: red
                u.info('Chat details:')
                print(
                    f'{Fore.BLUE}id{Style.RESET_ALL}: {Fore.GREEN}{chatobj["id"]}{Style.RESET_ALL}')
                print(
                    f'{Fore.BLUE}Name{Style.RESET_ALL}: {Fore.GREEN}{chatobj["name"]}{Style.RESET_ALL}')
                print(
                    f'{Fore.BLUE}Last update{Style.RESET_ALL}: {Fore.GREEN}{chatobj["modtime"]}{Style.RESET_ALL}')
                for c in conversation:
                    match c["role"]:
                        case 'system':
                            print(
                                f'{Fore.YELLOW}system -- {Style.RESET_ALL}: {c["content"]}')
                        case 'assistant':
                            print(
                                f'{Fore.BLUE}assistant -> {Style.RESET_ALL}: {c["content"]}')
                        case 'user':
                            print(
                                f'{Fore.GREEN}user <- {Style.RESET_ALL}: {c["content"]}')
                        case _:
                            print(
                                f'{Fore.RED}{c["role"]} -- {Style.RESET_ALL}: {c["content"]}')

                OpenChat(chat_id, conversation)
                break


def OpenChat(chat_id, conversation):
    '''
    打开会话
    @param chat_id: 用于存储的会话标识符
    @param conversation: 对话体
    '''
    config.load()
    chat = chat_init(chat_id)
    chatting = chatting_init(
        api_base_url=config.cfg['api_base_url'],
        account_id=config.cfg['account_id'],
        api_token=config.cfg['api_token'],
        model=config.cfg['model'],
    )
    u.prints('[Tip]',
             '- /s -> Send',
             '- /b -> Backline',
             '- /q -> Quit the chat')
    while True:
        all_msgs = []
        firstInput = True  # 是否是本次第一行输入
        print(f'{Fore.GREEN}[Input]{Style.RESET_ALL}')
        while True:
            msgn = input(config.cfg['prompt-when-input'])
            match msgn:
                case '/s':  # send
                    break
                case '/b':  # backline
                    try:
                        all_msgs.pop()
                        u.backline(1)
                        # print(config.cfg['prompt-when-input'] + all_msgs[-1])
                    except IndexError:
                        # u.warning('Maybe pop from empty list, ignore.')
                        pass
                case '/q':  # quit
                    u.info('Quitting chat')
                    return 0
                case _:  # default: add msg
                    if firstInput:
                        firstInput = False
                        all_msgs += [msgn]
                    else:
                        all_msgs += ['\n' + msgn]
        all_msg = ''.join(all_msgs)
        conversation += [{"role": "user", "content": all_msg},]
        u.debug(f'all_msg: {repr(all_msg)}')
        u.info('Querying')
        output = chatting.run(conversation)
        u.debug(f'output: {output}')
        if output['success']:
            u.prints(f'{Fore.BLUE}[Response]{Style.RESET_ALL}',
                     f'{output["result"]["response"]}')
            conversation += [{"role": "assistant",
                              "content": output['result']['response']}]
            chat.save(conversation)
            chatlist.update(chat_id)
        else:
            u.error('Error!',
                    'All Response:',
                    f'{u.format_dict(output)}')
            conversation.pop()  # its a list!!!
            u.debug('Pop last user input')
            continue


if __name__ == "__main__":
    Main()
