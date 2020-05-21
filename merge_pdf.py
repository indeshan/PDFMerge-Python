from urllib2 import Request,urlopen
from pyPdf import PdfFileWriter,PdfFileReader
from StringIO import StringIO
import time,datetime
import threading

class PdfDownloader:

	def __init__(self):
		self.pdfList = []

	def dPdf(self,url,i):
		remoteFile = urlopen(Request(url)).read()
		memoryFile = StringIO(remoteFile)
		pdfFile = PdfFileReader(memoryFile)
		self.pdfList.append(pdfFile)

	def logic1(self):
		start = time.time()
		print "Starting PDF Fetching at: %s" % (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
		urls = ["https://www.example.com/1.pdf",
"https://www.example.com/2.pdf",
"https://www.example.com/3.pdf",
"https://www.example.com/4.pdf",
"https://www.example.com/5.pdf",
"https://www.example.com/6.pdf",  
"https://www.example.com/7.pdf",
"https://www.example.com/8.pdf",
"https://www.example.com/9.pdf",
"https://www.example.com/10.pdf",
"https://www.example.com/11.pdf",
"https://www.example.com/12.pdf",
"https://www.example.com/13.pdf",
"https://www.example.com/14.pdf",
"https://www.example.com/15.pdf",
"https://www.example.com/16.pdf",
"https://www.example.com/17.pdf",
"https://www.example.com/18.pdf",
"https://www.example.com/19.pdf",
"https://www.example.com/20.pdf",  
"https://www.example.com/21.pdf",
"https://www.example.com/22.pdf",
"https://www.example.com/23.pdf",
"https://www.example.com/24.pdf",
"https://www.example.com/25.pdf"]
		writer = PdfFileWriter()
		count = 0
		threadLists = []
		for i,url in enumerate(urls):
			thread = threading.Thread(target=self.dPdf,args=(url,i))
			count = count+1
			thread.name = "T%d" % count
			threadLists.append(thread)

		for it in threadLists:
			it.start()

		for it in threadLists:
			it.join()

		print "PDF Fetch completed at: %s" % (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
		end1 = time.time()
		print "%s sec to fetch 100 PDFs" % (end1 - start)
		print "Starting PDF merging at: %s" % (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                for pdf in  self.pdfList:
			for pageNum in xrange(pdf.getNumPages()):
				currentPage = pdf.getPage(pageNum)
				writer.addPage(currentPage)

		outputStream = open("merged_pdf.pdf","wb")
		writer.write(outputStream)
		outputStream.close()
		end = time.time()
		print "Completed PDF merging at: %s" % (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
		print "%s sec to fetch and merge 100 PDFs" % (end - start)
		print "Open file merged_pdf.pdf"

obj = PdfDownloader()
obj.logic1()
