#Class Listkeeper is a class that provides methods to work with lists.
class ListKeeper:

    #Verwende dictionairy um Listen zu speichern.
    example = dict()

    #initialisiere Klasse mit einer Liste die 1,2,3,4,5 enthält
    def __init__(self):
        example["listOne"]=[1,2,3,4,5]

    #Methode zum Anzeigen aller Listen innerhalb des dictionairys
    def show(self):
        keys = []
        for key in self.example:
            keys.append(key)
        return keys

    #Methode zum Hinzufügen einer Liste
    def add(self, name, list):
        self.example[name] = list

    #Methode zum Löschen der Liste name
    def delete(self, name):
        self.example.pop(name)

    #Methode zum Sortieren der Elemente in der Liste name
    def sort(self, name):
        self.example[name].sort()

    #Methode zum Hinzufügen von den Werten list zur Liste name
    def append(self, name, list):
        self.example[name].append(list)

    #Methode zum betrachten der Liste
    def getList(self, name):
        return self.example[name]