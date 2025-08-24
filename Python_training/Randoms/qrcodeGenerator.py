# pip install qrcode
import qrcode

# Create a QR code instance
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=20,
    border=2
)

# Add link or data
qr.add_data("https://auppunasean.wixsite.com/diplomacyclub")
qr.make(fit=True)

# Create the image
img = qr.make_image(fill="black", back_color="white")

# Save the image with a proper file extension
img.save("Diplomacy_Club_Website_QR.png")

# Show the QR code (optional)
img.show()
