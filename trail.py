# import qrcode
# name = (input("Enter the name "))

# # URL or text you want to encode into the QR code
# # data = "https://amitrana619.github.io/businesslinks/"  

# data = "http://localhost:8000/"
# # Create a QR code instance
# qr = qrcode.QRCode(
#     version=1,  # Size of the QR code (1 is the smallest)
#     error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level (L = low)
#     box_size=10,  # Size of each box (pixel size)
#     border=4  # Border thickness
# )

# # Add data to the QR code
# qr.add_data(data) 
# qr.make(fit=True)

# # Generate the QR code image
# img = qr.make_image(fill='black', back_color='white')

# # Save the image to a file (PNG format)
# img.save(f"{name}_qrcode.png")

# print("QR code has been generated and saved as qrcode.png")



# #with kirusa
# from PIL import Image, ImageDraw, ImageFont
# import qrcode

# # User input for QR code name
# name = input("Enter the name: ")
# data = "http://localhost:8000/"

# # Create a QR code with high error correction (to allow part of it to be overwritten)
# qr = qrcode.QRCode(
#     version=5,  # Adjust this value to make the QR code larger or smaller
#     error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction level
#     box_size=10,  # Size of each box in the QR code
#     border=4,  # Border thickness
# )
# qr.add_data(data)
# qr.make(fit=True)

# # Generate QR code image
# img = qr.make_image(fill='black', back_color='white').convert('RGB')
# img_width, img_height = img.size

# # Create a drawing object
# draw = ImageDraw.Draw(img)

# # Use a font for "Kirusa"
# font_size = 70  # Adjust this font size as needed
# font = ImageFont.truetype("roboto.ttf", size=font_size)  # Ensure you have the font file
# text = "Kirusa"

# # Calculate the text size
# text_bbox = draw.textbbox((0, 0), text, font=font)
# text_width = text_bbox[2] - text_bbox[0]
# text_height = text_bbox[3] - text_bbox[1]

# # Define the size of the blank space in the middle
# clear_box_size = (text_width + 60, text_height + 60)  # Clear box size for "Kirusa"
# clear_box_position = (
#     (img_width - clear_box_size[0]) // 2,  # X position for the clear box
#     (img_height - clear_box_size[1]) // 2  # Y position for the clear box
# )

# # Draw a white rectangle in the middle to clear space
# draw.rectangle(
#     [clear_box_position, (clear_box_position[0] + clear_box_size[0], clear_box_position[1] + clear_box_size[1])],
#     fill='white'
# )

# # Draw the "Kirusa" text in the center of the cleared space
# text_position = (
#     (img_width - text_width) // 2,
#     (img_height - text_height) // 2
# )
# draw.text(text_position, text, font=font, fill='black')

# # Save the final image
# img.save(f"{name}_qrcode.png")

# print(f"QR code with 'Kirusa' text in the middle has been generated and saved as {name}_qrcode.png")




#for different colors 
# from PIL import Image, ImageDraw, ImageFont
# import qrcode

# # User input for QR code name
# name = input("Enter the name: ")
# # data = "http://localhost:8000/"

# data = "https://www.kirusa.com/qr-code"

# # Create a QR code with high error correction
# qr = qrcode.QRCode(
#     version=5,  # Adjust this value to make the QR code larger or smaller
#     error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction level
#     box_size=10,  # Size of each box in the QR code
#     border=4,  # Border thickness
# )
# qr.add_data(data)
# qr.make(fit=True)

# # Generate QR code image in black and white
# img = qr.make_image(fill='black', back_color='white').convert('RGB')
# img_width, img_height = img.size

# # Define the color #AD1F24 (RGB: (173, 31, 36))
# # red_color = (173, 31, 36)  # RGB for #AD1F24
# red_color = (28, 3, 252)
# for x in range(img_width):
#     for y in range(img_height):
#         if img.getpixel((x, y)) == (0, 0, 0):  # Check if the pixel is black
#             img.putpixel((x, y), red_color)  # Change it to #AD1F24

# # Create a drawing object
# draw = ImageDraw.Draw(img)

# # Use a font for "Kirusa"
# font_size = 70  # Adjust this font size as needed
# font = ImageFont.truetype("roboto.ttf", size=font_size)  # Ensure you have the font file
# text = "Kirusa"

# # Calculate the text size
# text_bbox = draw.textbbox((0, 0), text, font=font)
# text_width = text_bbox[2] - text_bbox[0]
# text_height = text_bbox[3] - text_bbox[1]

# # Define the size of the blank space in the middle
# clear_box_size = (text_width + 60, text_height + 60)  # Clear box size for "Kirusa"
# clear_box_position = (
#     (img_width - clear_box_size[0]) // 2,  # X position for the clear box
#     (img_height - clear_box_size[1]) // 2  # Y position for the clear box
# )

# # Draw a white rectangle in the middle to clear space
# draw.rectangle(
#     [clear_box_position, (clear_box_position[0] + clear_box_size[0], clear_box_position[1] + clear_box_size[1])],
#     fill='white'
# )

# # Draw the "Kirusa" text in the center of the cleared space in #AD1F24
# text_position = (
#     (img_width - text_width) // 2,
#     (img_height - text_height) // 2
# )
# draw.text(text_position, text, font=font, fill=red_color)  # Change to #AD1F24

# # Save the final image
# img.save(f"{name}_qrcode.png")

# print(f"QR code with 'Kirusa' text in the middle has been generated and saved as {name}_qrcode.png")

#main

# from PIL import Image, ImageDraw, ImageFont
# import qrcode

# # User input for QR code name
# name = input("Enter the name: ")
# data = "https://www.kirusa.com/qr-code"

# # Create a QR code with high error correction
# qr = qrcode.QRCode(
#     version=5,  # Adjust this value to make the QR code larger or smaller
#     error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction level
#     box_size=10,  # Size of each box in the QR code
#     border=4,  # Border thickness
# )
# qr.add_data(data)
# qr.make(fit=True)

# # Generate QR code image in black and white
# img = qr.make_image(fill='black', back_color='white').convert('RGB')
# img_width, img_height = img.size

# # Define the color #AD1F24 (RGB: (173, 31, 36))
# # red_color = (173, 31, 36)  # RGB for #AD1F24
# color = (65,65,65)
# for x in range(img_width):
#     for y in range(img_height):
#         if img.getpixel((x, y)) == (0, 0, 0):  # Check if the pixel is black
#             img.putpixel((x, y), color)  # Change it to #AD1F24

# # Load the logo image (qr_logo.jpg)
# logo = Image.open("qr_logo.png")

# # Resize the logo to fit in the QR code (reduce or increase size as needed)
# logo_size = (img_width // 3, img_height // 5)  # 1/5th of the QR code size
# logo = logo.resize(logo_size)

# # Define the size of the blank space in the middle
# clear_box_size = logo_size  # Use the logo size for clearing space

# # Adjust the Y-coordinate to move the logo upwards
# clear_box_position = (
#     (img_width - clear_box_size[0]) // 2,  # X position for the clear box
#     (img_height - clear_box_size[1]) // 2 + 10  # Y position, decreased to move up
# )

# # Create a drawing object to clear the space
# draw = ImageDraw.Draw(img)
# draw.rectangle(
#     [clear_box_position, (clear_box_position[0] + clear_box_size[0], clear_box_position[1] + clear_box_size[1])],
#     fill='white'
# )

# # Paste the logo image in the center of the cleared space
# img.paste(logo, clear_box_position)

# # Save the final image
# img.save(f"{name}_qrcode.png")

# print(f"QR code with logo moved up has been generated and saved as {name}_qrcode.png")



# #black background 
# from PIL import Image, ImageDraw, ImageFont, ImageOps
# import qrcode

# # User input for QR code name
# name = input("Enter the name: ")
# data = "https://www.kirusa.com/qr-code"

# # Create a QR code with high error correction
# qr = qrcode.QRCode(
#     version=5,  # Adjust this value to make the QR code larger or smaller
#     error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction level
#     box_size=10,  # Size of each box in the QR code
#     border=3  # Border thickness
# )
# qr.add_data(data)
# qr.make(fit=True)

# # Generate QR code image with black background and white foreground
# img = qr.make_image(fill='black', back_color='white').convert('RGB')

# # Invert the colors to get white QR code on black background
# img = ImageOps.invert(img)
# img_width, img_height = img.size
# # Load the logo image (qr_logo.png)
# logo = Image.open("qr_logo.png")

# # Resize the logo to fit in the QR code (reduce or increase size as needed)
# logo_size = (img_width // 3 + 6, img_height // 5 + 3)  # 1/5th of the QR code size
# logo = logo.resize(logo_size)

# # Define the size of the blank space in the middle
# clear_box_size = logo_size  # Use the logo size for clearing space

# # Adjust the Y-coordinate to move the logo upwards
# clear_box_position = (
#     (img_width - clear_box_size[0]) // 2,  # X position for the clear box
#     (img_height - clear_box_size[1]) // 2 + 10  # Y position, decreased to move up
# )

# # Create a drawing object to clear the space
# draw = ImageDraw.Draw(img)
# draw.rectangle(
#     [clear_box_position, (clear_box_position[0] + clear_box_size[0], clear_box_position[1] + clear_box_size[1])],
#     fill='white'
# )

# # Paste the logo image in the center of the cleared space
# img.paste(logo, clear_box_position)

# # Save the final image
# img.save(f"{name}_qrcode.png")

# print(f"QR code with logo moved up has been generated and saved as {name}_qrcode.png")






from PIL import Image, ImageDraw, ImageFont, ImageOps
import qrcode

# User input for QR code name
name = input("Enter the name: ")
data = "https://www.kirusa.com/qr-code"
dark_cyan = (0, 128, 128)
# Create a QR code with high error correction
qr = qrcode.QRCode(
    version=5,  # Adjust this value to make the QR code larger or smaller
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction level
    box_size=10,  # Size of each box in the QR code
    border=3  # Border thickness
)
qr.add_data(data)
qr.make(fit=True)

# Generate QR code image with custom color (white) for foreground and red background
img = qr.make_image(fill='white', back_color=(117, 255, 255)).convert('RGB')

# Invert the colors to get red QR code on white background
img = ImageOps.invert(img)
img_width, img_height = img.size
# Load the logo image (qr_logo.png)
logo = Image.open("qr_logo.png")

# Resize the logo to fit in the QR code (reduce or increase size as needed)
logo_size = (img_width // 3 + 6, img_height // 5 + 3)  # 1/5th of the QR code size
logo = logo.resize(logo_size)

# Define the size of the blank space in the middle
clear_box_size = logo_size  # Use the logo size for clearing space

# Adjust the Y-coordinate to move the logo upwards
clear_box_position = (
    (img_width - clear_box_size[0]) // 2,  # X position for the clear box
    (img_height - clear_box_size[1]) // 2 + 10  # Y position, decreased to move up
)

# Create a drawing object to clear the space
draw = ImageDraw.Draw(img)
draw.rectangle(
    [clear_box_position, (clear_box_position[0] + clear_box_size[0], clear_box_position[1] + clear_box_size[1])],
    fill='white'
)

# Paste the logo image in the center of the cleared space
img.paste(logo, clear_box_position)

# Save the final image
img.save(f"{name}_qrcode.png")

print(f"QR code with logo moved up has been generated and saved as {name}_qrcode.png")
