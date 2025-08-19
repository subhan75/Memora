import os
import streamlit as st
from core import MemoryAssistant
from dotenv import load_dotenv

load_dotenv()

def main():
    st.title("🧠 Memory-Powered Personal Assistant")
    
    # Sidebar for configuration
    user_id = st.sidebar.text_input("User ID", value="user123")
    
    # Initialize session state
    if "messages" not in st.session_state:
        st.session_state.messages = []

    try:
        assistant = MemoryAssistant(user_id=user_id)
    except Exception as e:
        st.error(f"Failed to initialize assistant: {e}")
        return

    # Display chat history
    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])

    # Text input
    if prompt := st.chat_input("You:"):
        # Add user message to session state
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.chat_message("user").write(prompt)
        
        # Generate and display assistant response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                try:
                    response = assistant.ask(prompt)
                    st.write(response)
                    # Add assistant message to session state
                    st.session_state.messages.append({"role": "assistant", "content": response})
                except Exception as e:
                    error_message = f"Error generating response: {str(e)}"
                    st.error(error_message)
                    st.session_state.messages.append({"role": "assistant", "content": error_message})

    # Voice Input
    audio = st.audio_input("Speak to Assistant", label_visibility="collapsed")
    if audio:
        try:
            with st.spinner("Transcribing audio..."):
                transcript = assistant.transcribe_audio(audio)
                st.session_state.messages.append({"role": "user", "content": transcript})
                st.chat_message("user").write(f"🎤 {transcript}")
            
            with st.chat_message("assistant"):
                with st.spinner("Thinking..."):
                    response = assistant.ask(transcript)
                    st.write(response)
                    st.session_state.messages.append({"role": "assistant", "content": response})
        except Exception as e:
            st.error(f"Error processing audio: {str(e)}")

    # Sentiment Analysis (only if there are messages)
    if st.session_state.messages:
        last_user_message = None
        for msg in reversed(st.session_state.messages):
            if msg["role"] == "user":
                last_user_message = msg["content"]
                break
        
        if last_user_message:
            try:
                sentiment = assistant.analyze_sentiment(last_user_message)
                st.sidebar.write(f"Sentiment: {sentiment}")
            except Exception as e:
                st.sidebar.write(f"Sentiment: Error analyzing")

if __name__ == "__main__":
    main()
