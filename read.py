import json


# Returns a list of keys/values of a json file. Returns the values by default. Specify key=True to return keys.
def return_key_or_value(file_handler, key: bool = False) -> list:

    fh = open(file_handler.name, 'r', encoding="utf8")

    json_string = fh.read()
    json_object = json.loads(json_string)

    # Extract the keys or values depending on input
    if key:
        json_keys_list = list(json_object.keys())
        return json_keys_list
    else:
        json_values_list = list(json_object.values())
        return json_values_list
