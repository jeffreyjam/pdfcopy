from PyPDF2 import PdfFileMerger
import os
import glob

merger = PdfFileMerger()

# directory = 'pdfs_to_combine'
for filepath in glob.iglob('pdfs_to_combine/*'):
    merger.append(filepath)

merger.write("result.pdf")
