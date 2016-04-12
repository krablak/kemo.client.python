__author__ = 'panda'
import base64
import hashlib
import urllib2

def key_to_address(key):
    """
    return equivalent to return encodeURIComponent(sjcl.codec.base64.fromBits(sjcl.hash.sha256.hash("littlebitof" + key + "salt")));

    JS on key "ahoj":    "PzsI7KYsIddiVubh0Li%2FmfTvvjdvZDNbcvQWOo%2FFDbo%3D"
    this code on "ahoj": 'PzsI7KYsIddiVubh0Li%2FmfTvvjdvZDNbcvQWOo%2FFDbo%3D'

    this will be later converted to tests...
    on "ahoj valdimire mrdej maxovi rit":
    "1qHaow4rhi9ZsYUaG3Owo6EzVJR1TnrXzfaGCo96PnE%3D"
    '1qHaow4rhi9ZsYUaG3Owo6EzVJR1TnrXzfaGCo96PnE%3D'

    JS: encodeURIComponent escapes all characters except the following: alphabetic, decimal digits, - _ . ! ~ * ' ( )
    """
    return urllib2.quote(base64.b64encode(hashlib.sha256("littlebitof" + key + "salt").digest()), safe="%-_.~!*'()")



def salt_key(key):
    """
    var saltKey = function(key) {
        return "clientenc" + key + "salt";
    };
    """
    return "clientenc" + key + "salt"
