import pokebase

avghp = 0
avgatk = 0
avgdef = 0
avgsatk = 0
avgsdef = 0
avgspd = 0

ALLP = pokebase.APIResourceList('pokemon')

for n in ALLP.names:
    
    poke = pokebase.NamedAPIResource('pokemon', n)
    
    for stat in poke.stats:
        if stat.stat.name == 'hp':
            avghp += stat.base_stat
        elif stat.stat.name == 'attack':
            avgatk += stat.base_stat
        elif stat.stat.name == 'defense':
            avgdef += stat.base_stat
        elif stat.stat.name == 'special-attack':
            avgsatk += stat.base_stat
        elif stat.stat.name == 'special-defense':
            avgsdef += stat.base_stat
        elif stat.stat.name == 'speed':
            avgspd += stat.base_stat
          
avghp /= len(ALLP)
avgatk /= len(ALLP)
avgdef /= len(ALLP)
avgsatk /= len(ALLP)
avgsdef /= len(ALLP)
avgspd /= len(ALLP)
print(f'HP : {avghp}\nAttack : {avgatk}\nDefense : {avgdef}\nSp. Attack : {avgsatk}\nSp. Defense : {avgsdef}\nSpeed : {avgspd}')
    
    