QUnit.test("Simple encryption/decryption scenario.", function(assert) {
  // Prepare test data
  var keyStr = "someStrKey";
  var message = "Some test message text.";

  // Perform encryption
  // TODO Base64 string at se nerozbije pri prenosi a cteni na ruznejch platformach?
  var encryptedMessage = kemo.encryption.encrypt(keyStr, message);
  assert.ok(encryptedMessage !== null && encryptedMessageAsStr !== undefined, "Basic encrypted data checks.");

  // Decrypt data
  var decryptedMessage = kemo.encryption.decrypt(keyStr, encryptedMessage);

  assert.equal(decryptedMessage, message, "Source and decrypted message should be same.");
});

QUnit.test("Empty data encryption/decryption scenario.", function(assert) {
  // Prepare test data
  var keyStr = "someStrKey";
  var message = "";

  // Perform encryption
  var encryptedMessage = kemo.encryption.encrypt(keyStr, message);
  assert.ok(encryptedMessage !== null && encryptedMessageAsStr !== undefined, "Basic encrypted data checks.");

  // Decrypt data
  var decryptedMessage = kemo.encryption.decrypt(keyStr, encryptedMessage);

  assert.equal(decryptedMessage, message, "Source and decrypted message should be same.");
});

QUnit.test("Smoke test module initialization check.", function(assert) {
  assert.ok(kemo, "Kemo module exists.");
  assert.ok(kemo.encryption, "Kemo encryption module exists.");
});



/*
QUnit.test("Run encryption function with wrong or missing arguments.", function(assert) {
  assert.ok(kemo.encryption.encrypt(), "Encryption without args should no fails.");
  assert.ok(kemo.encryption.encrypt(null, null), "Encryption with null args should not fail.");
  assert.ok(kemo.encryption.encrypt("", null), "Encryption with null args should not fail.");
  assert.ok(kemo.encryption.encrypt("", ""), "Encryption with null args should not fail.");
  assert.ok(kemo.encryption.encrypt("", ""), "Encryption with null empty string args should not fail.");
});

QUnit.test("Run decryption function with wrong or missing arguments.", function(assert) {
  assert.ok(kemo.encryption.decrypt(), "Decryption without args should no fails.");
  assert.ok(kemo.encryption.decrypt(null, null), "Decryption with null args should not fail.");
  assert.ok(kemo.encryption.encrypt("", null), "Decryption with null args should not fail.");
  assert.ok(kemo.encryption.encrypt("", ""), "Decryption with null empty string args should not fail.");
});
/*