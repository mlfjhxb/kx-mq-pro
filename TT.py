from pandas._libs import json

if __name__ == '__main__':
    #字典转str
    var =[{"domain":".mail.126.com","httpOnly":"false","name":"starttime","path":"\/","secure":"true","value":""}]

    lst={"name":"hxb"}
    print(lst["name"])

    lst3={'name':'hxb'}
    print(lst3["name"])

    lst2='{"name":"hxb"}'
    print(eval(lst2)['name'])

    str='hello;world'
    print(', '.join(str.split(';')))

    ar=[{'name':'hxb'},{'name':'yx'}]
    print(len(ar),json.dumps(ar))
    for i in range(0,len(ar)):
         print(ar[i]["name"])

    print('------------')
    arr=json.dumps(ar)
    for i in json.decode(arr):
        print(i['name'])
    # logging.info(eval(cookies_str)["PHPSESSID"])
