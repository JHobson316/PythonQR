import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers.pil import RoundedModuleDrawer
from qrcode.image.styles.moduledrawers.pil import HorizontalBarsDrawer
from qrcode.image.styles.moduledrawers.pil import VerticalBarsDrawer
from qrcode.image.styles.colormasks import RadialGradiantColorMask

qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_L)
link = "https://downloads.khinsider.com/persona"
qr.add_data(link)

img_1 = qr.make_image(image_factory=StyledPilImage, module_drawer=HorizontalBarsDrawer())
img_2 = qr.make_image(image_factory=StyledPilImage, module_drawer=VerticalBarsDrawer())
img_3 = qr.make_image(image_factory=StyledPilImage, color_mask=RadialGradiantColorMask())
img_4 = qr.make_image(image_factory=StyledPilImage, embeded_image_path="./Assets/RSTRCTD.png")

img_1.save("img1.png")
img_2.save("img2.png")
img_3.save("img3.png")
img_4.save("img4.png")