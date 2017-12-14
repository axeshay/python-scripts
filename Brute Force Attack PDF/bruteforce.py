# 1)Encrypted the PDF

import PyPDF2
import random
#To encrypt PDF using PyPDF2 module
'''pdfFile = PyPDF2.PdfFileReader(open("sample.pdf","rb"))
pdfWriter = PyPDF2.PdfFileWriter()
		
for pages in range(pdfFile.numPages):
    pageobj = pdfFile.getPage(pages)
    pdfWriter.addPage(pageobj)

result = open("encryptedpdf.pdf","wb")
pdfWriter.encrypt('REVIVAL')
pdfWriter.write(result)
result.close()'''

# 2)open the encrypted PDF
result = PyPDF2.PdfFileReader(open("encryptedpdf.pdf","rb"))  # Replace with your filename


# 3) Get random keywords from the textfile
with open("dictionary.txt","r") as f:
    contents = f.read()
for i in range(len(contents)):
    random_words = random.choice(contents.split())
    passWorked = result.decrypt(random_words.upper())
    if(passWorked == 1):
        print("the password is: " + random_words.upper())
        break
    else:
        print(random_words.upper() + " didnt work")
    passLower = result.decrypt(random_words.lower())
    if(passLower == 1):
        print("The Password is: " + random_words.lower())
        break
    else:
        print(random_words.lower() + " Did not work")
        
    

			
