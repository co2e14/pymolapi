import itertools
import makepic
import os

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

keywords = [''.join(i) for i in itertools.product(alphabets, repeat = 3)]
ones = ['4' + key for key in keywords]
for x in ones:
    print(x)
    makepic.pdbhandle(x)
    os.remove(x + '.pdb')
    os.remove(x + '.cif')