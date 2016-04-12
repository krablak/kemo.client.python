__author__ = 'jesus'

import enc_tools
import websocket
import logging
from datetime import datetime as dt
import threading
import misc
from cryptogej import Cryptor
import hashlib
import binascii
import time

logging.basicConfig(filename='logs/kemo.log', level=logging.DEBUG)

DATE_FORMAT = "%H:%M:%S"

class Kemo(object):

    def __init__(self, ui, name, secret_key):
        #self.wsurl = "ws://kemoundertow-krablak.rhcloud.com:8000/messaging/"
        self.wsurl = "wss://kemoundertow-krablak.rhcloud.com:8443/messaging/"
        self.name = name
        self.ui = ui
        self.secret_key = secret_key
        self.sec_key_sha256_hex = hashlib.sha256(secret_key).hexdigest()
        self.test_msg_arrived = False
        self.c = Cryptor

        url = "%s%s/" % (self.wsurl, enc_tools.key_to_address(self.secret_key))
        logging.debug("connecting to '%s'" % url)
        self.ws = websocket.WebSocketApp(url,
                                    on_message=self.on_message,
                                    on_error=self.on_error,
                                    on_close=self.on_close)
        self.start_ws_thread()

    def start_ws_thread(self):
        self.ws_thread = threading.Thread(target=self.initialize_connection)
        self.ws_thread.start()

    def initialize_connection(self):
        self.ws.on_open = self.on_open
        #websocket.enableTrace(True)
        self.ws.run_forever()

    def on_open(self, ws):
        test_msg = "Echoed test message, welcome to Kemo!"

        self.send_msg(test_msg)
        logging.debug("Opening websocket")

    def on_message(self, ws, enc_message):
        try:
            message = self.decrypt(enc_message)
            self.ui.chatbuffer_add("%s %s" % (dt.now().strftime(DATE_FORMAT), message))
            self.test_msg_arrived = True
        except:
            self.ui.chatbuffer_add("Le decrypt erreur!")

    def on_error(self, ws, error):
        pass

    def on_close(self):
        self.ws.close()

    def send_msg(self, msg):
        if len(msg.strip()) > 0:
            message = "[%s] %s" % (self.name, msg)
            try:
                enc_message = self.encrypt(message)
                self.ws.send(enc_message)
            except:
                self.ui.chatbuffer_add("Le encrypt erreur!")

    def parse_command(self, command):
        if command.strip() in [":h", ":help"]:
            misc.print_help(self.ui)
        elif command.strip() in [":key"]:
            misc.sys_msg(self.ui, "Secret key: "+self.secret_key)
        else:
            misc.sys_msg(self.ui, "Unknown command")

    def encrypt(self, message):
        """
        encrypts to AES
        """
        iv, encrypted = Cryptor.encrypt(message, self.sec_key_sha256_hex)
        cyphertext = binascii.b2a_base64(encrypted).rstrip()
        return iv+cyphertext

    def decrypt(self, encblob):
        """
        decrypts from AES
        """
        iv = encblob[:32]
        cyphertext = encblob[32:]
        decrypted = Cryptor.decrypt(cyphertext, self.sec_key_sha256_hex, iv)
        return decrypted