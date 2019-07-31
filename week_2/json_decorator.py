import json
import functools

def to_json(func):
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        result = func(*args, **kwargs)
        return (json.dumps(result))
    return wrapped

# print(json.dumps(None))
#
# @to_json
# def get_data():
#    return  None
#
#
# print(get_data())