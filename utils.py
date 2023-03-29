from haystack.nodes import TextConverter, PDFToTextConverter, PDFToTextOCRConverter, DocxToTextConverter

# PDF to text parser
def pdf_to_text(filepath, filedetails):
    doc = PDFToTextConverter(
        remove_numeric_tables=True,
        valid_languages=["en"],
        ).convert(filepath, meta=filedetails)
    return doc

