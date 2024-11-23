import json

data = {}

responses = json.load(open('207188815.json'))
for response in responses:
    if "requestId" in response["params"].keys():
        request_id = response["params"]["requestId"]
        method = response["method"]
        if request_id not in data:
            data[request_id] = {}

        if method in data[request_id]:
            data[request_id][method].append(response)
        else:
            data[request_id][method] = [response]

    # print(list(response["params"].keys()))

with open("refined.json", "w") as outfile:
    json.dump(data, outfile)

print(list(data.keys()))
for datum in data:
    print(datum)
    for item in data[datum]:
        print(item, len(data[datum][item]))
#     types = [item["params"]["type"] for item in data[datum] if "type" in item["params"]]
#     methods = [item["method"] for item in data[datum] if "method" in item]
#     print(datum, *types, len(methods), len(set(methods)), *methods, len(data[datum]))
    # break
    # if "params" in data[datum]:
    #     print(datum["params"])
