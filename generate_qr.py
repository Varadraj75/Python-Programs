import qrcode

url = "https://www.wikipedia.org"

qr = qrcode.make(url)
qr.save("qrcode.png")

print("QR code generated successfully!")
