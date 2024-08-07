# coding: utf-8

import json
import os
from utils import utils as utils_init
u = utils_init()
from libs.jsonc_parser.parser import JsoncParser as jsonp


def initJson():
    try:
        jsonData = jsonp.parse_file(u.get_datapath('example.jsonc'), encoding='utf-8')
        with open(u.get_datapath('data/config.json'), 'w+', encoding='utf-8') as file:
            json.dump(jsonData, file, indent=4, ensure_ascii=False)
    except:
        u.error('Create config.json failed!')
        raise

class config:
    def __init__(self):
        if not (os.path.exists(u.get_datapath('data/config.json'))):
            u.warning('config.json not exist, creating')
            initJson()
        self.load()
    def load(self):
        self.cfg = u.load_json(u.get_datapath('data/config.json'))
    def save(self):
        self.load()
        with open(u.get_datapath('data/config.json'), 'w+', encoding='utf-8') as file:
            json.dump(self.cfg, file, indent=4, ensure_ascii=False)
    def cset(self, name, value):
        self.load()
        self.cfg[name] = value
        with open(u.get_datapath('data/config.json'), 'w+', encoding='utf-8') as file:
            json.dump(self.cfg, file, indent=4, ensure_ascii=False)
    def cget(self, name):
        self.load()
        try:
            gotcfg = self.cfg[name]
        except:
            gotcfg = None
        return gotcfg