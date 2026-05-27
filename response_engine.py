SEVERITY_MAP = {
    "memory_error": 9,
    "network_error": 8,
    "dependency_error": 7,
    "runtime_error": 6,
    "authentication_error": 7,
    "authorization_error": 8,
    "timeout_error": 6,
    "validation_error": 3,
    "syntax_error": 1,
    "math_error": 2,
    "unknown": 5
}


def calculate_severity(category: str) -> int:
    """
    Convert error category into a severity score (0–10).
    Higher = more critical system impact.
    """
    category = (category or "").lower().strip()
    return SEVERITY_MAP.get(category, 5)


def estimate_debug_time(category: str, severity: int) -> int:
    """
    Estimate debugging/fix time in minutes based on category + severity.
    """
    category = (category or "").lower().strip()

    base_time_map = {
        "syntax_error": 10,
        "math_error": 15,
        "validation_error": 20,
        "runtime_error": 45,
        "timeout_error": 60,
        "dependency_error": 90,
        "network_error": 75,
        "memory_error": 120,
        "authentication_error": 60,
        "authorization_error": 80,
        "unknown": 60
    }

    base_time = base_time_map.get(category, 60)

    severity_multiplier = 0.5 + (severity / 10)

    estimated_time = int(base_time * severity_multiplier)

    return max(5, estimated_time)


def get_fix_suggestion(category: str, error_type: str = None) -> str:
    """
    Return a simple human-readable fix suggestion based on category
    and optional parser error type.
    """

    category = (category or "").lower().strip()
    error_type = (error_type or "").lower().strip()

    suggestions = {
        "memory_error": "Check for memory leaks, optimize data structures, or increase server memory limits.",
        "network_error": "Verify network connectivity, retry logic, and external service availability.",
        "dependency_error": "Check installed packages, version conflicts, and reinstall dependencies.",
        "runtime_error": "Inspect stack trace and handle edge cases or invalid inputs.",
        "authentication_error": "Verify API keys, tokens, and authentication configuration.",
        "authorization_error": "Check user permissions and access control rules.",
        "timeout_error": "Optimize slow operations or increase timeout limits.",
        "validation_error": "Validate input data formats and enforce stricter schema rules.",
        "syntax_error": "Fix code syntax issues or parsing errors in input.",
        "math_error": "Check for invalid mathematical operations like division by zero.",
        "unknown": "Inspect logs carefully and add more detailed error tracking."
    }

    base_suggestion = suggestions.get(
        category,
        "Review logs and debug step-by-step to identify root cause."
    )

    # Optional refinement using parser error_type
    if error_type:
        if "zero" in error_type:
            base_suggestion += " Specifically check for division by zero cases."
        elif "null" in error_type or "none" in error_type:
            base_suggestion += " Look for null/None value handling issues."
        elif "index" in error_type:
            base_suggestion += " Check array/list index boundaries."

    return base_suggestion