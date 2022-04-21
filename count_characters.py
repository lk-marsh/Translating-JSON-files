import json


# Count number of characters being translated
def count(file_handler):
    json_string = json.loads(file_handler.read())

    string: str = ''
    for value in json_string.values():
        string += value

    char_count = len(string)

    print('Number of characters:', char_count)
    return char_count


# Estimate cost of translation based on fixed exchange rate
def estimate_cost(count: int):

    # Exchange Rate
    usd_sgd = 1.36

    # Translate: $15 per million characters
    cost_per_char = 15/1000000

    est_cost = usd_sgd * cost_per_char * count

    print("Estimated cost for translation: {} SGD".format(est_cost))
    return float(est_cost)
