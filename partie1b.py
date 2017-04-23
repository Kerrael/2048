from random import choice, randrange
from tkinter import *

n = 6

jeu = Tk()
jeu.title("Jeu 2048 - version L1 2017")


def partie(n):
    g3 = init(n)
    dessine_grille(g3)
    # Liaisons touche-fonction
    jeu.bind('<Up>',
             lambda event: touche(event, g3))
    jeu.bind('<Down>',
             lambda event: touche(event, g3))
    jeu.bind('<Left>',
             lambda event: touche(event, g3))
    jeu.bind('<Right>',
             lambda event: touche(event, g3))


def message(m):
    label_fin_partie.config(text=m)


def deplacer(grille, direction):
    if direction == "Up":
        grille = haut(grille)
    elif direction == "Down":
        grille = bas(grille)
    elif direction == "Left":
        grille = gauche(grille)
    elif direction == "Right":
        grille = droite(grille)
    return grille


def cree_grille(n, val):
    lst = [0] * n
    for i in range(n):
        lst[i] = [val] * n
    return lst


def couleur(n):
    dico = {2: "#91FFD2", 4: "#B2D8E7", 8: "#B2C4DF", 16: "#6FB8FF",
            32: "#339ED7", 64: "#50EEEF", 128: "#6893EC", 256: "#0040EC",
            512: "#6F40E0", 1024: "#7C0C59", 2048: "#C50CD1"}
    return dico[n]


def dessine_grille(g):
    n = len(g)
    cote = 70
    x0, y0 = 50, 50
    for i in range(n):
        for j in range(n):
            x = g[i][j]
            coords_tuile = (x0 + cote * j,
                            y0 + cote * i + 1,
                            x0 + cote * (j + 1),
                            y0 + cote * (i + 1))
            if x != 0:
                if x > 64:
                    clr_text = "white"
                else:
                    clr_text = "black"
                clr = couleur(x)
                can.create_rectangle(coords_tuile, fill=clr, width=0)
                can.create_text(x0 + cote * j + cote / 2,
                                y0 + cote * i + cote / 2,
                                text=x, justify=CENTER, fill=clr_text,
                                font=("Ubuntu", 20, "bold"))
            else:
                can.create_rectangle(coords_tuile, fill="white", width=0)
    for i in range(n + 1):
        can.create_line(x0 + cote * i, y0, x0 + cote * i, y0 + n * cote,
                        width=3, fill="gray")
        can.create_line(x0, y0 + cote * i, x0 + n * cote, y0 + cote * i,
                        width=3, fill="gray")


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
    for j in range(n):  # on parcourt les colonnes
        x, y = i, j
        while x < n - 1:  # fusions
            if g[x + 1][y] == g[x][y]:  # si deux éléments identiques
                g[x][y] *= 2  # alors on les fusionne
                g[x + 1][y] = 0
            x += 1
    # i = 0
    # while i < n - 1:
    for j in range(n):
        x, y = i, j
        while x < n - 1:
            if g[x][y] == 0 and g[x + 1][y] != 0:
                while x >= 0 and g[x][y] == 0:
                    g[x][y] = g[x + 1][y]
                    g[x + 1][y] = 0
                    x -= 1
            x += 1
            # i += 1
    return g


def bas(g):
    n = len(g)
    i = n - 1
    for j in range(n):  # on parcourt les colonnes
        x, y = i, j
        while x > 0:  # fusions
            if g[x - 1][y] == g[x][y]:  # si deux éléments identiques
                g[x][y] *= 2  # alors on les fusionne
                g[x - 1][y] = 0
            x -= 1
    # i = n - 1
    # while i > 0:
    for j in range(n):
        x, y = i, j
        while x > 0:
            if g[x][y] == 0 and g[x - 1][y] != 0:
                while x < n and g[x][y] == 0:
                    g[x][y] = g[x - 1][y]
                    g[x - 1][y] = 0
                    x += 1
            x -= 1
            # i -= 1
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
        while y > 0:  # fusions
            if g[x][y - 1] == g[x][y]:
                # si case précédente identique à case actuelle
                g[x][y] *= 2
                g[x][y - 1] = 0
            y -= 1
        while j > 0:  # déplacements une fois les fusions faites
            if g[i][j] == 0 and g[i][j - 1] != 0:
                while j < n and g[i][j] == 0:
                    g[i][j] = g[i][j - 1]
                    g[i][j - 1] = 0
                    j += 1
            j -= 1
    return g


# Fonctions Tkinter #

def quitter():
    jeu.quit()
    jeu.destroy()


def touche(event, g):
    clef = event.keysym
    deplacer(g, clef)
    val1 = randrange(2, 5, 2)
    g = ajoute_alea(g, val1)
    dessine_grille(g)
    if pleine(g) or gagnante(g):
        jeu.unbind('<Up>')
        jeu.unbind('<Down>')
        jeu.unbind('<Left>')
        jeu.unbind('<Right>')
        if pleine(g):
            score = valeur_max(g)
            msg = "Fin de la partie, vous avez perdu." + " "
            msg += "Votre score est de " + str(score) + "."
            message(msg)
        if gagnante(g):
            message("Bravo vous avez gagné")


# Widgets Tkinter #

can = Canvas(jeu, height=400, width=400, bg="white")
can.grid(row=0, rowspan=3)

bJouer = Button(jeu, text="Jouer", command=lambda: partie(4))
bJouer.grid(row=0, column=1)

label_fin_partie = Label(jeu)
label_fin_partie.grid(row=1, column=1)

# Bouton quitter
bQuitter = Button(jeu, text="Quitter", command=quitter)
bQuitter.grid(row=2, column=1)

jeu.mainloop()
