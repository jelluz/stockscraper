import json
from stockscraper import parse_response

def test_parse_response():
    with open('akza.json') as fp:
        data = json.load(fp)

    my_dict = parse_response(data)

