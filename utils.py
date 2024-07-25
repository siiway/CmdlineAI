import json
import os
import sys
from colorama import Fore, Style


class utils:
    env_debug = False

    def get_basepath(self):
        '''
        获取 base path (main.py 所在目录)
        '''
        main_py = sys.argv[0]
        return os.path.dirname(main_py)

    def get_datapath(self, path):
        '''
        将相对路径的数据目录改为绝对路径
        @param path: 相对路径
        '''
        return os.path.join(self.get_basepath(), path)

    def info(self, msg, noret=False):
        if noret:
            print(f'{Fore.GREEN}[I]{Style.RESET_ALL} {msg}', end='')
        else:
            print(f'{Fore.GREEN}[I]{Style.RESET_ALL} {msg}')

    def warning(self, msg, noret=False):
        if noret:
            print(f'{Fore.YELLOW}[W]{Style.RESET_ALL} {msg}', end='')
        else:
            print(f'{Fore.YELLOW}[W]{Style.RESET_ALL} {msg}')

    def error(self, msg, noret=False):
        if noret:
            print(f'{Fore.RED}[E]{Style.RESET_ALL} {msg}', end='')
        else:
            print(f'{Fore.RED}[E]{Style.RESET_ALL} {msg}')

    def debug(self, msg, noret=False):
        if self.env_debug:
            if noret:
                print(f'{Fore.BLUE}[D]{Style.RESET_ALL} {msg}', end='')
            else:
                print(f'{Fore.BLUE}[D]{Style.RESET_ALL} {msg}')

    def format_dict(self, dic):
        '''
        列表 -> 格式化 json
        @param dic: 列表
        '''
        return json.dumps(dic, indent=4, ensure_ascii=False, sort_keys=False, separators=(', ', ': '))

    def read_dir(self, dirpath):
        '''
        遍历文件夹
        @param dirpath: 文件夹路径
        '''
        if not os.path.exists(dirpath):
            raise NotADirectoryError(f'{dirpath} not exist.')
        indir_list = []
        for filename in os.listdir(dirpath):
            indir_list += [filename]
        return indir_list

    def remove_json(self, lst):
        '''
        移除列表中每项末尾的 `.json`
        @param lst: 列表
        '''
        lst_after = []
        for i in lst:
            lst_after += [os.path.splitext(i)[0]]
        return lst_after

    def load_json(self, json_name):
        with open(json_name, 'r', encoding='utf-8') as file:
            return json.load(file)
