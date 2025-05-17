import os

def validate_file_access(file_path):
    try:
        with open(file_path, 'r') as f:
            f.read(1)
        return True
    except FileNotFoundError:
        raise FileNotFoundError(f"File '{file_path}' does not exist.")
    except PermissionError:
        raise PermissionError(f"File '{file_path}' is not readable.")
    except Exception as e:
        raise IOError(f"An error occurred while trying to read '{file_path}': {e}")

def check_for_header(lines):
    if not lines:
        raise ValueError("File is empty; no header found.")
    
    header = lines[0].strip().split(",")
    if any(field == "" for field in header):
        raise ValueError("Header contains empty fields.")
    
    return header

def ensure_uniform_field_count(lines):
    if len(lines) <= 1:
        raise ValueError("No records found in the file; the file is empty or only contains a header.")
    
    header_len = len(lines[0].strip().split(","))
    
    for i, line in enumerate(lines[1:], start=2):
        fields = line.strip().split(",")
        if len(fields) == 0 or not any(field.strip() for field in fields):
            raise ValueError(f"Line {i} is blank or empty.")
        if len(fields) != header_len:
            raise ValueError(f"Line {i} does not match header field count: expected {header_len}, got {len(fields)}")
