import requests

def expensive_call(url):

    resp = requests.get(url=url)

    return len(resp.text.split())

def do_something_else():

    for i in range(1000):

        print(i)

def on_success_count(job, connection, result, *args, **kwargs):

    print(f"the results {result}")





