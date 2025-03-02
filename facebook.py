from __future__ import annotations
from collections import deque

class User:
    def __init__(self,name) -> None:
        self.name: str = name
        self.friends: list[User] =[]

class Facebook:
    def __init__(self)->None:
        self._users:dict[str,User]={}

    def pridej_uzivatel(self, name:str)->None:
        self._users[name]=User(name)
    
    def pridej_znamost(self,name1,name2)->None:
        user1_uzel=self._users[name1]
        user2_uzel=self._users[name2]
        #
        user1_uzel.friends.append(user2_uzel)
        user2_uzel.friends.append(user1_uzel)

    def jak_daleko(self,name1,name2):
        if name1 not in self._users or name2 not in self._users:
            return None
        fronta = deque()  
        fronta.append((self._users[name1], 0))
        seznam=[]

        while fronta:
            aktualni, vzdalenost = fronta.popleft()
            seznam.append(aktualni)
            if aktualni.name == name2:
                return vzdalenost
            for soused in aktualni.friends:
                if soused not in seznam:
                    fronta.append((soused, vzdalenost + 1))            
        return None

# Vytvoření instance Facebooku
fb = Facebook()

# Seznam unikátních jmen
jmena = [
    "Adam", "Beata", "Cyril", "Dana", "Emil", "František", "Gabriela", "Hana", "Ivan", "Jana",
    "Karel", "Lenka", "Marek", "Nina", "Ondřej", "Petra", "Quentin", "Radka", "Stanislav", "Tereza",
    "Urbán", "Veronika", "Walter", "Xenie", "Yvona", "Zdeněk", "Alex", "Blanka", "Cecilie", "David"
]

# Vkládání známostí do Facebooku
for jmeno in jmena:
    fb.pridej_uzivatel(jmeno)
  
# Hardkodované známosti
znamosti = [
    ("Adam", "Beata"), ("Adam", "Cyril"), ("Beata", "Dana"),
    ("Cyril", "Emil"), ("Cyril", "František"), ("Dana", "Gabriela"),
    ("Emil", "Hana"), ("František", "Ivan"), ("Gabriela", "Jana"),
    ("Hana", "Karel"), ("Ivan", "Lenka"), ("Jana", "Marek"),
    ("Karel", "Nina"), ("Lenka", "Ondřej"), ("Marek", "Petra"),
    ("Nina", "Quentin"), ("Ondřej", "Radka"), ("Petra", "Stanislav"),
    ("Quentin", "Tereza"), ("Radka", "Urbán"), ("Stanislav", "Veronika"),
    ("Tereza", "Walter"), ("Urbán", "Xenie"), ("Veronika", "Yvona"),
    ("Walter", "Zdeněk"), ("Xenie", "Alex"), ("Yvona", "Blanka"),
    ("Zdeněk", "Cecilie"), ("Alex", "David"), ("Blanka", "Adam")
]

# Vkládání známostí do Facebooku
for clovek1, clovek2 in znamosti:
    fb.pridej_znamost(clovek1, clovek2)
