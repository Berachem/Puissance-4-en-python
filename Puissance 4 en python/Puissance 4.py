def grille_vide():
    """
    Fonction qui renvoie une grille vide
    """
    g = [[0 for i in range(7)] for j in range(6)]

    return g
    
##############################################


def affiche(g):
    """
    Fonction qui affiche la grille haut en bas
    """
    for i in range(len(g)):
        print(g[len(g)-i-1])

##############################################

def coup_possible(g,c):
    """
    Fonction qui renvoie un booléen si il est possible de jouer dans la colonee c
    """
    for i in range(len(g)):
        if g[i][c] ==0:
            return True
    return False
    
##############################################

def jouer(g,j,c):
    """
    Fonction qui renvoie une grille après que le joueur j est joué dans la colonne c
    """
    for i in range(len(g)):
        if g[i][c] == 0:
            g[i][c] = j
            return g
            

##############################################

def horiz(g,j,l,c):
    """
    Fonction qui renvoie un booléen pour dire si 4 jeton du joueur j sont alignés dans la ligne l
    """
    for i in range(4):
        if g[l][i] == j and g[l][i] == g[l][i+1] and g[l][i] == g[l][i+2] and g[l][i] == g[l][i+3]:
            return True
    return False
    

def vert(g,j,l,c):
    """
    Fonction qui renvoie un booléen pour dire si 4 jeton du joueur j sont alignés dans la colonne c
    """
    for i in range(3):
        if g[i][c] == j and g[i][c] == g[i+1][c] and g[i][c] == g[i+2][c] and g[i][c] == g[i+3][c]:
            return True
    return False
                    


def diag(g,j,l,c):
    """
    Fonction qui renvoie un booléen pour dire si 4 jeton du joueur j sont alignésen diagonal du jeton de coordonnés (c,l)
    """
    if l<=2 and c<=3:
    
        if g[l][c] == j and g[l][c] == g[l+1][c+1] and g[l][c] == g[l+2][c+2] and g[l][c] == g[l+3][c+3]:
                return True

        if g[l][c] == j and g[l][c] == g[l+1][c-1] and g[l][c] == g[l+2][c-2] and g[l][c] == g[l+3][c-3]:
                return True
                        
    if l>=3 and c<=3 and c>=3:                    
        
        if g[l][c] == j and g[l][c] == g[l-1][c-1] and g[l][c] == g[l-2][c-2] and g[l][c] == g[l-3][c-3]:
                return True
                
        if g[l][c] == j and g[l][c] == g[l-1][c+1] and g[l][c] == g[l-2][c+2] and g[l][c] == g[l-3][c+3]:
                return True
                        
    return False
    

##############################################

def victoire(g,j):
    """
    Fonction qui renvoie un booléen pour dire si le joueur j a gagné
    """
    for i in range(len(g)):
            for k in range(len(g[i])):
                if horiz(g,j,i,k) or vert(g,j,i,k) or diag(g,j,i,k):
                    return True
    return False
    
##############################################

def match_nul(g):
    """
    Fonction qui renvoie un booléen pour dire si toute la grille est remplie et qu'il n'y a pas eu de victoire
    """
    for i in range(len(g[5])):
        if g[5][i]==0:
            return False
            
    return True

##############################################

def coup_aleatoire(g,j):
    """
    Fonction qui renvoie une grille après qu'on ai mit un jeton dans une colonne aléatoire où il est possible de jouer
    """
    from random import randint
    while True:
        c = randint(0,6)
        if coup_possible(g,c):
            g = jouer(g,j,c)
            return g

##############################################

def IA_versus_IA():
    """
    Jeu du puissance 4 automatisé faisant un 1 contre 1 de BOT
    """
    joueur_un = 1
    joueur_deux = 2
    g = grille_vide()
    j = joueur_un
    
    while not victoire(g,j) and not match_nul(g):
        if j == joueur_un:
            j = joueur_deux
        else:
            j = joueur_un
        
        g = coup_aleatoire(g,j)
        print("=======================")
        affiche(g)
        
        
            
    if victoire(g,j):
        print("=======================")
        print("Le joueur",j,"a gagné !")
        print("=======================")
    else:
        print("=======================")
        print("EGALITE")
        print("=======================")
   
##############################################
            
def un_versus_IA():
    """
    Jeu du puissance 4 automatisé faisant un 1 contre 1 contre un BOT
    """
    joueur_un = 1
    BOT = 2
    g = grille_vide()
    j = joueur_un
    
    while not victoire(g,j) and not match_nul(g):
        
        if j == joueur_un:
            c = int(input("Quelle colonne (elles sont de 0 à 6) ?"))
            g = jouer(g,j,c)
            j = BOT
            
        else:
            g = coup_aleatoire(g,j)
            j = joueur_un
            
        print("=======================")    
        affiche(g)
        
        
        
    if victoire(g,j):
        print("=======================")
        print("Le joueur",j,"a gagné !")
        print("=======================")
    else:
        print("=======================")
        print("EGALITE")
        print("=======================")

            
        

            


