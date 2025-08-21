#КЕГЭ 10574

from ipaddress import*

for m in range(33):
    net = ip_network(f'158.116.11.146/{m}', 0)
    if str(net.network_address) == '158.116.0.0':    #если адрес сети данный нам совпадает епта с адлресом данным по епта условию - то зашибись, выводим маску епта
        print(m)
