from random import randint

szamok:list[int] = []

for i in range(100):
    szam = randint(200, 1999) * 5
    szamok.append(szam)
    print(szam, end=' ')
    if i % 10 == 9: print(end='\n')

osszeg:int = 0
for szam in szamok:
    osszeg += szam
print(f'számok összege: {osszeg}')

db_4K5K:int = 0
ossz_4K5K:int = 0
for szam in szamok:
    if 4000 <= szam < 5000:
        db_4K5K += 1
        ossz_4K5K += szam
print(f'4 és 5K közötti számok átlaga: {ossz_4K5K / db_4K5K}')

maxi:int = 0
for i in range(len(szamok)):
    if szamok[i] > szamok[maxi]:
        maxi = i
print(f'a megnagyobb szám: {szamok[maxi]}, indexe: {maxi}')
print(f'sor: {maxi // 10 + 1}, oszlop: {maxi % 10 + 1}')

i:int = 0
while i < len(szamok) and szamok[i] % 65 != 0:
    i += 1
if i < len(szamok):
    print(f'VAN 65-el osztható szám: {szamok[i]}, indexe: {i}')
else: print('NINCS a listában 65 többszöröse')

db3e_v1:int = 0
for szam in szamok:
    if szam // 1000 == 3:
        db3e_v1 += 1
print(f'3mas számjeggyel kezdődő számok darabszáma: {db3e_v1}')

db3e_v2:int = 0
for szam in szamok:
    if 3000 <= szam < 4000:
        db3e_v2 += 1
print(f'3mas számjeggyel kezdődő számok darabszáma: {db3e_v2}')

db3e_v3:int = 0
for szam in szamok:
    if str(szam)[0] == '3':
        db3e_v3 += 1
print(f'3mas számjeggyel kezdődő számok darabszáma: {db3e_v3}')