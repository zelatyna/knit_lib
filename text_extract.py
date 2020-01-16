from tika import parser

file = 'media/knitking_magazine_vol_15_no.6.pdf'
# Parse data from file
file_data = parser.from_file(file)
# Get files text content
text = file_data['content']
print(text)