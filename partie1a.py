# Maël QUERRÉ
# Vincent DE MENEZES

from random import choice, randrange


def partie(n):
    g3 = init(n)
    affiche(g3)
    while not gagnante(g3) and not pleine(g3):
        d = input("Direction : ")
        g3 = deplacer(g3, d)
        val_1 = randrange(2, 5, 2)
        g3 = ajoute_alea(g3, val_1)
        affiche(g3)


def deplacer(grille, direction):
    if direction == "h":
        grille = haut(grille)
    elif direction == "b":
        grille = bas(grille)
    elif direction == "g":
        grille = gauche(grille)
    elif direction == "d":
        grille = droite(grille)
    return grille


def cree_grille(n, val):
    lst = [0] * n
    for i in range(n):
        lst[i] = [val] * n
    return lst


def affiche(grille):
    res = ""
    for x in grille:
        for y in x:
            if y in range(10):
                res += "   "
            elif y in range(10, 100):
                res += "  "
            elif y in range(100, 1000):
                res += " "
            res += str(y) + " "
        res += '\n'
    print(res)


def appartient(e, g):
    for x in g:
        for y in x:
            if y == e:
                return True
    return False


def gagnante(g):
    return appartient(2048, g)


def pleine(g):
    return not appartient(0, g)


def valeur_max(g):  # 'max' est un built-in
    res = 0
    for x in g:
        for y in x:
            if y > res:
                res = y
    return res


def les_cases(g, val):
    lst = []
    for i in range(len(g)):
        for j in range(len(g)):
            if g[i][j] == val:
                lst.append([i, j])
    return lst


def vides(g):
    return les_cases(g, 0)


def ajoute_alea(g, val):
    pos = choice(vides(g))
    g[pos[0]][pos[1]] = val
    return g


def init(n):
    grille = cree_grille(n, 0)
    val_1, val_2 = randrange(2, 5, 2), randrange(2, 5, 2)
    grille = ajoute_alea(grille, val_1)
    grille = ajoute_alea(grille, val_2)
    return grille

def haut(g):
    n = len(g)
    for j in range(n):  # on parcourt les colonnes
        i = 0
        while i < n - 1:  # on effectue les fusions
            if g[i][j] != 0 and g[i + 1][j] == g[i][j]:
                g[i][j] *= 2
                g[i + 1][j] = 0
            i += 1
        i = 0
        while i < n - 1:  # déplacements une fois les fusions effectuées
            if g[i][j] == 0 and g[i + 1][j] != 0:
                x, y = i, j
                while x >= 0 and g[x][y] == 0:
                    g[x][y] = g[x + 1][y]
                    g[x + 1][y] = 0
                    x -= 1
            i += 1
    return g


def bas(g):
    n = len(g)
    for j in range(n):
        i = n - 1
        while i > 0:  # fusions
            if g[i][j] != 0 and g[i - 1][j] == g[i][j]:
                g[i][j] *= 2
                g[i - 1][j] = 0
            i -= 1
        i = n - 1
        while i > 0:  # déplacements une fois les fusions effectuées
            if g[i][j] == 0 and g[i - 1][j] != 0:
                x, y = i, j
                while x < n and g[x][y] == 0:
                    g[x][y] = g[x - 1][y]
                    g[x - 1][y] = 0
                    x += 1
            i -= 1
    return g


def gauche(g):
    n = len(g)
    for i in range(n):  # on parcourt les lignes
        j = 0
        x, y = i, j
        while y < n - 1:  # fusions
            if g[x][y] != 0 and g[x][y + 1] == g[x][y]:
                g[x][y] *= 2
                g[x][y + 1] = 0
            y += 1
        while j < n - 1:  # déplacements une fois les fusions effectuées
            if g[i][j] == 0 and g[i][j + 1] != 0:
                while j >= 0 and g[i][j] == 0:
                    g[i][j] = g[i][j + 1]
                    g[i][j + 1] = 0
                    j -= 1
            j += 1
    return g


def droite(g):
    n = len(g)
    for i in range(n):  # on parcourt les lignes
        j = n - 1
        x, y = i, j
        while y > 0:  # fusions
            if g[x][y] != 0 and g[x][y - 1] == g[x][y]:
                g[x][y] *= 2
                g[x][y - 1] = 0
            y -= 1
        while j > 0:  # déplacements une fois les fusions effectuées
            if g[i][j] == 0 and g[i][j - 1] != 0:
                while j < n and g[i][j] == 0:
                    g[i][j] = g[i][j - 1]
                    g[i][j - 1] = 0
                    j += 1
            j -= 1
    return g

partie(6)
