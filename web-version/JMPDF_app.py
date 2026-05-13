import streamlit as st
import pypdf
from io import BytesIO

def Just_Merge_PDF(PDFs_Order,PDFs):
    merger = pypdf.PdfWriter()
    for pdf in PDFs_Order:
        merger.append(PDFs[pdf])
    pdf_buffer = BytesIO()
    merger.write(pdf_buffer)
    pdf_buffer.seek(0)
    return pdf_buffer

st.title("Just Merge PDF❤️")


uploaded_files = st.file_uploader(
    "Upload PDFs", accept_multiple_files="directory", type=["pdf"]
)

if uploaded_files:
    file_list =[]
    file_dict = {}
    for file in uploaded_files:
        file_list.append(file.name)
        file_dict[file.name] = file
    option = st.selectbox('Soted',['Sorted', 'Unsorted', 'Reverse','ReverseSorted'])
    if option == 'Sorted':
        file_list = sorted(file_list)
        table = st.table({'Files':file_list})
        if st.button("Merge PDF"):
            pdf_file = Just_Merge_PDF(file_list,file_dict)

            st.download_button(
                label="Download PDF",
                data=pdf_file,
                file_name="merged.pdf",
                mime="application/pdf"
            )
    if option == 'Unsorted':
        # file_list = sorted(file_list)
        table = st.table({'Files':file_list})
        if st.button("Merge PDF"):
            pdf_file = Just_Merge_PDF(file_list,file_dict)

            st.download_button(
                label="Download PDF",
                data=pdf_file,
                file_name="merged.pdf",
                mime="application/pdf"
            )
    if option == 'Reverse':
        file_list = reversed(file_list)
        table = st.table({'Files':file_list})
        if st.button("Merge PDF"):
            pdf_file = Just_Merge_PDF(file_list,file_dict)

            st.download_button(
                label="Download PDF",
                data=pdf_file,
                file_name="merged.pdf",
                mime="application/pdf"
            )
    if option == 'ReverseSorted':
        file_list = reversed(sorted(file_list))
        table = st.table({'Files':file_list})
        if st.button("Merge PDF"):
            pdf_file = Just_Merge_PDF(file_list,file_dict)

            st.download_button(
                label="Download PDF",
                data=pdf_file,
                file_name="merged.pdf",
                mime="application/pdf"
            )
