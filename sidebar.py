import streamlit as st



def sidebar():
  
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
            "📖This allows you to ask questions about your "
            "documents and get fairly accurate answers answers with instant citations. "
        )
        st.markdown(
            "This tool is a work in progress. "
            "If you have any questions or feedback, please reach out to Digital team in DBS"
        )
        st.markdown("---")
        st.markdown("Made by Digital")