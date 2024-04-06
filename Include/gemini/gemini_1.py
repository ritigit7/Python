import streamlit as st
import google.generativeai as genai

# Configure API key
genai.configure(api_key="AIzaSyD7xMD5WObXcSAk28F6TURWLtfZW8IA-gQ")

# Model and Safety Settings
generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

def get_ai_response(user_message):
  model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                               generation_config=generation_config,
                               safety_settings=safety_settings)
  convo = model.start_chat(history=[])
  convo.send_message(user_message)
  return convo.last.text

# Streamlit App
st.title("Chatbot with Generative AI")
st.subheader("Talk to the AI and see its response!")

user_input = st.text_input("Enter your message for the AI:")

if st.button("Ask AI"):
  response = get_ai_response(user_input)
  st.write(f"(AI)->: {response}")
