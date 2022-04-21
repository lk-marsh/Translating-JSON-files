import json


# Write to a JSON file given keys and values
def to_json(keys: list, values: list, file_handler):

    # Check length of keys and values are matching
    if len(keys) != len(values):
        print("Error: lengths of keys and values don't match!")
        return

    json_object = {}
    for i in range(len(keys)):
        json_object[keys[i]] = values[i]

    file_handler.write(json.dumps(json_object, ensure_ascii=False, indent=4))


# Write a list of values to a .txt file.
def to_text(file_handler, values: list):
    for value in values:
        line_break_included = str(value + "\n")
        file_handler.write(line_break_included)
