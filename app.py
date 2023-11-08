import streamlit as st
from streamlit_image_comparison import image_comparison
from embedchain import App
import os
import sys



IMAGE_TO_URL = {

    "sample_image_1": "./img/c.jpg",

    "sample_image_2": "./img/d.jpg",

    # "sample_image_1": "https://user-images.githubusercontent.com/34196005/143309873-c0c1f31c-c42e-4a36-834e-da0a2336bb19.jpg",

    # "sample_image_2": "https://user-images.githubusercontent.com/34196005/143309873-c0c1f31c-c42e-4a36-834e-da0a2336bb19.jpg",

}





st.set_page_config(

    page_title="Streamlit Image Comparison",

    page_icon="🔥",

    layout="centered",

    initial_sidebar_state="auto",

)



st.markdown(

    """

    <h2 style='text-align: center'>

     Image Comparison Demo

    </h2>

    """,

    unsafe_allow_html=True,

)

# st.markdown(

#     """

#     <p style='text-align: center'>

#     <br />

#     Follow me for more! <a href='https://twitter.com/fcakyon' target='_blank'> <img src="https://img.icons8.com/color/48/000000/twitter--v1.png" height="30"></a><a href='https://github.com/fcakyon' target='_blank'><img src="https://img.icons8.com/fluency/48/000000/github.png" height="27"></a><a href='https://www.linkedin.com/in/fcakyon/' target='_blank'><img src="https://img.icons8.com/fluency/48/000000/linkedin.png" height="30"></a> <a href='https://fcakyon.medium.com/' target='_blank'><img src="https://img.icons8.com/ios-filled/48/000000/medium-monogram.png" height="26"></a>

#     </p>

#     """,

#     unsafe_allow_html=True,

# )



st.write("##")



with st.form(key="Streamlit Image Comparison"):

    # image one inputs

    col1, col2 = st.columns([3, 1])

    with col1:

        img1_url = st.text_input("Image one URL:", value=IMAGE_TO_URL["sample_image_1"])

    with col2:

        img1_text = st.text_input("Image one text:", value="A")



    # image two inputs

    col1, col2 = st.columns([3, 1])

    with col1:

        img2_url = st.text_input("Image two URL:", value=IMAGE_TO_URL["sample_image_2"])

    with col2:

        img2_text = st.text_input("Image two text:", value="B")



    # continious parameters

    col1, col2 = st.columns([1, 1])

    with col1:

        starting_position = st.slider(

            "Starting position of the slider:", min_value=0, max_value=100, value=50

        )

    with col2:

        width = st.slider(

            "Component width:", min_value=400, max_value=1000, value=700, step=100

        )



    # boolean parameters

    col1, col2, col3, col4 = st.columns([1, 3, 3, 3])

    with col2:

        show_labels = st.checkbox("Show labels", value=True)

    with col3:

        make_responsive = st.checkbox("Make responsive", value=True)

    with col4:

        in_memory = st.checkbox("In memory", value=True)



    # centered submit button

    col1, col2, col3 = st.columns([6, 4, 6])

    with col2:

        submit = st.form_submit_button("Update Render 🔥")



static_component = image_comparison(

    img1=img1_url,

    img2=img2_url,

    label1=img1_text,

    label2=img2_text,

    width=width,

    starting_position=starting_position,

    show_labels=show_labels,

    make_responsive=make_responsive,

    in_memory=in_memory,

)




# if submit:
with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
    "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
    "[View the source code](https://github.com/chan4lk/hello-embedchain/blob/main/app.py)"
    "[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/chan4lk/hello-embedchain?quickstart=1)"
 
st.title("💬 Chatbot")
 
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]
 
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])
 
if prompt := st.chat_input():
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()
 
    os.environ["OPENAI_API_KEY"]  = openai_api_key
 
    bistec_bot = App()
 
    DATA_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), 'img'))
    files = [f for f in os.listdir(DATA_DIR)]
    for file in files:
        print(file)
        bistec_bot.add(os.path.join(DATA_DIR, file), data_type="images")
 
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
 
    response = bistec_bot.query(prompt)
    st.session_state.messages.append({"role": "assistant", "content": response})
    st.chat_message("assistant").write(response)