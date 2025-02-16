import re
import sys

def check_select_statements(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    # Find all SELECT statements (case-insensitive)
    select_statements = re.findall(r'select\s+.*?\s+from', content, re.IGNORECASE)

    # Check if any SELECT statement is not in uppercase
    warnings = []
    for statement in select_statements:
        if statement != statement.upper():
            warnings.append(f"Warning: SELECT statement should be in uppercase: {statement}")

    return warnings

if __name__ == "__main__":
    import os

    for root, _, files in os.walk('.'):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                warnings = check_select_statements(file_path)
                if warnings:
                    print(f"File: {file_path}")
                    for warning in warnings:
                        print(warning)
                    sys.exit(1)  # Fail the pipeline