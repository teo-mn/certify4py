import json


def json_wrap(data):
    if data is None:
        return "null"
    if type(data) is str:
        return "\"" + data.lower() + "\""
    if type(data) is int:
        return str(data).lower()
    if type(data) is float:
        return str(data).lower()
    if type(data) is list:
        res = "["
        first = True
        for x in data:
            if first is False:
                res += ","
            first = False
            res += json_wrap(x)
        res += "]"
        return res.lower()
    if type(data) is dict:
        data_dict = dict(data)
        keys = data_dict.keys()
        res = "{"
        first = True
        for key in sorted(keys):
            if first is False:
                res += ","
            first = False
            res += "\"" + key + "\":"
            res += json_wrap(data[key])
        res += "}"
        return res.lower()
    return str(data).lower()


if __name__ == "__main__":
    f = open('/home/surenbayar/1.json')
    json_data = json.load(f)
    print(json_data)
    print(json_wrap(json_data))
