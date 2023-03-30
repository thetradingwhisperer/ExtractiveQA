import streamlit as st
from haystack.document_stores import InMemoryDocumentStore
from haystack.nodes import TfidfRetriever, FARMReader
from haystack.pipelines import ExtractiveQAPipeline


from utils import parse_file_to_doc, save_and_parse_file


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
    
    # Parse file to doc
    docs = save_and_parse_file(uploaded_file)

st.write(docs)