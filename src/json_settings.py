import json
def write_dict_to_json(d, start, end, filename):
    new_dict = {"startingState": start}
    final_states = d.get(('acceptingState', ''), [])
    for k, v in d.items():
        src, input_char = k
        if src not in new_dict:
            new_dict[src] = {"isTerminatingState": False}
        if input_char not in new_dict[src]:
            new_dict[src][input_char] = []
        if input_char == 'ε':
            new_dict[src][input_char].extend(v)
        else:
            new_dict[src][input_char] = v[0]
        new_dict[src]["isTerminatingState"] = src in final_states or v[0] in final_states
        if v[0] not in new_dict:
            new_dict[v[0]] = {"isTerminatingState": bool(v[0] in final_states)}
    for each_end in end:
        new_dict[each_end]["isTerminatingState"] = True
    # Add line breaks after each state
    json_str = json.dumps(new_dict, indent=4)
    for state in new_dict.keys():
        json_str = json_str.replace(f'"{state}":', f'\n    "{state}":')
    with open(filename, "w") as f:
        f.write(json_str)




# write nfa to json file
# def write_dict_to_json(d, start, end, filename):
#     new_dict = {"startingState": start}
#     final_states = d.get(('acceptingState', ''), [])
#     for k, v in d.items():
#         src, input_char = k
#         if src not in new_dict:
#             new_dict[src] = {"isTerminatingState": False }
#         if input_char not in new_dict[src]:
#             new_dict[src][input_char] = []
#         if input_char == "\u03b5":
#             new_dict[src][input_char].extend(v)
#         else:
#             new_dict[src][input_char] = v[0]
#         new_dict[src]["isTerminatingState"] = src in final_states or v[0] in final_states
#         if v[0] not in new_dict:
#             new_dict[v[0]] = {"isTerminatingState": bool(v[0] in final_states)}
#     new_dict[end]["isTerminatingState"] = True
#     with open(filename, "w") as f:
#         json.dump(new_dict, f)
