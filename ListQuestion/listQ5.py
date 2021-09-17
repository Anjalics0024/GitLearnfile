heros=['spider man','thor','hulk','iron man','captain america']

heros.append('black panther')
print("Add 'black panther' at the end of this list : ", heros)

#You realize that you need to add 'black panther' after 'hulk',
#so remove it from the list first and then add it after 'hulk'
heros.remove('black panther')
heros.insert(3,'black panther')
print("you need to add 'black panther' after 'hulk' : ", heros)

heros[1:3] = ['anjali Chauhan']
print(heros)

heros.sort()
print(heros)