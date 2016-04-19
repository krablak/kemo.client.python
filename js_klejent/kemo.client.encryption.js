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

  kemo.encryption.encrypt = function(key, iv, data) {
    return null;
  };

  kemo.encryption.decrypt = function(key, data) {
    return null;
  };

  return kemo;
}(kemo || {});
