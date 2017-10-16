# -*- coding: utf-8 -*-
from PyPDF2 import PdfFileMerger, PdfFileReader
import base64
import tempfile
from io import StringIO
import magic


def merge(pdf_base64_encoded_list=None):
    pdf_temp_file_list = []

    for i in pdf_base64_encoded_list:
        binary_string = base64.urlsafe_b64decode(str(i))

        if magic.from_buffer(binary_string, mime=True) != 'application/pdf':
            raise Exception('Wrong file. Mime type should be application/pdf')

        f = tempfile.SpooledTemporaryFile()
        f.write(binary_string)
        pdf_temp_file_list.append(f)

    merger = PdfFileMerger(strict=False)

    for pdf_file in pdf_temp_file_list:
        merger.append(PdfFileReader(pdf_file, strict=False))

    pdf_merged_buffer = StringIO.StringIO()
    merger.write(pdf_merged_buffer)

    return base64.urlsafe_b64encode(pdf_merged_buffer.getvalue())
