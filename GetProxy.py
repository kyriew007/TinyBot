import requests


def GeneratPorxyNum(num):
    url = "http://dps.kdlapi.com/api/getdps/?orderid=910362950154248"
    url = url + "&num=%d&pt=1&format=json&sep=1" % num
    # proxy = requests.get(url=url)
    # proxy = proxy.json()
    return url

if __name__ == "__main__":
    num = int(input("please input proxy number:>>>"))
    url = GeneratPorxyNum(num)
    print(url)