"""
1. feladat: Rizikó (határidő 2018-09-12 szerda 24:00, 4 pont)
A Rizikó (Risk) nevű társasjátékban egyszerre egy játékos maximum három katonájával tud támadni,
míg a védekező játékos legföljebb kettővel tud védekezni. Pontosan három támadó és két védő esetén
az összecsapás a következőképpen zajlik. A támadó játékos három piros kockával míg a védekező játékos
két kék kockával dob. Ezután összehasonlítjuk a támadó és a védő legnagyobb dobását. A kisebb érték birtokosa
veszít egy katonát, a döntetlen a védőnek kedvez, vagyis ekkor a támadó veszít egyet. Ezután a két fél második
legnagyobb dobását is összehasonlítjuk ugyanilyen módon. Így az összecsapásnak három kimenetele lehet: a támadó veszít két katonát,
döntetlen, azaz mindkét fél veszít 1-1 katonát, a védő veszít két katonát.
Szimulálja 1000-szer a kísérletet és ebből határozza meg a három esemény relatív gyakoriságát.
Szimulálja 1000000-szor a kísérletet és ebből határozza meg a három esemény relatív gyakoriságát.
Számolja ki a három kimenetel pontos valószínűségét az összes lehetséges eset megvizsgálásával.
A valószínűséget a kedvező esetek és az összes esetek hányadosa adja.
Ezeket az eredményeket is 5 tizedes pontossággal írja ki, köztük 3 szóközzel!
A program kimenete így nézzen ki (természetesen más számadatokkal)

                  Tamado    Dontetlen Vedo
1000 kíserlet:    0.35222   0.44444   0.20334
1000000 kíserlet: 0.33988   0.43011   0.23001
Valoszinuseg:     0.34000   0.43000   0.23000
"""

import random

attacker = []
defender = []

maxAttacker=1
secondbiggestAttacker=0

onlyAttackerLostSoldiers=0
onlyDefenderLostSoldiers=0
draws=0


for q in range(1,10000):

    print('-----------------------------------------------------')
    print('Attacker')
    maxAttacker=1
    for x in range(0, 3):
         attacker.append(int(random.random()*6)+1)
         if attacker[x]>maxAttacker:
            secondbiggestAttacker=maxAttacker
            maxAttacker=attacker[x]
    for a in range (0, len(attacker)):
        print(a, attacker[a])


    print('')
    print('Defender')

    maxDefender=1
    secondbiggestDefender=0
    for y in range(0, 2):
         defender.append(int(random.random()*6)+1)
         print(y, defender[y])
         if defender[y]>maxDefender:
            secondbiggestDefender = maxDefender
            maxDefender=defender[y]

    if maxAttacker>maxDefender:
        onlyDefenderLostSoldiers+=1
    elif maxAttacker<maxDefender:
        onlyAttackerLostSoldiers+=1
    elif maxAttacker==maxDefender:
        draws+=1

    attacker.clear()
    defender.clear()

print('*****************************************************')
print('Csak a támadó vesztett katonákat eset: ',onlyAttackerLostSoldiers)
print('Csak a védekező vesztett katonákat eset:',onlyDefenderLostSoldiers)
print('Döntetlenek száma, mindkettő veszít katonát: ',draws)
print('')
print(onlyAttackerLostSoldiers / 100,'%')
print(onlyDefenderLostSoldiers / 100,'%')
print(draws/100,'%')

print('*****************************************************')