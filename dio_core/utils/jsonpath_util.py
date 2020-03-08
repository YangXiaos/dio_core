import jsonpath


def get_list_by_jsonpath(text, path):
    return jsonpath.jsonpath(text, path)