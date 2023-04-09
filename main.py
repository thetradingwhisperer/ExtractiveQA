import streamlit as st
from haystack.document_stores import InMemoryDocumentStore
from utils import save_and_parse_file, qa_pipeline


import logging
logging.basicConfig(format="%(levelname)s - %(name)s -  %(message)s", level=logging.WARNING)
logging.getLogger("haystack").setLevel(logging.INFO)


# Create a DocumentStore
document_store = InMemoryDocumentStore()


def clear_submit():
    st.session_state["submit"] = False

# Upload file
uploaded_file = st.file_uploader(
    "Upload a pdf, docx, txt or csv file",
    type = ['pdf', 'docx', 'txt', 'csv'],
    help="Upload a pdf, docx, txt or csv file - scanned documents are not supported yet.",
    on_change=clear_submit,
    #accept_multiple_files=True
    )

doc=None

if uploaded_file is not None:
    st.write("File uploaded successfully")
    # Parse file to doc
    doc = save_and_parse_file(uploaded_file)
    # Add docs to document store
    document_store.write_documents(doc)


# User is give an inout box to ask a question
question = st.text_input("Ask a question",
                         placeholder="Ask a question about your document?")
#Button to submit the question
button = st.button("Submit")

if button or st.session_state.get("submit"):
    if question is not None:
        st.session_state["submit"] = True
        # Get answers from pipeline
        pipe = qa_pipeline(document_store)
        results = pipe.run(query=question, 
                           params={"Retriever": {"top_k": 3}, "Reader": {"top_k": 2}})
    
    st.markdown("### Answers")
    st.write(results["answers"])
    answer_1 = results["answers"][0]
    answer_2 = results["answers"][1]
    st.markdown(f" 1st answer is: **{answer_1.answer}**")
    st.markdown(f" Context: **{answer_1.context}**")
    st.markdown(f" Source name is **{answer_1.meta['filename']}**")
    
    st.divider()
    
    st.markdown(f" 2nd answer is: **{answer_2.answer}**")
    st.markdown(f" Context: **{answer_2.context}**")
    st.markdown(f" Source name is **{answer_2.meta['filename']}**")
    st.session_state["submit"] = False
