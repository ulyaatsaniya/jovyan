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
st.title("Instagram Marketing QnA")

# Top right corner image container
st.markdown(
    "<div class='top-right-image-container'>"
    "<img src='https://imgur.com/sxSdMX2.png' width='60'>"
    "<img src='https://imgur.com/22eWfGo.png' width='80'>"
    "</div>",
    unsafe_allow_html=True
)

# Sidebar
with st.sidebar:
    st.header("Social Media")
    # LinkedIn Post option
    st.markdown(
        "<div class='block-container'>"
        "<div style='display: flex; align-items: center;'>"
        "<img src='https://imgur.com/MZm2T4E.png' style='width:20px; margin-right: 10px;'>"
        "Linkedin Post"
        "</div>"
        "</div>",
        unsafe_allow_html=True
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
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.chat_message("user").write(prompt)
        
        # Chatbot response (you need to replace this with actual PaLM interaction)
        response = "Chatbot response goes here"
        
        msg = {"role": "assistant", "content": response}
        st.session_state.messages.append(msg)
        st.chat_message("assistant").write(msg["content"])

        # Clear the text input after sending a message
        st.session_state.prev_prompt = True
        prompt = ""  # Clear the prompt

# Display empty space in the right column
with col2:
    pass  # Add any content you want in the right column

# This line ensures that the app runs when you run the script
if __name__ == "__main__":
    st.set_page_config(page_title="LinkedIn Marketing QnA")
