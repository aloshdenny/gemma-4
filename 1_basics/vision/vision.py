from ollama import chat

response = chat(
    model='gemma4:e2b',
    messages=[
        {
            'role': 'user',
            'content': 'What is the output',
            'images': ['1_basics/vision/python.png']
        }
    ],
    think=False
)

print(response['message']['content'])