import qrcode
from PIL import Image

def generate_qr_code_with_logo(text, logo_file_name, file_name):
    # Generate the QR code image without a logo
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="#000000")

    # Open the logo file and convert it to RGBA if it is not already in RGBA format
    logo = Image.open(logo_file_name).convert("RGBA")

    # Resize the logo to fit inside the QR code
    qr_size = img.size[0]
    logo_size = (qr_size // 5, qr_size // 5)
    logo = logo.resize(logo_size)

    # Calculate the position to place the logo at the center of the QR code image
    logo_pos = ((qr_size - logo_size[0]) // 2, (qr_size - logo_size[1]) // 2)

    # Create a new image to hold the QR code and the logo
    qr_with_logo = Image.new("RGBA", (qr_size, qr_size), color=(255, 255, 255, 255))

    # Paste the QR code onto the new image
    qr_with_logo.paste(img, (0, 0))

    # Paste the logo onto the new image at the calculated position
    qr_with_logo.alpha_composite(logo, logo_pos)

    # Save the new image as the output file
    qr_with_logo.save(file_name)

# Input text to generate QR code for
text = "LINK"

# Logo file name
logo_file_name = "logo.png"

# File name to save the QR code image
file_name = "qr_code.png"

generate_qr_code_with_logo(text, logo_file_name, file_name)
print(f"QR Code {file_name} created.")
