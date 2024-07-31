# coding: utf-8

import json
import os
from utils import utils as utils_init
u = utils_init()
from libs.jsonc_parser.parser import JsoncParser as jsonp


# def initJson():
    # try:
        # jsonData = 

        # with open(u.get_datapath('data/config.json'), 'w+', encoding='utf-8') as file:
            # json.dump(jsonData, file, indent=4, ensure_ascii=False)
    # except:
        # u.error('Create config.json failed')
        # raise
def initJson():
    try:
        jsonData = jsonp.parse_file(u.get_datapath('example.jsonc'), encoding='utf-8')
        with open(u.get_datapath('data/config.json'), 'w+', encoding='utf-8') as file:
            json.dump(jsonData, file, indent=4, ensure_ascii=False)
    except:
        u.error('Create config.json failed')
        raise

class config:
    def __init__(self):
        if not (os.path.exists(u.get_datapath('data/config.json'))):
            u.warning('config.json not exist, creating')
            initJson()
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