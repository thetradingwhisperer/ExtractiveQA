from haystack.nodes import TextConverter, PDFToTextConverter, PDFToTextOCRConverter, DocxToTextConverter
import tempfile
import streamlit as st

# PDF to text parser
def parse_file_to_doc(filepath, filedetails, file_type=None):
    if file_type == "pdf":
        doc = PDFToTextConverter(remove_numeric_tables=True,
                                    valid_languages=["en"],
                                    ).convert(filepath, meta=filedetails)
    elif file_type == "docx":
        doc = DocxToTextConverter(remove_numeric_tables=True,
                                    valid_languages=["en"],
                                    ).convert(filepath, meta=filedetails)
    elif file_type == "txt":
        doc = TextConverter(remove_numeric_tables=True,
                                    valid_languages=["en"],
                                    ).convert(filepath, meta=filedetails)
    else:
        doc = None
        st.error("File type not supported")
    return doc

# Get file details and save in temp folder
def save_and_parse_file(uploaded_file):
    file_details = {"filename": uploaded_file.name, "content_type": uploaded_file.type}
    # create a temporary folder
    with tempfile.TemporaryDirectory() as temp_dir:
        #Save the uploaded file to the temporary folder
        file_path = temp_dir + '/' + uploaded_file.name
        with open(file_path, 'wb') as f:
            f.write(uploaded_file.getbuffer())
            doc = parse_file_to_doc(file_path, file_details, file_type=uploaded_file.name.split('.')[-1])
            return doc
