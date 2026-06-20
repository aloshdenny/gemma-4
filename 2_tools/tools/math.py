def add_numbers(a: float, b: float):
    return a + b


def multiply_numbers(a: float, b: float):
    return a * b


def divide_numbers(a: float, b: float):
    return a / b

TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "add_numbers",
            "description": "Add numbers together",
            "parameters": {
                "type": "object",
                "properties": {
                    "a": {"type": "number"},
                    "b": {"type": "number"}
                },
                "required": ["a", "b"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "multiply_numbers",
            "description": "Multiply two numbers together",
            "parameters": {
                "type": "object",
                "properties": {
                    "a": {"type": "number"},
                    "b": {"type": "number"}
                },
                "required": ["a", "b"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "divide_numbers",
            "description": "Divide two numbers together",
            "parameters": {
                "type": "object",
                "properties": {
                    "a": {"type": "number"},
                    "b": {"type": "number"}
                },
                "required": ["a", "b"]
            }
        }
    }
]

FUNCTION_MAP = {
    "add_numbers": add_numbers,
    "multiply_numbers": multiply_numbers,
    "divide_numbers": divide_numbers
}