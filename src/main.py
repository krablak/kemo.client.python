from mods.ui import ChatUI
import mods.kemo_ws
import time
from curses import wrapper

DATE_FORMAT = "%H:%M:%S"
import mods.misc
import logging
logging.basicConfig(filename='logs/kemo.log', level=logging.DEBUG)


def main(stdscr):
    stdscr.clear()
    ui = ChatUI(stdscr)

    mods.misc.print_top_logo(ui)


    mods.misc.sys_msg(ui, "Enter your secret key...")
    secret_key = ui.wait_input("secret key: ")
    #ui.userlist.append(secret_key)
    ui.redraw_userlist()

    mods.misc.sys_msg(ui, "Enter your username...")
    name = ui.wait_input("username: ")
    ui.set_username(name)
    #ui.userlist.append(name)
    ui.redraw_userlist()

    kemo = mods.kemo_ws.Kemo(ui, name, secret_key)

    mods.misc.sys_msg(kemo.ui, "Initializing connection to Kemo pipe")
    while not kemo.test_msg_arrived:  # wait until next round to try is the first message arrived
        time.sleep(0.5)
    mods.misc.print_logo(ui)
    mods.misc.sys_msg(kemo.ui, "Kemo connection established, you can start chatting now.")
    mods.misc.sys_msg(kemo.ui, "Enter :h or :help to see list of commands")

    user_input = ""

    try:
        while user_input != ":q":
            logging.debug("Waiting for input")
            user_input = ui.wait_input("input: ")
            if user_input.startswith(":"):  # all commands start with : like in vim
                kemo.parse_command(user_input)
            else:
                kemo.send_msg(user_input)
        kemo.on_close()
    except KeyboardInterrupt:
            kemo.on_close()

    #also maybe close the thread

if __name__ == "__main__":
    wrapper(main)
