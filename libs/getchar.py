from encodings import utf_8
utf_8
import os

if os.name == 'nt':
    import msvcrt
    def getch():
        try:
            return msvcrt.getch().decode()
        except:
            return None
else:
    import sys, tty, termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    def getch():
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

def getChar():
    wgch = getch()
    try:
        wgch2 = str(wgch)
    except ValueError:
        wgch2 = None
    return wgch2
