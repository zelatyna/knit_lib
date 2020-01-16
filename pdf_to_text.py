from __future__ import print_function

from wand.image import Image

with Image(filename='media/knitking_magazine_vol_15_no.6.pdf', dir='media') as img:

    print('width =', img.width)
    print('height =', img.height)
    print('pages = ', len(img.sequence))
    print('resolution = ', img.resolution)

    with img.convert('png') as converted:
         converted.save(filename='knitking_magazine_vol_15_no.6.png')

