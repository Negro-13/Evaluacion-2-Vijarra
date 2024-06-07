import requests, json

print('Selecione un numero de post entre 1 y 100')
cantpost = int(input())
index = 1

posts = []
primo = []
noprimo = []
while True:
    if cantpost > 0 and cantpost < 100:
        url = f'https://jsonplaceholder.typicode.com/posts/{index}'
        getApy = requests.get(url)
        data = getApy.json()
        #no me salio la func numprime
        if index <= cantpost:
            if data['id'] % 2 == 0:
                index += 1
                primo.append(data)
            else:
                index +=1
                noprimo.append(data)
        else:
            break
    else:
        print('Selecione un numero entre 1 y 100')
        cantpost = int(input())
#verifico q me devuelve las cosas cumpliendo al condicion
print('Los post primos son:')
print(primo)
print('Los post no primos son:')
print(noprimo)

primef = open('./Downloads/dlXPrimes.json','w')
primef.write({'numeros primos': primo})
primef.close()

noprimef = open('./Downloads/dlXNotPrimes.json','w')
noprimef.write({'numeros no primos': noprimo})
noprimef.close()



