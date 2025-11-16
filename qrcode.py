# import qrcode
# url = input("Enter the url: ").strip()

# file_path = "Module and library//qrcode.png"

# qr = qrcode.QRCode()
# qr.add_data(url)

# img = qr.make_image()
# img.save(file_path)

# print("qr code generated")
import qrcode

url = input("Enter URL: ")
img = qrcode.make(url)
img.save("qrcode.png")
