import streamlit as st



def eqa_sidebar():
  
    with st.sidebar:
        #st.image("NOC logo.PNG", width=150)
        st.markdown("#")
        st.markdown("#")

        st.markdown(
            "## How to use\n"
            "1. Upload your pdf or text document :page_with_curl:\n"  # noqa: E501
            "2. Ask a question about the document💬\n"
        )

        st.markdown("---")
        st.markdown("# About")
        st.markdown(
            "📖This page allows you to ask questions about your "
            "documents and get answers directly from extracts of your document with the source (document name). "
        )
        st.markdown(
            "This tool is a work in progress. "
            "If you have any questions or feedback, please reach out to Digital team in DBS"
        )
        st.markdown("---")
        st.markdown("Made by Digital")
        

def genqa_sidebar():
  
    with st.sidebar:
        st.markdown("#")
        st.markdown("#")

        st.markdown(
            "## How to use\n"
            "1. Upload your pdf or text document :page_with_curl:\n"  # noqa: E501
            "2. Ask a question about the document💬\n"
        )

        st.markdown("---")
        st.markdown("# About")
        st.markdown(
            "📖This page allows you to ask questions about your "
            "documents and get answers in a generative manner. A large language model gives you the answers from one or many parts of your document. It also provides the source. "
        )
        st.markdown(
            "This tool is a work in progress. "
            "If you have any questions or feedback, please reach out to Digital team in DBS"
        )
        st.markdown("---")
        st.markdown("Made by Digital")