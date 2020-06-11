import sys
import imageio
import time
import os
import matplotlib.pyplot as pl

if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    is_exe = True
    bundle_dir = getattr(
        sys, '_MEIPASS', os.path.abspath(
            os.path.dirname(__file__)))
    path_to_res = os.path.join(bundle_dir, 'res')
else:
    is_exe = False
    path_to_res = os.path.join(os.path.dirname(__file__), 'res')


def screen_clear():
    # for mac and linux(here, os.name is 'posix')
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        # for windows platfrom
        _ = os.system('cls')


def timed_print(msg: str, secs: int):
    print(msg, end="", flush=True)
    for _ in range(secs):
        time.sleep(1)
        print(".", end="", flush=True)
    print()


def im_show(filename: str):
    filepath = os.path.join(path_to_res, filename)
    fig = pl.imshow(imageio.imread(filepath))
    fig.axes.get_xaxis().set_visible(False)
    fig.axes.get_yaxis().set_visible(False)
    fig.axes.margins(0, tight=None)
    pl.show()


def close_game():
    if is_exe:
        sys.exit(0)
    else:
        exit()
