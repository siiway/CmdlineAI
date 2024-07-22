# coding: utf-8

import json
import os
import utils as u


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

        with open('data/config.json', 'w+') as file:
            json.dump(jsonData, file, indent=4, ensure_ascii=False)
    except:
        u.error('Create config.json failed')
        raise

# 检测是否存在
if not (os.path.exists('data/config.json')):
    u.warning('config.json not exist, creating')
    initJson()

class config:
    def __init__(self):
        with open('data/config.json', 'r') as file:
            self.cfg = json.load(file)
    def load(self):
        with open('data/config.json', 'r') as file:
            self.cfg = json.load(file)
    def save(self):
        with open('data/config.json', 'w+') as file:
            json.dump(self.cfg, file, indent=4, ensure_ascii=False)
    def cset(self, name, value):
        self.cfg[name] = value
        with open('data/config.json', 'w+') as file:
            json.dump(self.cfg, file, indent=4, ensure_ascii=False)
    def cget(self, name):
        with open('data/config.json', 'r') as file:
            self.cfg = json.load(file)
            try:
                gotcfg = self.cfg[name]
            except:
                gotcfg = None
            return gotcfg