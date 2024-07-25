# coding: utf-8

import json
import os
from utils import utils as utils_init
u = utils_init()


def initJson():
    try:
        jsonData = {
            'version': 1,
            'debug': False,
            'account_id': None,
            'api_token': None,
            'api_base_url': 'https://api.cloudflare.com/client/v4/accounts/{account_id}/ai/run/',
            'model': '@cf/qwen/qwen1.5-7b-chat-awq',
            'prompt': '',
            'prompt-when-input': '',
        }

        with open(u.get_datapath('data/config.json'), 'w+', encoding='utf-8') as file:
            json.dump(jsonData, file, indent=4, ensure_ascii=False)
    except:
        u.error('Create config.json failed')
        raise


# 检测是否存在
if not (os.path.exists(u.get_datapath('data/config.json'))):
    u.warning('config.json not exist, creating')
    initJson()

class config:
    def __init__(self):
        with open(u.get_datapath('data/config.json'), 'r', encoding='utf-8') as file:
            self.cfg = json.load(file)
    def load(self):
        with open(u.get_datapath('data/config.json'), 'r', encoding='utf-8') as file:
            self.cfg = json.load(file)
    def save(self):
        with open(u.get_datapath('data/config.json'), 'w+', encoding='utf-8') as file:
            json.dump(self.cfg, file, indent=4, ensure_ascii=False)
    def cset(self, name, value):
        self.cfg[name] = value
        with open(u.get_datapath('data/config.json'), 'w+', encoding='utf-8') as file:
            json.dump(self.cfg, file, indent=4, ensure_ascii=False)
    def cget(self, name):
        with open(u.get_datapath('data/config.json'), 'r', encoding='utf-8') as file:
            self.cfg = json.load(file)
            try:
                gotcfg = self.cfg[name]
            except:
                gotcfg = None
            return gotcfg