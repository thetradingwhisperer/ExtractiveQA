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
    
    # Add docs to document store
    document_store.write_documents(docs)

# Create retriever
retriever = TfidfRetriever(document_store=document_store)

# Create reader
reader = FARMReader(model_name_or_path="deepset/roberta-base-squad2", use_gpu=False)

# Create pipeline
pipe = ExtractiveQAPipeline(reader, retriever)


# User is give an inout box to ask a question
question = st.text_input("Ask a question",
    placeholder="Ask a question about your document?")
if question is not None:
    # Get answers from pipeline
    results = pipe.run(query=question, top_k_retriever=10, top_k_reader=5)
    st.write(results)

