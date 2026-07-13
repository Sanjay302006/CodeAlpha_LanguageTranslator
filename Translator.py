import streamlit as st
import urllib.parse
from deep_translator import GoogleTranslator

st.title("AI-Based Language Translator 🌍") #provide a title
st.write("Translate any text instantly using AI.")

col1, col2 = st.columns(2) #create two column layouts to select languages

with col1:
    source_lang = st.selectbox("Source Language", ["English", "Spanish", "French", "German"]) #select your language

with col2:
    target_lang = st.selectbox("Target Language", ["Spanish", "English", "French", "German"]) #select the language that you want the text to be translated into

text_to_translate = st.text_area("Enter the text to translate:", height=150) #enter your text here

#condition to be checked when the button is clicked
if st.button("Translate"):
    if text_to_translate:
        translator=GoogleTranslator(source=source_lang.lower(), target=target_lang.lower()) 
        translated_text = translator.translate(text_to_translate) #translates the given text
        st.success(translated_text)
        st.code(translated_text, language=None) #creates a copy button
    else:
        st.warning("Please enter some text to translate first.")