import json

data = {}

responses = json.load(open('207188815.json'))
for response in responses:
    if "requestId" in response["params"].keys():
        if response["params"]["requestId"] in data:
            data[response["params"]["requestId"]].append(response)
        else:
            data[response["params"]["requestId"]] = [response]

    # print(list(response["params"].keys()))

print(list(data.keys()))
for datum in data:
    print(datum, *[item["params"]["type"] for item in data[datum] if "type" in item["params"]],
          [item["method"] for item in data[datum] if "method" in item], len(data[datum]))
    # break
    # if "params" in data[datum]:
    #     print(datum["params"])
