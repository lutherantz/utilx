import os
import sys
import time
import ctypes
from datetime import datetime

class _CursorInfo(ctypes.Structure):
    _fields_ = [("size", ctypes.c_int),
                ("visible", ctypes.c_byte)]

class Color:
    lred  = "\033[38;2;255;100;100m"
    dgray = "\033[38;2;100;100;100m"
    dred  = "\033[38;2;100;0;0m"
    white  = "\033[38;2;255;255;255m"
    reset = "\033[0m"

class Utils:
    @staticmethod
    def _print(title: str, content: str, newline: bool = True, input: bool = False):
        part = f"{Color.dgray}[{Color.dred}{title}{Color.dgray}] | [{Color.lred}{datetime.now().strftime('%H:%M:%S')}{Color.dgray}] {Color.white}{content}"

        if input:
            return f"{part}"
        if not newline:
            print(f"{part}", end="\r")
        else:
            print(f"{part}")

    @staticmethod
    def display_banner(banner):
        terminal_width = os.get_terminal_size().columns
        return "\n".join(line.center(terminal_width) for line in banner.splitlines())

    @staticmethod
    def title(title: str):
        os.system(f"title {title}" if os.name == "nt" else "")

    @staticmethod
    def clear():
        os.system(f"cls" if os.name == "nt" else "clear")

    @staticmethod
    def hide_cursor():
        if os.name == 'nt':
            ci = _CursorInfo()
            handle = ctypes.windll.kernel32.GetStdHandle(-11)
            ctypes.windll.kernel32.GetConsoleCursorInfo(handle, ctypes.byref(ci))
            ci.visible = False
            ctypes.windll.kernel32.SetConsoleCursorInfo(handle, ctypes.byref(ci))
        elif os.name == 'posix':
            sys.stdout.write("\033[?25l")
            sys.stdout.flush()

    @staticmethod
    def show_cursor():
        if os.name == 'nt':
            ci = _CursorInfo()
            handle = ctypes.windll.kernel32.GetStdHandle(-11)
            ctypes.windll.kernel32.GetConsoleCursorInfo(handle, ctypes.byref(ci))
            ci.visible = True
            ctypes.windll.kernel32.SetConsoleCursorInfo(handle, ctypes.byref(ci))
        elif os.name == 'posix':
            sys.stdout.write("\033[?25h")
            sys.stdout.flush()

    @staticmethod
    def typing(text: str, interval: bool = 0.05):
        for letter in text:
            print(letter, end="", flush=True)
            time.sleep(interval)
        return ""