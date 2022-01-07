import pymol
import pymol.cmd as pm
import random
import csv
import os

def get_colors(selection='', quiet=1):
    pymol_color_list = []
    for tuplepair in pymol.querying.get_color_indices(selection):
        pymol_color_list.append(tuplepair[0])
    pymol_color_list.sort()
    if not int(quiet): print(pymol_color_list)
    return pymol_color_list

def get_random_color(selection='', quiet=1):
    randomcolor=random.choice(get_colors(selection, 1))
    if not int(quiet): print(randomcolor)
    return randomcolor

def setup():
    pm.util.performance(0)

def pdbhandle(pdbid):
    pm.fetch(pdbid)
    chains = pm.get_chains()
    for chain in chains:
        pm.color(get_random_color(), 'chain ' + chain)
        pm.extract(chain, 'chain ' + chain)
    pm.hide()
    pm.show('surface')
    pm.reset()
    pm.ray(3000,3000)
    pm.save("pics/" + pdbid, format='png')
    pm.reinitialize()


if __name__ == '__main__':
    pics = "/home/chris/pymolapi"
    with open('all.txt', newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
        data = data[0]
    for pdb in data:
        setup()
        pdbhandle(str(pdb))
        dir_name = "/home/chris/pymolapi"
        test = os.listdir(dir_name)
        for item in test:
            if item.endswith(".cif"):
                os.remove(os.path.join(dir_name, item))
            if item.endswith(".png"):
                os.rename(item, os.path.join("/home/chris/pymolapi/pics", item))
