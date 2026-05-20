import qrcode

resource = "https://univaq-electors-prod.gea.esse3.cineca.it/"
img = qrcode.make(resource)
img.save("qr.png")
