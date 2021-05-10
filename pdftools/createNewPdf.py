
from reportlab.pdfgen.canvas import Canvas



def generatePdf(pdfName):
    canvas = Canvas("./pdftools/pdfAssets/"+pdfName+".pdf")
    canvas.drawString(72, 300, "Hello, First Page in " + pdfName)
    canvas.showPage()
    canvas.drawString(72, 300, "Hello, Second Page in " + pdfName)
    canvas.showPage()
    canvas.drawString(72, 300, "Hello, Third Page in "+pdfName)
    canvas.showPage()
    canvas.save()

generatePdf("PDF1")
generatePdf("PDF2")
generatePdf("PDF3")