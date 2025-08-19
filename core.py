import os
import openai
from mem0 import MemoryClient
from dotenv import load_dotenv
from textblob import TextBlob
import whisper

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
memory = MemoryClient(api_key=os.getenv("MEM0_API_KEY"))
whisper_model = whisper.load_model("base")

class MemoryAssistant:
    def __init__(self, user_id="default_user"):
        self.user_id = user_id

    def ask(self, query: str) -> str:
        try:
            # Retrieve memory
            results = memory.search(query=query, user_id=self.user_id, limit=3)
            
            # Handle different return formats from memory.search()
            if isinstance(results, dict) and "results" in results:
                # If results is a dict with "results" key
                memory_entries = results["results"]
            elif isinstance(results, list):
                # If results is directly a list
                memory_entries = results
            else:
                # Fallback for unexpected format
                memory_entries = []
            
            # Extract memory strings safely
            mem_str = ""
            if memory_entries:
                memory_texts = []
                for entry in memory_entries:
                    if isinstance(entry, dict):
                        # Try different possible keys for memory content
                        memory_text = entry.get('memory') or entry.get('text') or entry.get('content') or str(entry)
                        memory_texts.append(f"- {memory_text}")
                    else:
                        memory_texts.append(f"- {str(entry)}")
                mem_str = "\n".join(memory_texts)
            else:
                mem_str = "- No relevant memories found"

            prompt = (
                "You are a thoughtful AI assistant.\n"
                f"Relevant memories:\n{mem_str}\n"
                f"User: {query}\n"
                "Assistant:"
            )

            resp = openai.chat.completions.create(model="gpt-4", messages=[{"role":"user","content":prompt}])
            answer = resp.choices[0].message.content

            # Save memory
            memory.add(messages=[{"role":"user","content":query}, {"role":"assistant","content":answer}], user_id=self.user_id)
            return answer
            
        except Exception as e:
            # Fallback response if memory operations fail
            print(f"Memory operation failed: {e}")
            
            # Generate response without memory context
            prompt = f"You are a thoughtful AI assistant.\nUser: {query}\nAssistant:"
            
            try:
                resp = openai.chat.completions.create(
                    model="gpt-4", 
                    messages=[{"role": "user", "content": prompt}]
                )
                answer = resp.choices[0].message.content
                return answer
            except Exception as openai_error:
                return f"I apologize, but I'm experiencing technical difficulties. Error: {str(openai_error)}"

    def transcribe_audio(self, audio_data: bytes) -> str:
        try:
            # Transcribe audio to text using Whisper
            result = whisper_model.transcribe(audio_data)
            return result["text"]
        except Exception as e:
            print(f"Audio transcription failed: {e}")
            return "Sorry, I couldn't transcribe the audio."

    def analyze_sentiment(self, text: str) -> str:
        try:
            # Analyze sentiment using TextBlob
            blob = TextBlob(text)
            polarity = blob.sentiment.polarity
            if polarity > 0:
                return "Positive"
            elif polarity < 0:
                return "Negative"
            else:
                return "Neutral"
        except Exception as e:
            print(f"Sentiment analysis failed: {e}")
            return "Unknown"
