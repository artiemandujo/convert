
# importing required modules
import PyPDF2

# create a pdf file object
pdfFileObj = open('PDF_to_Text_Python.pdf', 'rb')

# create a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# print number of pages in the pdf file
print("Page Number:", pdfReader.numPages)

# create a page object
pageObj = pdfReader.getPage(0)

# extract text from page
text = pageObj.extractText()

# display just the text
print(text)

# save to a text file for later use
# copy the path where the script and pdf is placed
file1=open(r"C:\Users\hp\Downloads\convertedtext.txt","a")
file1.writelines(text)

# closing the pdf file object
pdfFileObj.close()

# closing the text file object
file1.close()
