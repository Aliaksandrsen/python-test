import requests

print(2 + 2)

r = requests.get("https://coreyms.com")


def foo(x):
    print(x)


print(r.status_code)
