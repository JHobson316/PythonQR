import qrcode
import qrcode.image.svg

run = True
while run == True:
    link = input("Please enter a link to create a QR code for. ")
    qr = qrcode.QRCode(version = 1, box_size = 5, border = 5)
    qr.add_data(link)

    qr.make()
    img = qr.make_image(fill_color = (4, 134, 194), back_color = 'black', error_correction=qrcode.constants.ERROR_CORRECT_L, style = horizontalBars)
    img.save('qrGen.png')
