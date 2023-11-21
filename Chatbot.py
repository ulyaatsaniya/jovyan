import streamlit as st
import google.generativeai as palm

# Set the background colors
st.markdown(
    """
    <style>
    body {
        background-color: #f0f0f0; /* Light gray background */
        margin: 0; /* Remove default margin for body */
        padding: 0; /* Remove default padding for body */
    }
    .st-bw {
        background-color: #eeeeee; /* White background for widgets */
    }
    .st-cq {
        background-color: #cccccc; /* Gray background for chat input */
        border-radius: 10px; /* Add rounded corners */
        padding: 8px 12px; /* Add padding for input text */
        color: black; /* Set text color */
    }

    .st-cx {
        background-color: white; /* White background for chat messages */
    }
    .sidebar .block-container {
        background-color: #f0f0f0; /* Light gray background for sidebar */
        border-radius: 10px; /* Add rounded corners */
        padding: 10px; /* Add some padding for spacing */
    }
    .top-right-image-container {
        position: fixed;
        top: 30px;
        right: 0;
        padding: 20px;
        background-color: white; /* White background for image container */
        border-radius: 0 0 0 10px; /* Add rounded corners to bottom left */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title
st.title("💬AI Marketing QnA")

# Top right corner image container
st.markdown(
    "<div class='top-right-image-container'>"
    "<img src='https://imgur.com/sxSdMX2.png' width='60'>"
    "<img src='https://imgur.com/sxSdMX2.png' width='60'>"
    "<img src='https://imgur.com/22eWfGo.png' width='80'>"
    "</div>",
    unsafe_allow_html=True
)

# Create functions to open each social media app
def open_app(app_name):
    st.experimental_set_query_params(page=app_name)


# Sidebar
with st.sidebar:

    palm_api_key = st.text_input('PaLM API Key',
                                 key='palm_api_key',
                                 help="Don't have API Key? [Join the waitlist](https://developers.generativeai.google/products/palm) or Generate using your Google Cloud project"
                                 )

# Set up the layout
col1, col2 = st.columns([3, 1])  # Adjust column widths as needed

# Chat interface in the left column
with col1:
    # Initialize the session_state if it doesn't exist
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "How can I help you?"}]
        st.session_state.prev_prompt = False
    
    # Display existing chat messages
    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])
    
    # Get user input
    prompt = st.text_input("You:", "")

    # Check if the user pressed "Enter"
    if st.session_state.prev_prompt and prompt == "":
        # User pressed "Enter", clear the text input
        st.session_state.prev_prompt = False
        prompt = ""
    
    # Process user input and interact with the chatbot
    if prompt:
        if not palm_api_key:
            st.info("Please add your PaLM API key to continue.")
        else:
            try:
                palm.configure(api_key=palm_api_key)
            except Exception as e:
                st.info("Please pass a valid API key")
            st.session_state.messages.append({"role": "user", "content": prompt})
            st.chat_message("user").write(prompt)
            
            # Create a message for the PaLM API
            user_messages = [{"role": "system", "content": "You are a marketing consultant."}]
            user_messages.extend(st.session_state.messages)
            
            response = palm.chat(messages=prompt)
            msg = {"role": "assistant", "content": response.last}
            st.session_state.messages.append(msg)
            st.chat_message("assistant").write(msg["content"])

            # Clear the text input after sending a message
            st.session_state.prev_prompt = True
            prompt = ""  # Clear the prompt
