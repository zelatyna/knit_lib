# knit_lib
Library of parsed and indexed old knitting magazines.

Domestic knitting machines were much more popular in 70s - 90s of 20. century. 
Some of the manufactureres like japanese "Brother knitting machines" are not produced anymore and hence resources for finding patterns are quite limited.
There are pages with collections of old knitting magazines but those are difficult search through when looking for specific term like "sock".
This project aims to parse the 

Challenges so far:
- pdfs are scanned and hence extraction of pdf content is not possible with Apache Tika
- converting pdfs to images deminishes the quality aof the text which is not recognized by OCR (Object Character recognition)

## Resources

Some websites with old knitting patterns magazines
http://machineknittingetc.com/brother-knitking/patterns-and-magazines.html

Article on parsing and indexing pdfs with Python
http://beenje.github.io/blog/posts/parsing-and-indexing-pdf-in-python/


Ideas on tools (for computer generated pdfs)
- Apache Tika for extracting PDF content
- Elastic Search or Algolia

UPDATE:
For scanned pdfs following approach
pdf -> image -> text from image

OpenCV OCR and text recognition with Tesseract 
https://www.pyimagesearch.com/2018/09/17/opencv-ocr-and-text-recognition-with-tesseract/

https://medium.com/@justinboylantoomey/fast-text-extraction-with-python-and-tika-41ac34b0fe61we

Libraries:
 pytesseract, cv2, and PIL.

