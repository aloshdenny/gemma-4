from ollama import chat

response = chat(
    model='gemma4:e2b',
    messages=[
        {
            'role': 'user',
            'content': 'Compare these images',
            'images': [
                '1_basics/vision/husky.png',
                '1_basics/vision/german.png'
            ]
        }
    ],
    think=False
)

print(response['message']['content'])