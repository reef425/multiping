# multiping
Результат работы команды ping для нескольких адресов

Пример запуска из командной строки:<p>
<b>python3 multiping.py args "-c 3" ip 8.8.8.8 127.0.0.1</b>

Пример запуска из командной строки с чтением адрсов из файла.<p>
<b>python3 multiping.py args "-c 3" ip $(awk '{match($0,/[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+/); ip = substr($0,RSTART,RLENGTH); print ip}' file)</b>

Содержимое файла file
<p><b>ten 1/1/1 - 8.8.8.8</b>
<p><b>ten 1/1/2 - 127.0.0.1</b>
