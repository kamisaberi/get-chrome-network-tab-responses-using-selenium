import json

req_id_method_data = {}
type_method_data = {}
type_req_id_data = {}

responses = json.load(open('207188815.json'))
for response in responses:
    # request_id > method
    if "requestId" in response["params"].keys():
        request_id = response["params"]["requestId"]
        method = response["method"]
        if request_id not in req_id_method_data:
            req_id_method_data[request_id] = {}

        if method in req_id_method_data[request_id]:
            req_id_method_data[request_id][method].append(response)
        else:
            req_id_method_data[request_id][method] = [response]

    # type > method
    if "type" in response["params"].keys():
        type_ = response["params"]["type"]
        method = response["method"]
        if type_ not in type_method_data:
            type_method_data[type_] = {}
        if method in type_method_data[type_]:
            type_method_data[type_][method].append(response)
        else:
            type_method_data[type_][method] = [response]

    if "type" in response["params"].keys() and "requestId" in response["params"].keys():
        type_ = response["params"]["type"]
        request_id = response["params"]["requestId"]
        if type_ not in type_req_id_data:
            type_req_id_data[type_] = {}
        if request_id in type_req_id_data[type_]:
            type_req_id_data[type_][request_id].append(response)
        else:
            type_req_id_data[type_][request_id] = [response]

    # print(list(response["params"].keys()))

with open("req_id_method_data.json", "w") as outfile:
    json.dump(req_id_method_data, outfile)

with open("type_method_data.json", "w") as outfile:
    json.dump(type_method_data, outfile)

with open("type_req_id_data.json", "w") as outfile:
    json.dump(type_req_id_data, outfile)

print(list(req_id_method_data.keys()))
print(list(type_method_data.keys()))
# for datum in req_id_data:
#     print(datum)
#     for item in req_id_data[datum]:
#         print(item, len(req_id_data[datum][item]))
#     types = [item["params"]["type"] for item in data[datum] if "type" in item["params"]]
#     methods = [item["method"] for item in data[datum] if "method" in item]
#     print(datum, *types, len(methods), len(set(methods)), *methods, len(data[datum]))
# break
# if "params" in data[datum]:
#     print(datum["params"])
