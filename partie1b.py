# Maël QUERRÉ
# Vincent DE MENEZES

from random import choice, randrange
from tkinter import *

n = 6

jeu = Tk()
jeu.title("Jeu 2048 - version L1 2017")


def partie(n):
    g3 = init(n)
    dessine_grille(g3)
    # Liaisons clavier-fonction
    jeu.bind('<Up>',
             lambda event: clavier(event, g3))
    jeu.bind('<Down>',
             lambda event: clavier(event, g3))
    jeu.bind('<Left>',
             lambda event: clavier(event, g3))
    jeu.bind('<Right>',
             lambda event: clavier(event, g3))


def message(m):
    texte_fin_partie.delete("0.0", END)
    texte_fin_partie.insert(END, m)


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


def couleur(nb):
    dico = {2: "#91FFD2",
            4: "#B2D8E7",
            8: "#B2C4DF",
            16: "#6FB8FF",
            32: "#339ED7",
            64: "#50EEEF",
            128: "#6893EC",
            256: "#0040EC",
            512: "#6F40E0",
            1024: "#7C0C59",
            2048: "#C50CD1"}
    return dico[nb]


def dessine_grille(g):
    n = len(g)
    cote = 70
    x0, y0 = 50, 50
    for i in range(n):
        for j in range(n):
            x = g[i][j]
            coords_tuile = (x0 + cote * j,
                            y0 + cote * i,
                            x0 + cote * (j + 1),
                            y0 + cote * (i + 1))
            if x != 0:
                if x > 64:
                    clr_text = "white"
                else:
                    clr_text = "black"
                clr = couleur(x)
                canvas.create_rectangle(coords_tuile, fill=clr, width=0)
                canvas.create_text(x0 + cote * j + cote / 2,
                                   y0 + cote * i + cote / 2,
                                   text=x, justify=CENTER, fill=clr_text,
                                   font=("Ubuntu", 20, "bold"))
            else:
                canvas.create_rectangle(coords_tuile, fill="white", width=0)
    for i in range(n + 1):
        canvas.create_line(x0 + cote * i, y0, x0 + cote * i, y0 + n * cote,
                           width=3,
                           fill="gray")
        canvas.create_line(x0, y0 + cote * i, x0 + n * cote, y0 + cote * i,
                           width=3,
                           fill="gray")


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
    val_1, val_2 = randrange(2, 5, 2), randrange(2, 5, 2)
    grille = ajoute_alea(grille, val_1)
    grille = ajoute_alea(grille, val_2)
    return grille


def haut(g):
    n = len(g)
    for j in range(n):  # on parcourt les colonnes
        i = 0
        while i < n - 1: # on effectue les fusions
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
            if g[x][y - 1] == g[x][y]:
                # si case précédente identique à case actuelle
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


# Fonctions Tkinter #

def quitter():
    jeu.quit()
    jeu.destroy()


def clavier(event, g):
    clef = event.keysym
    deplacer(g, clef)
    val_1 = randrange(2, 5, 2)
    g = ajoute_alea(g, val_1)
    dessine_grille(g)
    if pleine(g) or gagnante(g):
        jeu.unbind('<Up>')
        jeu.unbind('<Down>')
        jeu.unbind('<Left>')
        jeu.unbind('<Right>')
        if pleine(g):
            score = valeur_max(g)
            msg = "Fin de la partie, vous avez perdu." + '\n'
            msg += "Votre score est de " + str(score) + "."
            message(msg)
        if gagnante(g):
            message("Bravo vous avez gagné !")


# Widgets Tkinter #

canvas = Canvas(jeu, height=400, width=400, bg="white")
canvas.grid(row=0, rowspan=3)

bouton_jouer = Button(jeu, text="Jouer", command=lambda: partie(4))
bouton_jouer.grid(row=0, column=1)

texte_fin_partie = Text(jeu, width=40, height=2)
texte_fin_partie.grid(row=1, column=1)

# Bouton quitter
bouton_quitter = Button(jeu, text="Quitter", command=quitter)
bouton_quitter.grid(row=2, column=1)

jeu.mainloop()
