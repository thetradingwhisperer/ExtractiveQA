import streamlit as st
from haystack.document_stores import InMemoryDocumentStore
from haystack.nodes import TfidfRetriever, FARMReader
from haystack.pipelines import ExtractiveQAPipeline
import tempfile

from utils import pdf_to_text


# Create a DocumentStore
document_store = InMemoryDocumentStore()


# Upload file
uploaded_file = st.file_uploader(
    "Upload a pdf, docx, txt or csv file",
    type = ['pdf', 'docx', 'txt', 'csv'],
    help="Upload a pdf, docx, txt or csv file - scanned documents are not supported yet.",
    #accept_multiple_files=True
    )

docs=None

if uploaded_file is not None:
    st.write("File uploaded successfully")
    st.write(uploaded_file)
    file_details = {"filename": uploaded_file.name, "content_type": uploaded_file.type}
    # create a temporary folder
    with tempfile.TemporaryDirectory() as temp_dir:
        #Save the uploaded file to the temporary folder
        file_path = temp_dir + '/' + uploaded_file.name
        with open(file_path, 'wb') as f:
            f.write(uploaded_file.getbuffer())
            docs = pdf_to_text(file_path, file_details)

st.write(docs)