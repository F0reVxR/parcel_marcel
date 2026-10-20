import requests

def get_proxy():
    arr = {}
    r = requests.get("https://advanced.name/freeproxy/6ad1fb5314908")
    new_text = r.text.splitlines()
    for item in new_text:
        new_arr = str(item).split(':')
        arr.update({new_arr[0]:new_arr[1]})
    return arr