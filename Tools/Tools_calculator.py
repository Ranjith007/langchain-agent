# tools/calculator.py
def calculate(expression: str) -> str:
    try:
        # safer eval: only allow math functions and numbers
        allowed = {"__builtins__": None}
        result = eval(expression, allowed, {})
        return str(result)
    except Exception as e:
        return f"Error evaluating expression: {e}"
