import qrcode
from PIL import Image

def generate_qr_code(text, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=3,
    )

    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="#0000")

    logo = Image.open("logo.png")
    logo_w, logo_h = logo.size

    # Scale the logo to 1/10 of the QR code size
    qr_size = img.size[0]
    logo_scale = qr_size / (10 * logo_w)
    logo = logo.resize((int(logo_w * logo_scale), int(logo_h * logo_scale)))

    # Calculate the center position for the logo
    pos = ((qr_size - logo.size[0]) // 2, (qr_size - logo.size[1]) // 2)

    # Paste the logo into the QR code
    img.paste(logo, pos)

    img.save(filename)

# Input text to generate QR code for
text = "LINK"

# File name to save the QR code image
file_name = "qr_code.png"

generate_qr_code(text, file_name)
print(f"QR Code {file_name} created.")
