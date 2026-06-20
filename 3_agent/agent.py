from openai import OpenAI
import json
from tools import *
from prompt import *

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"
)

MODEL = "gemma4:e4b"

def run_chat(history):
    while True:
        response = client.chat.completions.create(
            model=MODEL,
            messages=history,
            tools=TOOLS,
            temperature=0,
            extra_body={
            "think": False
            }
        )

        assistant = response.choices[0].message

        # No tool calls → this is the final verdict
        if not assistant.tool_calls:
            return assistant.content

        # Append assistant turn (once, before iterating tool calls)
        history.append({
            "role": "assistant",
            "content": assistant.content,
            "tool_calls": assistant.tool_calls
        })

        # Execute each tool and append its result to history
        for tool_call in assistant.tool_calls:
            tool_name = tool_call.function.name
            args = json.loads(tool_call.function.arguments)

            print(f"\n[TOOL] {tool_name}")
            print("ARGS:", args)

            result = FUNCTION_MAP[tool_name](**args)

            print("RESULT:", result)

            history.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": json.dumps(result)
            })

        # Loop back → model now sees tool results and produces verdict

history = [
    {
        "role": "system",
        "content": PROMPT
    }
]

while True:

    query = input("\nYou: ")

    if query.lower() in ["exit", "quit"]:
        break

    history.append(
        {
            "role": "user",
            "content": query
        }
    )

    answer = run_chat(history)

    history.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    print("\nAssistant:", answer)