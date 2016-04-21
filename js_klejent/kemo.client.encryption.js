var kemo = function(kemo) {
  kemo.encryption = kemo.encryption || {};

  var toBytes = function(str) {
    var bytes = [];
    if (str) {
      for (var i = 0; i < str.length; ++i) {
        bytes.push(str.charCodeAt(i));
      }
    }
    return bytes;
  };

  kemo.encryption.encrypt = function(key, message) {
    var key_sha256 = CryptoJS.SHA256(key).toString();
    var key_hex = CryptoJS.enc.Hex.parse(key_sha256);
    var iv = CryptoJS.lib.WordArray.random(16);
    var encrypted = CryptoJS.AES.encrypt(message, key_hex, {iv: iv,  mode: CryptoJS.mode.CFB});
    return CryptoJS.enc.Hex.stringify(iv)+encrypted;
  };

  kemo.encryption.decrypt = function(key, ivciphertext) {
    var key_sha256 = CryptoJS.SHA256(key).toString();
    var key_hex = CryptoJS.enc.Hex.parse(key_sha256);
    var iv = ivciphertext.substring(0,32);
    var iv = CryptoJS.enc.Hex.parse(iv);
    var ciphertext = ivciphertext.substring(32);
    var cipher = CryptoJS.lib.CipherParams.create({
            ciphertext: CryptoJS.enc.Base64.parse(ciphertext)
        });
    var result = CryptoJS.AES.decrypt(cipher, key_hex, {iv: iv, mode: CryptoJS.mode.CFB});
    return result.toString(CryptoJS.enc.Utf8);
  };

  return kemo;
}(kemo || {});
