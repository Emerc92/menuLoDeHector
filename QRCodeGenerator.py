import PIL
import qrcode
from PIL import Image

#####################################################
###### CREAZIONE QRCODE PER MENU RESTAURANT 'LO DE HECTOR' #########
#####################################################

# apro il logo
logo = Image.open("logo.jpg")
logo = logo.convert("RGB")
# misura del logo
logoSize = 100

wPercent = (logoSize / float(logo.size[0]))
hsize = int((float(logo.size[1]) * float(wPercent)))
logo = logo.resize((logoSize, hsize), Image.Resampling.LANCZOS)

# creazione qr code per menu
linkMenu = "https://drive.google.com/file/d/1CMt8lcrNoDWrcNLFwARwtDcXajGZqJ-D/view?usp=sharing"

# 1 genero il qr in formato png
qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
qr.add_data(linkMenu)

# apro il qr come immagine per inserire il logo
qr.make()

qrColor = 'black'

qrImg = qr.make_image(fill_color=qrColor, back_color="white").convert('RGB')

# calcolo misure logo dentro il qrCode
pos = ((qrImg.size[0] - logo.size[0]) // 2,
       (qrImg.size[1] - logo.size[1]) // 2)

# salvo le modifiche
qrImg.paste(logo, pos)
qrImg.save('myMenu.png')
# qrImg.show()
# inserisco il logo nel qrCode
# img.paste(logo, (xmin, ymin, xmax, ymax))
# img.show()
# img.save("newMuenu.png")

# qr.svg('C:/Users/emiliano.mercado/Desktop/qrMenu.svg', scale=15, background="white", module_color="black")
# qr.show()
# se voglio vedere il qr nel terminale
# print(qrImg.terminal())
