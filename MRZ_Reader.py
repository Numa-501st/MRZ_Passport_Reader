from tkinter import *
import pytesseract
from PIL import Image

root = Tk()
root.title("Passport OCR")

## Get values from MRZ
def get_value_from_mrz(text, key):
    key_position = text.find(key)
    if key_position != -1:
        mrz_substring = text[key_position:]
        value_end = mrz_substring.find('<<', len(key))
        if value_end != -1:
            value = mrz_substring[len(key):value_end].strip().replace('<', ' ')
            # Remove 'GBR' from the given name
            value = value.replace('GBR', '')                ## Removes GBR from Given Name Value
            return value
    return ''


## Populate
def populate_form():
    # Open an image file
    image_path = './passport.png'
    image = Image.open(image_path)

    # Use pytesseract to do OCR on the image
    text = pytesseract.image_to_string(image)

    # Extract values from the MRZ
    surname = get_value_from_mrz(text, '<<')
    given_name = get_value_from_mrz(text, '<')

    # Set the surname and given name in the respective fields
    surname_var.set(surname)
    given_name_var.set(given_name)

# Form fields
surname_var = StringVar()
given_name_var = StringVar()

surname_label = Label(root, text="Surname").grid(row=0, column=0)
given_name_label = Label(root, text="Given Name").grid(row=1, column=0)

surname_entry = Entry(root, textvariable=surname_var)
surname_entry.grid(row=0, column=1)

given_name_entry = Entry(root, textvariable=given_name_var)
given_name_entry.grid(row=1, column=1)

btn = Button(root, text="Extract from Passport", command=populate_form).grid(row=2, column=0)

root.mainloop()
