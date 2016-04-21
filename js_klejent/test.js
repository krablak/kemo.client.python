
function test_all() {

    var key = $('#encrypt_key').val();
    var message = $('#encrypt_ct').val();

    var encrypted = kemo.encryption.encrypt(key, message);
    var decrypted = kemo.encryption.decrypt(key, encrypted);

    $('#2').text(decrypted); //encrypted.ciphertext);

}

