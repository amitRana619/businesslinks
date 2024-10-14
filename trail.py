import qrcode
name = (input("Enter the name "))

# URL or text you want to encode into the QR code
# data = "https://amitrana619.github.io/businesslinks/"  # Replace with your URL

data = "http://localhost:8000/"
# Create a QR code instance
qr = qrcode.QRCode(
    version=1,  # Size of the QR code (1 is the smallest)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level (L = low)
    box_size=10,  # Size of each box (pixel size)
    border=4  # Border thickness
)

# Add data to the QR code
qr.add_data(data)
qr.make(fit=True)

# Generate the QR code image
img = qr.make_image(fill='black', back_color='white')

# Save the image to a file (PNG format)
img.save(f"{name}_qrcode.png")

print("QR code has been generated and saved as qrcode.png")
