from tkinter import Tk, Label, Button, filedialog, Entry
# from pdftools import processMerge
from functools import partial
from PyPDF2 import PdfFileMerger
from pathlib import Path
from collections import defaultdict

# 第1步，实例化object，建立窗口window
window = Tk()

# 第2步，给窗口的可视化起名字
window.title('PDF Merge Tool')

# 第3步，设定窗口的大小(长 * 宽)
window.geometry('500x300')  # 这里的乘是小x

# creating a lable widget
label1 = Label(window, text="Step1: Please select pdf files to merge:")
# label2 = Label(window, text="Please select the 2nd pdf to merge:")
filePageDic = defaultdict(list)
filePaths = None
rowCount = -1
columnCount = -1


def getRowCount(newRow):
    global rowCount
    if newRow:
        rowCount += 1
    return rowCount


def getColumnCount(newColumn):
    global columnCount
    if newColumn:
        columnCount += 1
    return columnCount

# TODO: can I remove global here?


def processMerge():
    pdfMerger = PdfFileMerger()
    global filePaths
    global filePageDic

    for filePath in filePaths:
        entryTupleList = filePageDic.get(filePath)

        for entryTuple in entryTupleList:
            fromPage = int(entryTuple[0].get())
            toPage = int(entryTuple[1].get())
            pdfMerger.append(filePath, pages=(fromPage-1, toPage-1))
    with Path("./pdftools/pdfAssets/merged_pdf.pdf").open(mode="wb") as output_file:
        pdfMerger.write(output_file)


# todo: make from and to only accept numbers,
# TODO: make from and to only access numbers in page range
# TODO: make from and to show default value 
def processFileInfor():
    global filePaths
    global filePageDic
    filePaths = filedialog.askopenfilenames(
        initialdir="./", title="Select a PDF", filetypes=[("pdf files", ".pdf")])
    for filePath in filePaths:
        fileName = filePath.split("/")[-1]
        Label(window, text="File Name is: " +
              fileName).grid(row=getRowCount(True), column=0)

        Label(window, text="Page From:").grid(row=getRowCount(False), column=1)
        entryFrom = Entry(window, width=5)
        entryFrom.grid(row=getRowCount(False), column=2)

        Label(window, text="Page To:").grid(row=getRowCount(False), column=3)
        entryTo = Entry(window, width=5)
        entryTo.grid(row=getRowCount(False), column=4)

        filePageDic[filePath].append((entryFrom, entryTo))

    button2.grid(row=getRowCount(True), column=0)


button1 = Button(window, text="load files",
                 command=lambda: () == processFileInfor())
# button2 = Button(window, text="process",
#                  command=testprint)
button2 = Button(window, text="process",
                 command=partial(processMerge))

# label3 = Label(window, text="File Path is: "+filePath1)

# shoving it onto the screen,放置标签
label1.grid(row=getRowCount(True), column=getColumnCount(True))
# label3.grid(row=0, column=2)
button1.grid(row=getRowCount(False), column=getColumnCount(True))
button2.grid(row=2, column=0)
# 第6步，主窗口循环显示
window.mainloop()
# 注意，loop因为是循环的意思，window.mainloop就会让window不断的刷新，如果没有mainloop,就是一个静态的window,传入进去的值就不会有循环，mainloop就相当于一个很大的while循环，有个while，每点击一次就会更新一次，所以我们必须要有循环
# 所有的窗口文件都必须有类似的mainloop函数，mainloop是窗口文件的关键的关键。
