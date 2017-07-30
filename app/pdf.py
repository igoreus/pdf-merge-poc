# -*- coding: utf-8 -*-
from PyPDF2 import PdfFileMerger, PdfFileReader
import base64
import tempfile
import StringIO

def merge(pdf_base64_encoded_list = None):

    pdf_temporaty_file_list = []
    for i in pdf_base64_encoded_list:
        f = tempfile.SpooledTemporaryFile()
        f.write(base64.urlsafe_b64decode(str(i)))
        pdf_temporaty_file_list.append(f)

    merger = PdfFileMerger()

    for pdf_file in pdf_temporaty_file_list:
        merger.append(PdfFileReader(pdf_file))

    pdf_merged_buffer = StringIO.StringIO()
    merger.write(pdf_merged_buffer)

    return base64.urlsafe_b64encode(pdf_merged_buffer.getvalue())

