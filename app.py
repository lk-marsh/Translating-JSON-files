# Functions
import call_api
import count_characters

# Modules contain functions to read and write to files respectively
import read
import write

# Environment Variables
src_file = r"C:\Users\u1261919\OneDrive - MMC\Documents\Translation\paid-api-with-amazon\input-files\test_en.json"
dest_file = r"C:\Users\u1261919\OneDrive - MMC\Documents\Translation\paid-api-with-amazon\output-files\translated.json"
txt_file = r"C:\Users\u1261919\OneDrive - MMC\Documents\Translation\paid-api-with-amazon\output-files\translated.txt"

# Translation Config
src_lang_code = "en"
target_lang_code = "ja"

# File handlers
src_file_handler = open(src_file, 'r', encoding="utf8")
dest_file_handler = open(dest_file, 'w', encoding="utf8")
write_to_txt_file_handler = open(txt_file, 'w', encoding="utf8")

# The keys and values of source JSON file
json_keys = read.return_key_or_value(src_file_handler, key=True)
src_lang_values = read.return_key_or_value(src_file_handler)

# Estimate cost of translation
char_count = count_characters.count(src_file_handler)
count_characters.estimate_cost(char_count)

decision = input(
    "Do you want to proceed with the translation? 'n' to terminate.\n")
if decision == "n":
    print("Thank you!")
else:
    # Call Amazon Translate API to get the list of translated values
    translated_values = []
    for line in src_lang_values:
        if len(line):
            translated_values.append(call_api.translate(
                line, target_lang_code, src_lang_code
            ))
        else:
            translated_values.append('')

    # Create JSON file
    write.to_json(json_keys, translated_values, dest_file_handler)

    # Create .txt file of translated values
    write.to_text(write_to_txt_file_handler, translated_values)

    print("Output JSON and .txt files written to output-files.")
