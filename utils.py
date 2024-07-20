import json
from colorama import Fore, Style

class utils:
    env_debug = False
    def info(self, msg):
        print(f'{Fore.GREEN}[I]{Style.RESET_ALL} {msg}')
    def warning(self, msg):
        print(f'{Fore.YELLOW}[W]{Style.RESET_ALL} {msg}')
    def error(self, msg):
        print(f'{Fore.RED}[E]{Style.RESET_ALL} {msg}')
    def debug(self, msg):
        if self.env_debug:
            print(f'{Fore.BLUE}[D]{Style.RESET_ALL} {msg}')
    def format_dict(self, dic):
        return json.dumps(dic, indent=4, ensure_ascii=False, sort_keys=False,separators=(', ', ': '))