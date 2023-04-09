from haystack.nodes import TextConverter, PDFToTextConverter, PDFToTextOCRConverter, DocxToTextConverter
from haystack.nodes import FARMReader, TfidfRetriever, TransformersReader
from haystack.pipelines import ExtractiveQAPipeline
import tempfile
import streamlit as st

# PDF to text parser
@st.cache_data
def parse_file_to_doc(filepath, filedetails, file_type=None):
    """
        Parse a file to a doc object
        input:
        filepath: path to file
        filedetails: dict with file details
        file_type: file type
        --------------------------------
        output:
        Document object
    """
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
@st.cache_data
def save_and_parse_file(uploaded_file):
    """ 
        Save and parse file to doc object
        uploaded_file: file uploaded by user
        the file is saved in a temporary folder
        the saved file is loaded and parsed to a doc object
    """
    file_details = {"filename": uploaded_file.name, "content_type": uploaded_file.type}
    # create a temporary folder
    with tempfile.TemporaryDirectory() as temp_dir:
        #Save the uploaded file to the temporary folder
        file_path = temp_dir + '/' + uploaded_file.name
        with open(file_path, 'wb') as f:
            f.write(uploaded_file.getbuffer())
            doc = parse_file_to_doc(file_path, 
                                    file_details,
                                    file_type=uploaded_file.name.split('.')[-1])
            return doc


@st.cache_resource
def qa_pipeline(_documentstore):
    """
        Create a pipeline for QA
    """
    # Create retriever
    retriever = TfidfRetriever(document_store=_documentstore)

    # Create reader
    reader = FARMReader(model_name_or_path="deepset/roberta-base-squad2", use_gpu=False)
    #reader = TransformersReader(model_name_or_path="distilbert-base-uncased-distilled-squad", tokenizer="distilbert-base-uncased", use_gpu=False)

    # Create pipeline
    pipe = ExtractiveQAPipeline(reader, retriever)
    #st.success("Pipeline created successfully")
    return pipe