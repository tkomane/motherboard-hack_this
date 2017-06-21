#!/usr/bin/env python3

"""
A Python script that extracts metadata from jpg images.
This includes things like location, camera-make, date-taken etc.

By Tshiamo Komane
"""

from PIL import Image  # makes use of the pillow library
from PIL.ExifTags import TAGS

image = Image.open("image.jpg")
info = image._getexif()  # creates a dictionary with tag-value exif data

for tag, value in info.items():
    key = TAGS.get(tag, tag)
    print(key + " " + str(value))  # outputs Exif data

print("#################################################################")
