import requests
import json


def tool_request_post(url, post_data, headers, timeout_t=(5, 10)):
    try:
        req = requests.post(url, timeout=timeout_t, data=post_data, headers=headers)
        # print(req.text)
        data = json.loads(req.text)
        return data
    except:
        return None


def tool_request_get(url, get_data, timeout_t=(5, 10)):
    try:
        req = requests.get(url, timeout=timeout_t, params=get_data)
        # print(req.text)
        data = json.loads(req.text)
        return data
    except:
        return None


def example_raw_json():
    """
    function: just like postman raw json request with Cookie
    :return:
    """
    value = {"member_ids": ["812738c1-e975-4b4c-84f9-f849ad7dc0fe"], "this_date": "2020-06-04"}
    value = json.dumps(value)
    url = 'http://xxxxxx.xxxx.cn/api/intranet/xxxxxx'

    headers = {
        'Content-Type': "application/json",
        "Cookie": "_ga=GA1"
    }

    res = tool_request_post(url, value, headers)
    print(res)


if __name__ == "__main__":
    example_raw_json()

