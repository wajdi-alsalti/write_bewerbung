import os
import win32com.client as client
from PyPDF2 import PdfFileMerger, PdfFileReader, PdfFileWriter
from PySide2.QtWidgets import QFileDialog


def convert_to_pdf(filepath:str):
    """Save a pdf of a docx file."""
    try:
        word = client.DispatchEx("Word.Application")
        target_path = filepath.replace(".docx", r".pdf")
        word_doc = word.Documents.Open(filepath)
        word_doc.SaveAs(target_path, FileFormat=17)
        word_doc.Close()
    except Exception as e:
            raise e
    finally:
            word.Quit()


def pdfMerge():
    """open file dialog and chose pfd files to merge"""
    filename = QFileDialog.getOpenFileNames(filter="*.pdf")
    pdfsFiles = filename[0] # a list of selected files
    if pdfsFiles: # check if the list not empty
        merger = PdfFileMerger()
        for file in pdfsFiles:
            merger.append(file)
        merger.write("merged.pdf")
        merger.close()
    else:
        raise IOError


def pdfSplitter():
    """open file dialog and chose pfd file to split"""
    filename = QFileDialog.getOpenFileNames(filter="*.pdf")
    pdfsFiles = filename[0][0]
    if pdfsFiles: # check if the list not empty
        fileName = os.path.splitext(os.path.basename(pdfsFiles))[0]
        pdf = PdfFileReader(pdfsFiles)
        for page in range(pdf.getNumPages()):
            pdf_writer = PdfFileWriter()
            pdf_writer.addPage(pdf.getPage(page))
            output_filename = '{}_page_{}.pdf'.format(
                fileName, page+1)
            with open(output_filename, 'wb') as out:
                pdf_writer.write(out)
