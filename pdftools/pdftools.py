from PyPDF2 import PdfFileReader
from PyPDF2 import PdfFileMerger
from pathlib import Path
# pdf_path = (Path.home())

# pdf1 = PdfFileReader(str('./pdftools/pdfAssets/PDF1.pdf'))
# page1 = pdf1.getPage(0)
pdf_merger = PdfFileMerger()

pdf_merger.append('/Users/changlyu/Documents/project/python_in_ML/pdftools/pdfAssets/PDF1.pdf', pages=(2,3))
pdf_merger.append(str('./pdftools/pdfAssets/PDF2.pdf'), pages=(1,2))
pdf_merger.append(str('./pdftools/pdfAssets/PDF3.pdf'), pages=(2,3))

with Path("./pdftools/pdfAssets/combined_pdf.pdf").open(mode="wb") as output_file:
    pdf_merger.write(output_file)



def processMerge(fileNames):
    pdfMerger = PdfFileMerger()
    pdfMerger.append('/Users/changlyu/Documents/project/python_in_ML/pdftools/pdfAssets/PDF1.pdf')
    pdfMerger.append(fileNames)
    print('processing merging')
    with Path("./pdftools/pdfAssets/merged_pdf.pdf").open(mode="wb") as output_file:
        pdfMerger.write(output_file)
