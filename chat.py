# coding: utf-8

import json
import os
from utils import utils as utils_init
u = utils_init()


class chat:
    '''
    单个对话存储
    '''

    def __init__(self, name):
        self.name = name

    def load(self):
        with open(u.get_datapath(f'data/chat/{self.name}.json'), 'r', encoding='utf-8') as file:
            return json.load(file)

    def save(self, value):
        with open(u.get_datapath(f'data/chat/{self.name}.json'), 'w+', encoding='utf-8') as file:
            json.dump(value, file, indent=4, ensure_ascii=False)


def initChatList():
    with open(u.get_datapath('data/chatlist.json'), 'w+', encoding='utf-8') as file:
        json.dump([], file, indent=4, ensure_ascii=False)


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
            self.chat_list = json.load(file)

    def save(self):
        with open(u.get_datapath('data/chatlist.json'), 'w+', encoding='utf-8') as file:
            json.dump(self.chat_list, file, indent=4, ensure_ascii=False)

    def lst(self):
        '''
        获取列表
        '''
        self.load()
        return self.chat_list

    def new(self, dic):
        '''
        新增一项 (写入必须包含 `id`, 否则无法删除!)
        @param dic: 存入的对话信息 (字典)
        '''
        self.load()
        self.chat_list += [dic]
        self.save()

    def get(self, id):
        '''
        获取指定 `id` 的一项
        @param id: ↑ 已经解释了
        '''
        self.load()
        for n in self.chat_list:
            try:
                if n['id'] == id:
                    return n
            except:
                pass
        return None

    def remove(self, id):
        '''
        删除一项
        @param id: 删除目标字典中的 `id`
        '''
        self.load()
        flag = False
        for o in self.chat_list:
            try:
                if o['id'] == id:
                    del o['id']
                    flag = True
            except:
                pass
        self.save()
        return flag
