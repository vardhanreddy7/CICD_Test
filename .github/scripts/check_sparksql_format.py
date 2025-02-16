import re
import sys

def check_select_statements(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    spark_sql_pattern = r'spark\.sql\([\'"](.*?)[\'"]\)'
    spark_sql_matches = re.findall(spark_sql_pattern, content, re.DOTALL)

    # Check if any SELECT statement is not in uppercase
    warnings = []
    for sql_query in spark_sql_matches:
        # Check if the query contains a SELECT statement
        if 'select' in sql_query.lower():
            # Check if SELECT is in uppercase
            if not re.search(r'\bSELECT\b', sql_query):
                warnings.append(f"Warning: SELECT keyword should be in uppercase in query: {sql_query.strip()}")

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