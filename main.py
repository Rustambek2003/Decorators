import json
def read_data(path:str)->dict:
    with open(path) as f:
        data = json.load(f)

    return data

print(read_data('data.csv'))