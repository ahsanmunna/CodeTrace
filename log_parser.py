import re
import json


def parse_python(traceback_text):

    result = {
        "error_type": None,
        "message": None,
        "file": None,
        "line": None,
        "code": None
    }

    file_match = re.search(
        r'File "(.+)", line (\d+)',
        traceback_text
    )

    error_match = re.search(
        r'(\w+Error): (.+)',
        traceback_text
    )

    code_match = re.search(
        r'line \d+\n\s+(.*)',
        traceback_text
    )

    if file_match:
        result["file"] = file_match.group(1)
        result["line"] = int(file_match.group(2))

    if error_match:
        result["error_type"] = error_match.group(1)
        result["message"] = error_match.group(2)

    if code_match:
        result["code"] = code_match.group(1).strip()

    return result


def parse_java(traceback_text):

    result = {
        "error_type": None,
        "message": None,
        "method": None,
        "file": None,
        "line": None
    }

    stack_match = re.search(
        r'at\s+([\w.$]+)\(([\w.$]+):(\d+)\)',
        traceback_text
    )

    error_match = re.search(
        r'([\w.]+Exception)(?:: (.+))?',
        traceback_text
    )

    if stack_match:
        result["method"] = stack_match.group(1)
        result["file"] = stack_match.group(2)
        result["line"] = int(stack_match.group(3))

    if error_match:
        result["error_type"] = error_match.group(1).split(".")[-1]
        result["message"] = error_match.group(2)

    return result


def parse_node(traceback_text):

    result = {
        "error_type": None,
        "message": None,
        "file": None,
        "line": None
    }

    file_match = re.search(
        r'/([^/]+):(\d+)$',
        traceback_text,
        re.MULTILINE
    )

    error_match = re.search(
        r'(\w+Error): (.+)',
        traceback_text
    )

    if file_match:
        result["file"] = file_match.group(1)
        result["line"] = int(file_match.group(2))

    if error_match:
        result["error_type"] = error_match.group(1)
        result["message"] = error_match.group(2)

    return result


def parse_log(traceback_text):

    if "Traceback" in traceback_text:
        return parse_python(traceback_text)

    elif "Exception in thread" in traceback_text:
        return parse_java(traceback_text)

    elif ".js" in traceback_text or "at Object.<anonymous>" in traceback_text:
        return parse_node(traceback_text)

    else:
        return {
            "error": "Unknown log format"
        }


# Example usage

python_trace = """
Traceback (most recent call last):
  File "main.py", line 5
    x + "hello"
TypeError: unsupported operand type(s) for +: 'int' and 'str'
"""

java_trace = """
Exception in thread "main" java.lang.NullPointerException
	at com.example.Main.getUser(Main.java:42)
	at com.example.Main.main(Main.java:10)
"""

node_trace = """
/home/user/app.js:15
    throw new Error('Connection failed');
TypeError: Cannot read property 'name' of undefined
    at Object.<anonymous> (/home/user/app.js:15:11)
"""

print(json.dumps(parse_log(python_trace), indent=2))
print(json.dumps(parse_log(java_trace), indent=2))
print(json.dumps(parse_log(node_trace), indent=2))