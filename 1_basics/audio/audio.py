import whisper
from ollama import chat

AUDIO_FILE = "1_basics/audio/shashi.mp3"

whisper_model = whisper.load_model("tiny.en")

transcript = whisper_model.transcribe(
    AUDIO_FILE,
    fp16=False,
    language="en"
)

text = transcript["text"]

response = chat(
    model="gemma4:e2b",
    messages=[
        {
            "role": "system",
            "content": """
You are an expert audio understanding assistant.

Analyze the transcript and provide:

1. Summary
2. Key discussion points
3. Important people mentioned
4. Action items
5. Open questions
6. Overall sentiment
"""
        },
        {
            "role": "user",
            "content": text
        }
    ],
    think=False
)

print(response["message"]["content"])