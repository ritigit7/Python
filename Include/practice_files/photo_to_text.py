import pytesseract
from PIL import Image

image_path = "D:\Screenshots\Screenshot 2023-06-02 155802.png"

image = Image.open(image_path)

# Convert the image to text
text = pytesseract.image_to_string(image)

# Print the text
print(text)
