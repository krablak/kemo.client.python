var encrypted;

// Send the #to_encrypt string to be encrypted by Python and populate the Encryption Result Section
$("#do_encrypt").click(function () {
    var post_data = {
        to_encrypt: $("#to_encrypt").val()
    };

    $.post("/encrypt", post_data, function (data) {
        encrypted = data;
        $("#encrypt_key").val(data.key);
        $("#encrypt_iv").val(data.iv);
        $("#encrypt_ct").val(data.ciphertext);

        $("#do_decrypt").removeAttr("disabled");
    });
});

// Output the decryption result to #decrypted, based on encrypted data from #do_encrypt
$("#do_decrypt").click(function () {
    var key = CryptoJS.enc.Hex.parse(encrypted.key),
        iv = CryptoJS.enc.Hex.parse(encrypted.iv),
        cipher = CryptoJS.lib.CipherParams.create({
            ciphertext: CryptoJS.enc.Base64.parse(encrypted.ciphertext)
        }),
        result = CryptoJS.AES.decrypt(cipher, key, {iv: iv, mode: CryptoJS.mode.CFB});

    $('#decrypted').val(result.toString(CryptoJS.enc.Utf8));

});


$("#do_encrypt").click(function () {
    var post_data = {
        to_encrypt: $("#to_encrypt").val()
    };

    $.post("/encrypt", post_data, function (data) {
        encrypted = data;
        $("#encrypt_key").val(data.key);
        $("#encrypt_iv").val(data.iv);
        $("#encrypt_ct").val(data.ciphertext);

        $("#do_decrypt").removeAttr("disabled");
    });
});


function encrypt(message, key) {



}

function decrypt(ivciphertext, key) {

var iv = ivciphertext.substring(0,32);
var ciphertext = ivciphertext.substring(32);

var key = CryptoJS.enc.Hex.parse(key);
var iv = CryptoJS.enc.Hex.parse(iv);
var cipher = CryptoJS.lib.CipherParams.create({
            ciphertext: CryptoJS.enc.Base64.parse(ciphertext)
        });
var result = CryptoJS.AES.decrypt(cipher, key, {iv: iv, mode: CryptoJS.mode.CFB});
console.log(result.toString(CryptoJS.enc.Utf8));
}