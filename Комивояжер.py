from geopy.distance import geodesic
from geopy.geocoders import Nominatim

import time
start_time = time.time()


fin = open('input.txt', "r")
Geoloc=Nominatim(user_agent='Tester')
n_d = int(input('Введите количество городов: '))
d = [['0']*n_d for i in range(n_d)]
coord = []
cities = []
for i in range(n_d):
#    name = input(f"City {i+1} :")
    name = fin.readline()[:-1]
    print("City ", i+1, ': ', name, sep='')
    location = Geoloc.geocode(name)
    s = (location.latitude, location.longitude)
    coord.append(s)
    cities.append(name)
for i in range(len(coord)):
    for j in range(i+1, len(coord)):
        d[i][j] = str(int(geodesic(coord[i], coord[j]).km))
        d[j][i] = str(int(geodesic(coord[i], coord[j]).km))
minn = 10000
summ = 0
visit = [1] + [0] * len(d)
x = [0] * len(d)
n = len(d)
count = 0
way = []
z = 0

print(d)
ending = ''
for i in d:
    for j in i:
        ending += j + ' '
print(ending)


def dfs(a, count):
    global minn, way, z
    minn = count
    if minn < count:
        return
    if a >= n:
        count += int(d[x[a-1]][0]) # если доходим до конца, когда a=n,
        # то последний раз прибавляем прибавляем расстояние
        minn = count # присваиваем к миинимальному
        return
    else:
        for j in range(n):
            if visit[j] == 0: # если вершина еще не посещена
                visit[j] = 1 # то отмечаем как посещенную
                x[a] = j # вносим ее в наш путь
                way = x.copy() # купируем массив пути для дальнейшего вывода
                z += 1
                dfs(a+1, count+int(d[x[a-1]][j]))
                visit[j] = 0
                x[a] = 0


dfs(1, 0)
print('Пройденных километров:', minn)
print('Путь:')
print(*[cities[i] for i in way], sep=' -> ')
print(z, 'возможных перестановок')

print("--- %s секунд работает программа ---" % (time.time() - start_time))
