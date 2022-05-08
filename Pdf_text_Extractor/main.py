
from PyPDF2 import PdfFileReader

reader = PdfFileReader("Chapter-14 Biomolecules.pdf.pdf")
number_of_pages = reader.numPages
page = reader.pages[0]
# print(reader.documentInfo)
# print(reader.getpage())

for i in range(1,20):
    str = ''
    # Extract text from the page
    text = reader.getPage(i).extractText()
    str += text

with open('file.txt','w',encoding='utf-8') as f:
    f.write(str)
