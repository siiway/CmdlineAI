# coding: utf-8

from libs.getchar import getChar as getchar
from colorama import Fore, Style
from libs.jsonc_parser.parser import JsoncParser as jsonp
import json
import os
import time
from utils import utils as utils_init
u = utils_init()


class chat:
    '''
    单个对话存储
    @param id: 对话标识 id
    '''

    def __init__(self, id):
        self.id = id

    def load(self):
        with open(u.get_datapath(f'data/chat/{self.id}.json'), 'r', encoding='utf-8') as file:
            return json.load(file)

    def save(self, value):
        with open(u.get_datapath(f'data/chat/{self.id}.json'), 'w+', encoding='utf-8') as file:
            json.dump(value, file, indent=4, ensure_ascii=False)


def initChatList():
    try:
        jsonData = jsonp.parse_file(u.get_datapath(
            'chat_list.example.jsonc'), encoding='utf-8')
        with open(u.get_datapath('data/chatlist.json'), 'w+', encoding='utf-8') as file:
            json.dump(jsonData, file, indent=4, ensure_ascii=False)
    except:
        u.error('Create config.json failed')
        raise


class chatlist:
    '''
    对话列表存储
    '''

    def __init__(self):
        if not (os.path.exists(u.get_datapath('data/chatlist.json'))):
            u.warning('chatlist.json not exist, creating')
            initChatList()
        self.load()

    def load(self):
        with open(u.get_datapath('data/chatlist.json'), 'r', encoding='utf-8') as file:
            self.file = json.load(file)

    def save(self):
        with open(u.get_datapath('data/chatlist.json'), 'w+', encoding='utf-8') as file:
            json.dump(self.file, file, indent=4, ensure_ascii=False)

    def new(self, name):
        '''
        新增一项
        @param name: 对话名称
        @return: int, 存入对话的 `id`
        '''
        name = str(name)
        id = self.file['last_id'] + 1
        self.load()
        self.file['id_list'] += [{
            'id': id,
            'name': name,
            'modtime': time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        }]
        self.file['last_id'] = id
        self.save()
        return id

    def get(self, id):
        '''
        获取指定 `id` 的一项
        @param id: ↑ 已经解释了
        '''
        self.load()
        try:
            for n in self.file['id_list']:
                try:
                    if n['id'] == id:
                        return n
                except:
                    pass
        except:
            pass
        return None

    def update(self, id):
        '''
        更改指定 `id` 的一项 (~~其实就是更新修改时间~~)
        @param id: ↑ 已经解释了
        @return: bool, 是否成功
        '''
        self.load()
        try:
            for i in range(self.file['last_id']):
                if self.file['id_list'][i]['id'] == id:
                    content = {
                        'id': id,
                        'modtime': time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                    }
                    self.file['id_list'][i] = content
                    self.save()
                    return True
        except:
            pass
        return False

    def remove(self, id):
        '''
        删除一项
        @param id: 删除目标字典中的 `id` -> int
        @return: 是否成功找到该项
        '''
        self.load()
        # for o in self.file['id_list']:
        #     try:
        #         print(o)
        #         print(o['id'])
        #         if o['id'] == id:
        #             del o
        #             flag = True
        #     except:
        #         pass
        try:
            for i in range(self.file['last_id']):
                if self.file['id_list'][i]['id'] == id:
                    del self.file['id_list'][i]
                    self.save()
                    return True
        except:
            pass
        return False

    def reset(self):
        '''
        重置所有
        - 重新生成 `data/chatlist.json`
        - 清空 `data/chat`
        '''
        print(f'{Fore.RED}WARNING{Style.RESET_ALL}: This will do:')
        print(f'- {Fore.RED}Reinit{Style.RESET_ALL} `{u.get_datapath("data/chatlist.json")}`')
        print(f'- {Fore.RED}Clear{Style.RESET_ALL} `{u.get_datapath("data/chat")}`')
        print(f'{Fore.RED}Continue?{Style.RESET_ALL} (y/...) ')
        ok = getchar()
        if ok == 'y' or ok == 'Y':
            initChatList()
            try:
                import shutil
            except:
                pass
            try:
                shutil.rmtree(u.get_datapath('data/chat'))
            except:
                pass
            try:
                os.mkdir(u.get_datapath('data/chat'))
            except:
                pass
            print(f'{Fore.GREEN}Clear ok.{Style.RESET_ALL}')
        else:
            print(f'{Fore.GREEN}Canceled.{Style.RESET_ALL}')
