from haystack.nodes import TextConverter, PDFToTextConverter, DocxToTextConverter
from haystack.nodes import TfidfRetriever
from haystack.pipelines import Pipeline
from haystack.nodes import PromptTemplate, PromptNode
from haystack.nodes import PromptNode
from transformers import AutoModelForCausalLM
from transformers import AutoTokenizer
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
        try:
            doc = PDFToTextConverter(remove_numeric_tables=True,
                                        valid_languages=["en"],
                                        ).convert(filepath, meta=filedetails)
        except:
            st.error("Error converting pdf to text")
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

    model = AutoModelForCausalLM.from_pretrained(
    'mosaicml/mpt-7b-instruct',
    trust_remote_code=True)
    
    tokenizer = AutoTokenizer.from_pretrained("EleutherAI/gpt-neox-20b")
    retriever = TfidfRetriever(document_store=_documentstore)

    # Create a prompt node
    #question_answering_with_references = PromptTemplate("deepset/question-answering-with-references", output_parser=AnswerParser(reference_pattern=r"Document\[(\d+)\]"))
    prompt_node = PromptNode("mosaicml/mpt-7b-instruct", model_kwargs={"model":model, "tokenizer": tokenizer}, default_prompt_template="deepset/question-answering-with-references")
    
    pipe = Pipeline()
    pipe.add_node(component=retriever, name="retriever", inputs=["Query"])
    pipe.add_node(component=prompt_node, name="prompt_node", inputs=["retriever"])
    
    
    #prompt_node.prompt(prompt_template=question_answering_with_references, query="YOUR_QUERY", documents=_documentstore)
    
    return pipe