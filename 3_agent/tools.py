import os
import glob
import subprocess


def get_current_directory():
    return os.getcwd()


def list_directory(path="."):
    try:
        return {
            "path": os.path.abspath(path),
            "contents": os.listdir(path)
        }
    except Exception as e:
        return {"error": str(e)}


def find_files(pattern, directory="."):
    try:
        matches = glob.glob(
            os.path.join(directory, "**", pattern),
            recursive=True
        )

        return {
            "count": len(matches),
            "files": matches[:500]
        }

    except Exception as e:
        return {"error": str(e)}


def read_file(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        return {"error": str(e)}


def write_file(path, content):
    try:
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)

        return {
            "success": True,
            "path": path
        }

    except Exception as e:
        return {"error": str(e)}


def append_file(path, content):
    try:
        with open(path, "a", encoding="utf-8") as f:
            f.write(content)

        return {
            "success": True,
            "path": path
        }

    except Exception as e:
        return {"error": str(e)}


def create_directory(path):
    try:
        os.makedirs(path, exist_ok=True)

        return {
            "success": True,
            "path": path
        }

    except Exception as e:
        return {"error": str(e)}


def search_text(text, directory="."):
    results = []

    try:

        for root, _, files in os.walk(directory):

            for file in files:

                path = os.path.join(root, file)

                try:

                    with open(
                        path,
                        "r",
                        encoding="utf-8"
                    ) as f:

                        content = f.read()

                        if text in content:

                            results.append(path)

                except:
                    pass

        return {
            "count": len(results),
            "files": results
        }

    except Exception as e:
        return {"error": str(e)}


def run_command(command):

    try:

        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            timeout=30
        )

        return {
            "returncode": result.returncode,
            "stdout": result.stdout,
            "stderr": result.stderr
        }

    except Exception as e:
        return {"error": str(e)}


TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "get_current_directory",
            "description": "Get current working directory",
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
            "description": "Find files matching a pattern such as *.py or *.txt",
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
            "description": "Read a text file",
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
    },
    {
        "type": "function",
        "function": {
            "name": "write_file",
            "description": "Create or overwrite a file",
            "parameters": {
                "type": "object",
                "properties": {
                    "path": {
                        "type": "string"
                    },
                    "content": {
                        "type": "string"
                    }
                },
                "required": ["path", "content"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "append_file",
            "description": "Append text to a file",
            "parameters": {
                "type": "object",
                "properties": {
                    "path": {
                        "type": "string"
                    },
                    "content": {
                        "type": "string"
                    }
                },
                "required": ["path", "content"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "create_directory",
            "description": "Create a directory",
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
    },
    {
        "type": "function",
        "function": {
            "name": "search_text",
            "description": "Search text across files",
            "parameters": {
                "type": "object",
                "properties": {
                    "text": {
                        "type": "string"
                    },
                    "directory": {
                        "type": "string"
                    }
                },
                "required": ["text"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "run_command",
            "description": "Execute shell commands",
            "parameters": {
                "type": "object",
                "properties": {
                    "command": {
                        "type": "string"
                    }
                },
                "required": ["command"]
            }
        }
    }
]


FUNCTION_MAP = {
    "get_current_directory": get_current_directory,
    "list_directory": list_directory,
    "find_files": find_files,
    "read_file": read_file,
    "write_file": write_file,
    "append_file": append_file,
    "create_directory": create_directory,
    "search_text": search_text,
    "run_command": run_command
}