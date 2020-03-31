function CreateQRPayCode(sum, email) {

    var qrcode = new QRCode("test", {
        width: 200,
        height: 200,
        colorDark: "#000000",
        colorLight: "#ffffff",
        correctLevel: QRCode.CorrectLevel.H
    });

    qrcode.makeCode(CreatePayPalLink(sum, email, currencyCode));

    function CreatePayPalLink(sum, email) {
        return ("https://www.paypal.com/cgi-bin/webscr?cmd=_xclick&business=" +
            email + "&amount=" + sum + "&currency_code=" + currencyCode + "&item_name=test");
    }
}


