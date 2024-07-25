# coding: utf-8

import json
import os
import utils as u


class chat:
    def __init__(self, name):
        self.name = name

    def load(self):
        with open(f'data/chat/{self.name}.json', 'r', encoding='utf-8') as file:
            return json.load(file)

    def save(self, value):
        with open(f'data/chat/{self.name}.json', 'w+', encoding='utf-8') as file:
            json.dump(value, file, indent=4, ensure_ascii=False)
