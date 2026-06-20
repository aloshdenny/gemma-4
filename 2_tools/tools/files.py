import os
import glob


def get_current_directory():
    return os.getcwd()


def list_directory(path="."):
    try:
        return os.listdir(path)
    except Exception as e:
        return str(e)


def find_files(pattern: str, directory="."):
    try:
        return glob.glob(
            os.path.join(directory, "**", pattern),
            recursive=True
        )
    except Exception as e:
        return str(e)


def read_file(path: str):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        return str(e)


TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "get_current_directory",
            "description": "Get the current working directory",
            "parameters": {
                "type": "object",
                "properties": {}
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "list_directory",
            "description": "List files and folders in a directory",
            "parameters": {
                "type": "object",
                "properties": {
                    "path": {
                        "type": "string"
                    }
                }
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "find_files",
            "description": "Find files matching a pattern such as *.py, *.txt, *.mov",
            "parameters": {
                "type": "object",
                "properties": {
                    "pattern": {
                        "type": "string"
                    },
                    "directory": {
                        "type": "string"
                    }
                },
                "required": ["pattern"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "read_file",
            "description": "Read the contents of a text file",
            "parameters": {
                "type": "object",
                "properties": {
                    "path": {
                        "type": "string"
                    }
                },
                "required": ["path"]
            }
        }
    }
]


FUNCTION_MAP = {
    "get_current_directory": get_current_directory,
    "list_directory": list_directory,
    "find_files": find_files,
    "read_file": read_file
}