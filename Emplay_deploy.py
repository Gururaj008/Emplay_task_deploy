import streamlit as st
from docx import Document
from docx2python import docx2python
from streamlit_option_menu import option_menu
import openai
import io
openai.api_key=st.secrets['auth_key']

def extract_text_from_word(docx_file):
    doc_result = docx2python(docx_file)
    return doc_result.body
    
def convert_lang(text, lang):
    msg = f"Translate the document to {lang} language."      

    messages = [
        {"role": "system", "content": "You are a language translator"},
        {"role": "user", "content": "Mandatorily stick to the following instructions while generation your response"},
        {"role": "user", "content": "1. Translate and all the words from english into the specified language"},
        {"role": "user", "content": "2. Dont skip the page numbers"},
        {"role": "user", "content": "2. There are some repeated sentences in the document as explained in the below example, translate and compulsarily retain them in the same format"},
        {"role": "user", "content": "For example"},
        {"role": "user", "content": "Employee Central (EC) Overview"},
        {"role": "user", "content": "for Internal SAP and Partner Use Only"},
        {"role": "user", "content": "Page _ of _ "},
        {"role": "user", "content": "3. Dont truncate your response, return all words until the end of the document"},
        {"role": "user", "content": msg},
        {"role": "assistant", "content": "Sure! Please provide me with the document."},
        {"role": "user", "content": str(text)}
        
    ]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k",
        messages=messages
    )

    review = response['choices'][0]['message']['content']
    return review

def identify_names(text):
    msg = f"Identify and replace the names in the document from native {country} names"
    messages = [
        {"role": "system", "content": "You are a helpful assistant, who is helping me with a NLP task"},
        {"role": "user", "content": msg},
        {"role": "assistant", "content": "Sure! Please provide me with the text"},
        {"role": "user", "content": str(text)}
    ]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k",
        messages=messages)
    names = response['choices'][0]['message']['content']
    return names

if __name__=="__main__":
    st.set_page_config(layout="wide")
    col101, col102, col103 = st.columns([40,200,40])
    with col102:
           st.markdown("""
                    <style>
                    @import url('https://fonts.googleapis.com/css2?family=Agdasima');
                    .custom-text { font-family: 'Agdasima', sans-serif; font-size: 40px;color:cyan }
                    </style>
                    <p class="custom-text">Emplay Assignment for Internship opportunity </p>
                    """, unsafe_allow_html=True)
    col104, col105, col106 = st.columns([90,200,90])
    with col105:
           st.markdown("""
                    <style>
                    @import url('https://fonts.googleapis.com/css2?family=Agdasima');
                    .custom-text-02 { font-family: 'Agdasima', sans-serif; font-size: 50px;color:#f4d03f }
                    </style>
                    <p class="custom-text-02">Demo Script Localization</p>
                    """, unsafe_allow_html=True)
    st.write('')
    st.write('')
    selected = option_menu(None, ["About the project","Using LLM","Developer contact details"], 
    icons=['pencil-square', 'dvd',  'file-person-fill'], menu_icon="cast", default_index=0, orientation="horizontal")
    st.write('')
    st.write('')
    if selected == 'About the project':
        st.subheader(':orange[About the project]')
        st.markdown('<div style="text-align: justify"> Welcome to the Localized Demo Script Generator app! This project aims to demonstrate the process of localizing a demo script by translating its content to a user-specified language and replacing names with those from a selected country and is based on a real-world scenario where sales representatives need to adapt their pitch scripts for different regions or locales.  </div>', unsafe_allow_html=True)
        st.write('')
        st.subheader(':orange[Steps involved ]')
        st.markdown('<div style="text-align: justify"> 1. You can upload a demo script in DOCX format using the file upload feature  </div>', unsafe_allow_html=True)
        st.write('')
        st.markdown('<div style="text-align: justify"> 2. Specify the language to which you wish to translate the script and select a country to use names from that specific country </div>', unsafe_allow_html=True)
        st.write('')
        st.markdown('<div style="text-align: justify"> 3. Make an API call in the background to ChatGPT-3.5 </div>', unsafe_allow_html=True)
        st.write('')
        st.markdown('<div style="text-align: justify"> 4. Using LLM perform language conversion and name replacement  </div>', unsafe_allow_html=True)
        st.write('')
        st.markdown('<div style="text-align: justify"> 5. Download the localized demo script with the content translated and names replaced according to your selections </div>', unsafe_allow_html=True)
        st.write('')
        st.write('')
        st.write('')
        st.markdown('<div style="text-align: justify"> Let us move to the "Using LLM" tab and perform the task..... </div>', unsafe_allow_html=True)
        
    if selected == "Using LLM":
        st.markdown("""
                    <style>
                    @import url('https://fonts.googleapis.com/css2?family=Agdasima');
                    .custom-text-10 { font-family: 'Agdasima', sans-serif; font-size: 30px;color:#f4d03f }
                    </style>
                    <p class="custom-text-10"> Instructions </p>
                    """, unsafe_allow_html=True)
        st.write('')
        st.write('')
        st.write('1. Upload a word document with .docx extension')
        st.write('2. Select the language to which you wish to convert the contents of the uploaded document')
        st.write('3. Select the country from which native names will be generated and replaced in the document uploaded')
        st.write('4. Hit the "Translate" followed by "Download" button to download the localized document')
        st.write('')
        st.write('')
        uploaded_file = st.file_uploader("Upload a Word document", type=["docx"])
        st.write('')
        st.write('')
        col107, col108 = st.columns([10,10])
        with col107:
              lang = st.selectbox('Select the language to which you want to convert the contents',
                             ('French','German','Spanish','Italian','Portugese','Japanese','Chinese','Korean'))
        with col108:
              country = st.selectbox('Select the country from which the names would be replaced ',
                             ('France','Germany','Spain','Italy','Portugal','Japan','China','South Korea'))
        if uploaded_file is not None:
            extracted_text = extract_text_from_word(uploaded_file)
            content_list = extracted_text[0][0][0]
            formatted_text = "\n\n".join(content_list)
            part1 = formatted_text[:(len(formatted_text)//5)]
            part2 = formatted_text[(len(formatted_text)//5):(len(formatted_text)*2//5)]
            part3 = formatted_text[(len(formatted_text)*2//5):(len(formatted_text)*3//5)]
            part4 = formatted_text[(len(formatted_text)*3//5):(len(formatted_text)*4//5)]
            part5 = formatted_text[(len(formatted_text)*4//5):]

            if st.button("Create .docx File",use_container_width=True):
                names1 = identify_names(part1)
                result1 = convert_lang(names1, lang)             
                names2 = identify_names(part2)
                result2 = convert_lang(names2, lang)
                names3 = identify_names(part3)
                result3 = convert_lang(names3, lang)
                names4 = identify_names(part4)
                result4 = convert_lang(names4, lang)
                names5 = identify_names(part5)
                result5 = convert_lang(names5, lang)
                final_result = result1 + result2 + result3 + result4 + result5
                doc = Document()
                doc.add_paragraph(final_result)
                doc_stream = io.BytesIO()
                doc.save(doc_stream)
                doc_stream.seek(0)
                doc_bytes = doc_stream.getvalue()
                st.download_button(
                    label="Download .docx file",
                    data=doc_bytes,
                    file_name="localized demo script.docx",
                    mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",use_container_width=True)
                

    if selected == 'Developer contact details':
        st.divider()
        col301, col302 = st.columns([10,20])
        with col301:
            st.markdown(":orange[email id:]")
            st.write('')
        with col302:
            st.markdown(":yellow[gururaj008@gmail.com]")
            st.write('')

        col301, col302 = st.columns([10,20])
        with col301:
            st.markdown(":orange[Personal webpage hosting Datascience projects :]")
            st.write('')
        with col302:
            st.markdown(":yellow[https://gururaj-hc-personal-webpage.streamlit.app/]")
            st.write('')

        col301, col302 = st.columns([10,20])
        with col301:
            st.markdown(":orange[LinkedIn profile :]")
            st.write('')
        with col302:
            st.markdown(":yellow[https://www.linkedin.com/in/gururaj-hc-data-science-enthusiast/]")
            st.write('')


        col301, col302 = st.columns([10,20])
        with col301:
            st.markdown(":orange[Github link:]")
            st.write('')
        with col302:
            st.markdown(":yellow[https://github.com/Gururaj008]")
            st.write('')
            
