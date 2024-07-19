from colorama import Fore, Style
_debug = False
def info(msg):
    print(f'{Fore.GREEN}[I]{Style.RESET_ALL} {msg}')
def warning(msg):
    print(f'{Fore.YELLOW}[W]{Style.RESET_ALL} {msg}')
def error(msg):
    print(f'{Fore.RED}[E]{Style.RESET_ALL} {msg}')
def debug(msg):
    if _debug:
        print(f'{Fore.RED}[E]{Style.RESET_ALL} {msg}')