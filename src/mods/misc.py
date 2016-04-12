__author__ = 'jesus'

#http://www.network-science.de/ascii/
# ogre, puffy, rounded, shadow, small, standard

KEMO_ASCII = [" _                                           _        ",
              "| | _____ _ __ ___   ___      _ __ ___   ___| | _____ ",
              "| |/ / _ \ '_ ` _ \ / _ \    | '__/ _ \ / __| |/ / __\ ",
              "|   <  __/ | | | | | (_) | _ | | | (_) | (__|   <\__ \ ",
              "|_|\_\___|_| |_| |_|\___/ |_||_|  \___/ \___|_|\_\___/",
              " "]


KEMO_ASCII_SMALL = [" _                                 _       ",
                    "| |_____ _ __  ___     _ _ ___  __| |__ ___",
                    "| / / -_) '  \/ _ \ _ | '_/ _ \/ _| / /(_-<",
                    "|_\_\___|_|_|_\___/|_||_| \___/\__|_\_\/__/"]

def sys_msg(ui, msg):
    ui.chatbuffer_add("[SYSTEM] %s" % msg)

def print_top_logo(ui):
    for line in KEMO_ASCII_SMALL:
        ui.userlist.append(line)
    ui.redraw_userlist()


def print_logo(ui):
    for line in KEMO_ASCII:
        ui.chatbuffer_add(line)

def print_help(ui):
    help = """

*******************************************
*  Commands:
*     :h, :help - this help
*     :q        - quit Kemo
*     :key      - shows secret key
*******************************************

"""
    for line in help.split("\n"):
        ui.chatbuffer_add(line)