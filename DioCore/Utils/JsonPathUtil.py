import jsonpath


def getListByJsonpath(text, path):
    return jsonpath.jsonpath(text, path)