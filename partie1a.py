from random import choice, randrange


def main():
    # g3 = init(4)
    g3 = [[2, 4, 2, 2, 0],
          [0, 4, 0, 0, 4],
          [2, 0, 2, 2, 0],
          [0, 4, 0, 2, 2],
          [2, 2, 0, 2, 0]]
    affiche(g3)
    while not gagnante(g3) or not pleine(g3):
        d = input("Direction : ")
        g3 = deplacer(g3, d)
        # val1 = randrange(2, 5, 2)
        # g3 = ajoute_alea(g3, val1)
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


def valeur_max(g):
    res = 0
    for x in g:
        for y in x:
            if y > res:
                res = y
    return res


def lst_cases(g, val):
    lst = []
    for i in range(len(g)):
        for j in range(len(g)):
            if g[i][j] == val:
                lst.append([i, j])
    return lst


def vides(g):
    return lst_cases(g, 0)


def ajoute_alea(g, val):
    pos = choice(vides(g))
    g[pos[0]][pos[1]] = val
    return g


def init(n):
    grille = cree_grille(n, 0)
    val1, val2 = randrange(2, 5, 2), randrange(2, 5, 2)
    grille = ajoute_alea(grille, val1)
    grille = ajoute_alea(grille, val2)
    return grille


def haut(g):
    n = len(g)
    i = 0
    while i < n - 1:
        for j in range(n):  # on parcourt les colonnes
            x, y = i, j
            while x < n - 1:  # fusions
                if g[x + 1][y] == g[x][y]:  # si deux éléments identiques
                    g[x][y] *= 2  # alors on les fusionne
                    g[x + 1][y] = 0
                x += 1
        i += 1
    i = 0
    while i < n - 1:
        for j in range(n):
            x, y = i, j
            while x < n - 1:
                if g[x][y] == 0 and g[x + 1][y] != 0:
                    while i >= 0 and g[x][y] == 0:
                        g[x][y] = g[x + 1][y]
                        g[x + 1][y] = 0
                        x -= 1
                x += 1
        i += 1
    return g


def bas(g):
    n = len(g)
    i = n - 1
    while i > 0:
        for j in range(n):  # on parcourt les colonnes
            x, y = i, j
            while x > 0:  # fusions
                if g[x - 1][y] == g[x][y]:  # si deux éléments identiques
                    g[x][y] *= 2  # alors on les fusionne
                    g[x - 1][y] = 0
                x -= 1
        i -= 1
    i = n - 1
    while i > 0:
        for j in range(n):
            x, y = i, j
            while x > 0:
                if g[x][y] == 0 and g[x - 1][y] != 0:
                    while x < n and g[x][y] == 0:
                        g[x][y] = g[x - 1][y]
                        g[x - 1][y] = 0
                        x += 1
                x -= 1
        i -= 1
    return g


def gauche(g):
    n = len(g)
    for i in range(n):  # on parcourt les lignes
        j = 0
        x, y = i, j
        while y < n - 1:  # fusions
            if g[x][y + 1] == g[x][y]:  # si deux éléments identiques
                g[x][y] *= 2  # alors on les fusionne
                g[x][y + 1] = 0
            y += 1
        while j < n - 1:  # déplacements
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
        while y > 0:  # fusions une fois les déplacements faits
            if g[x][y - 1] == g[x][y]:
                g[x][y] *= 2
                g[x][y - 1] = 0
            y -= 1
        while j > 0:  # déplacements
            if g[i][j] == 0 and g[i][j - 1] != 0:
                while j < n and g[i][j] == 0:
                    g[i][j] = g[i][j - 1]
                    g[i][j - 1] = 0
                    j += 1
            j -= 1
    return g


g1 = [[2, 2, 2, 2], [4, 0, 2, 8], [0, 16, 32, 0], [128, 256, 1024, 2048]]
g2 = [[2, 2, 2, 2], [4, 0, 2, 8], [0, 16, 32, 0], [128, 256, 16, 32]]

print("Grille g1 :")
affiche(g1)
print("appartient(1024, g1) :", appartient(1024, g1))
print("appartient(512, g1) :", appartient(512, g1))
print("appartient(0, g1) :", appartient(0, g1))
print("gagnante(g1) :", gagnante(g1))
print("pleine(g1) :", pleine(g1))
print("vides(g1) :", vides(g1))

print("------------------------------------", '\n')

print("Grille g2 :")
affiche(g2)
print("valeur_max(g2) :", valeur_max(g2))
print("lst_cases(g2, 16) :", lst_cases(g2, 16))

print("------------------------------------", '\n')


main()

# def afficher(grille):
#     res = ""
#     i = 0
#     while i < len(grille):
#         j = 0
#         while j < len(grille):
#             if (j, 2) in positions(grille):
#                 if len(str(grille[i][j])) != 2:
#                     res += " "
#             if (j, 3) in positions(grille):
#                 if len(str(grille[i][j])) != 3:
#                     res += "  "
#             if (j, 4) in positions(grille):
#                 if len(str(grille[i][j])) != 4:
#                     res += "   "
#             res += str(grille[i][j]) + " "
#             j += 1
#         res += '\n'
#         i += 1
#     print(res)
#
#
# def positions(g):
#     pos = []
#     i = 0
#     while i < len(g):
#         j = 0
#         while j < len(g):
#             if len(str(g[i][j])) == 2:
#                 pos.append((j, 2))  # (colonne, nb_caractères)
#             elif len(str(g[i][j])) == 3:
#                 pos.append((j, 3))
#             elif len(str(g[i][j])) == 4:
#                 pos.append((j, 4))
#             j += 1
#         i += 1
#     return pos
