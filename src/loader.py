from validator import validate_file_access, check_for_header, ensure_uniform_field_count


def load_file(file_path): 
    if validate_file_access(file_path):
        with open(file_path, 'r') as file:
            lines = file.readlines()
            ensure_uniform_field_count(lines)
            return parse_lines_to_dictionaries(lines)
    else:
        print(f"File not found: {file_path}")
        return []
    
def parse_lines_to_dictionaries(lines):
    records = []
    header = check_for_header(lines)
    for line in lines[1:]:
        values = line.strip().split(',')
        record = dict(zip(header, values))
        records.append(record)
    return records


if __name__== "__main__":
    records = load_file("../datasets/blank.csv")
    print(records[:3])

