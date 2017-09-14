'''
Created on Sep 14, 2017

@author: klondaik
'''




def getData():
    """Получаем аргументы и разделяем на аргументы для пинг и ip адреса
        args = разделяем на аргументы для пинг
        ips = ip адреса
    """
    import sys
    i=0
    args=""
    ips=[]
    ar = sys.argv
    print(ar)
    for item in ar:
        if item=="args":
                args = ar[i+1]
        if item=="ip":
            ips = ar[i+1:]
        i+=1
    return args,ips


def runPings():
    """После получения аргументов запускаем подряд процессы пинг и выводим данные в вывод."""
    data = list(getData())
    import subprocess
    for item in data[1]:
        proc = subprocess.Popen("ping %s %s"%(data[0],item),shell=True,stdout=subprocess.PIPE)
        out = proc.stdout.readlines()
        #out = proc.communicate()
        for item in out:
            print(item.decode())
    
runPings()
    
# Содержимое file
#ten 1/1/1 - 8.8.8.8
#ten 1/1/2 - 127.0.0.1
# Пример запуска из командной строки
# python3 multiping.py args "-c 3" ip $(awk '{match($0,/[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+/); ip = substr($0,RSTART,RLENGTH); print ip}' file)


if __name__ == '__main__':
    pass