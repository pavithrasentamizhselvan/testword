import PyPDF2
obj=open('C:\\Users\\swami\\Documents\\hack.pdf','rb')
read=PyPDF2.PdfFileReader(obj)
print(read.numPages)
page=read.getPage(6)
print(page.extractText())
obj.close()
