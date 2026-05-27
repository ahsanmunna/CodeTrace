training_examples = [

    # =========================
    # RUNTIME ERRORS
    # =========================

    {
        "text": "ZeroDivisionError: division by zero",
        "label": "runtime_error"
    },
    {
        "text": "NullPointerException at Main.java:42",
        "label": "runtime_error"
    },
    {
        "text": "IndexError: list index out of range",
        "label": "runtime_error"
    },
    {
        "text": "TypeError: unsupported operand type(s) for +: 'int' and 'str'",
        "label": "runtime_error"
    },
    {
        "text": "ValueError: invalid literal for int() with base 10: 'hello'",
        "label": "runtime_error"
    },
    {
        "text": "Segmentation fault (core dumped)",
        "label": "runtime_error"
    },
    {
        "text": "AttributeError: 'NoneType' object has no attribute 'append'",
        "label": "runtime_error"
    },
    {
        "text": "java.lang.ArrayIndexOutOfBoundsException: Index 5 out of bounds",
        "label": "runtime_error"
    },
    {
        "text": "RuntimeError: coroutine raised StopIteration",
        "label": "runtime_error"
    },
    {
        "text": "Fatal error: Uncaught Exception: DivisionByZeroError",
        "label": "runtime_error"
    },

    # =========================
    # SYNTAX ERRORS
    # =========================

    {
        "text": "SyntaxError: invalid syntax",
        "label": "syntax_error"
    },
    {
        "text": "SyntaxError: unexpected EOF while parsing",
        "label": "syntax_error"
    },
    {
        "text": "Unexpected token ';' in JSON at position 24",
        "label": "syntax_error"
    },
    {
        "text": "IndentationError: expected an indented block",
        "label": "syntax_error"
    },
    {
        "text": "SyntaxError: missing ')' after argument list",
        "label": "syntax_error"
    },
    {
        "text": "ParserError: unexpected token '}'",
        "label": "syntax_error"
    },
    {
        "text": "java: ';' expected",
        "label": "syntax_error"
    },
    {
        "text": "XMLSyntaxError: opening and ending tag mismatch",
        "label": "syntax_error"
    },
    {
        "text": "SyntaxError: unterminated string literal",
        "label": "syntax_error"
    },
    {
        "text": "bash: syntax error near unexpected token `fi'",
        "label": "syntax_error"
    },

    # =========================
    # DEPENDENCY ERRORS
    # =========================

    {
        "text": "ModuleNotFoundError: No module named 'numpy'",
        "label": "dependency_error"
    },
    {
        "text": "ImportError: cannot import name 'Flask'",
        "label": "dependency_error"
    },
    {
        "text": "java.lang.ClassNotFoundException: org.postgresql.Driver",
        "label": "dependency_error"
    },
    {
        "text": "npm ERR! Cannot find module 'express'",
        "label": "dependency_error"
    },
    {
        "text": "PackageNotFoundError: package 'requests' is not installed",
        "label": "dependency_error"
    },
    {
        "text": "pip._internal.exceptions.DistributionNotFound",
        "label": "dependency_error"
    },
    {
        "text": "Error: Cannot resolve dependency 'react-dom'",
        "label": "dependency_error"
    },
    {
        "text": "DLL load failed while importing cv2",
        "label": "dependency_error"
    },
    {
        "text": "NoClassDefFoundError: com/google/gson/Gson",
        "label": "dependency_error"
    },
    {
        "text": "Gem::LoadError: Could not find 'rails' gem",
        "label": "dependency_error"
    },

    # =========================
    # MEMORY ERRORS
    # =========================

    {
        "text": "MemoryError: unable to allocate 2.0 GiB",
        "label": "memory_error"
    },
    {
        "text": "java.lang.OutOfMemoryError: Java heap space",
        "label": "memory_error"
    },
    {
        "text": "CUDA out of memory. Tried to allocate 256 MiB",
        "label": "memory_error"
    },
    {
        "text": "Fatal Python error: Cannot recover from stack overflow",
        "label": "memory_error"
    },
    {
        "text": "std::bad_alloc",
        "label": "memory_error"
    },
    {
        "text": "OutOfMemoryException: insufficient memory to continue",
        "label": "memory_error"
    },
    {
        "text": "Killed process 2451 (python) total-vm exceeded limit",
        "label": "memory_error"
    },
    {
        "text": "Tensor allocation failed due to insufficient memory",
        "label": "memory_error"
    },
    {
        "text": "malloc(): memory corruption",
        "label": "memory_error"
    },
    {
        "text": "RuntimeError: DataLoader worker ran out of shared memory",
        "label": "memory_error"
    },

    # =========================
    # NETWORK ERRORS
    # =========================

    {
        "text": "ConnectionRefusedError: [Errno 111] Connection refused",
        "label": "network_error"
    },
    {
        "text": "TimeoutError: request timed out after 30 seconds",
        "label": "network_error"
    },
    {
        "text": "requests.exceptions.ConnectionError: Failed to establish a new connection",
        "label": "network_error"
    },
    {
        "text": "socket.gaierror: [Errno -2] Name or service not known",
        "label": "network_error"
    },
    {
        "text": "HTTPError: 504 Gateway Timeout",
        "label": "network_error"
    },
    {
        "text": "NetworkError: failed to fetch resource",
        "label": "network_error"
    },
    {
        "text": "SSH connection failed: Connection timed out",
        "label": "network_error"
    },
    {
        "text": "urllib3.exceptions.MaxRetryError",
        "label": "network_error"
    },
    {
        "text": "BrokenPipeError: [Errno 32] Broken pipe",
        "label": "network_error"
    },
    {
        "text": "WebSocket connection closed unexpectedly",
        "label": "network_error"
    }

]