from ollama import chat

model = "gemma4:e2b"

with open("1_basics/chat/prompt.txt", "r", encoding="utf-8") as f:
    system_prompt = f.read()

messages = [
    {
        "role": "system",
        "content": system_prompt
    }
]

while True:
    user_input = input("\nYou: ")

    if user_input.lower() in ["exit", "quit"]:
        break

    messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    response = chat(
        model=model,
        messages=messages,
        think=False
    )

    answer = response["message"]["content"]

    messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    print(f"\nAssistant: {answer}")