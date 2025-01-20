import tkinter
import modele

##definition des constantes

DIM=30 # taille d'une cellule du tetris(un carree)
 #POUR LE PETIT TERRAIN A COTE

#définition des coulerus qui seront utiliser dans le jeu (9couleurs !=tes)
COULEURS= ["red","blue","green","yellow","orange","purple","pink","orchid","cyan","dark grey","black"]
SUIVANT = 7 #initialiser une valeur
#la classe vueTetris
class VueTetris:
    ''' cette class modelise tous ce qui est affichage et graphisme,la fenetre de
        de jeu c-a-d l'interface et le contact avec l'utilisateur '''
    
    def __init__(self,mod):
        ''' VueTetris,ModeleTetris -> VueTetris
            le constructeur de la classe de VueTetris prend en pamrametre une
            instance de la classe ModeleTetris ,
            elle construit le window principale(la fenetre) de l'application et
            toutes ses composantes.
        '''
        self.__etat=False
        self.__modele=mod
        #la fenetre principale de jeu
        self.__fen=tkinter.Tk()
        self.__fen.title("Tetris")
        # le canvas
        larg=self.__modele.get_largeur()*DIM #largeur de canvas
        haut=self.__modele.get_hauteur()*DIM # hauteur de canavas 
        self.__can_terrain=tkinter.Canvas(self.__fen,width=larg,height=haut)
        self.__can_terrain.pack(side="left")
        # mettre les objets dans une liste de liste 
        l=[]
        for i in range (self.__modele.get_hauteur()):
            l2=[]
            for j in range (self.__modele.get_largeur()):
                l2.append(self.__can_terrain.create_rectangle(j*DIM, i*DIM, (j+1)*DIM, (i+1)*DIM, fill=COULEURS[self.__modele.get_valeur(i,j)],outline=COULEURS[self.__modele.get_valeur(i,j)]))
            l.append(l2)
        
        self.__les_cases=l
        #le frame pour le boutoun quitter et les autres element...
        fr=tkinter.Frame(self.__fen)
        fr.pack(side="left")
        #boutton pour afficher le meilleur score ,ou game over ou bravo 
        self.__btn_game = tkinter.Label(fr,text="",fg="red")
        self.__btn_game.pack()
        lbl = tkinter.Label(fr,text="Forme suivante :",fg="black",bg="white")
        lbl.pack()
        self.__can_fsuivante =tkinter.Canvas(fr,width=SUIVANT*DIM,height=SUIVANT*DIM)
        self.__can_fsuivante.pack() #pour dessiner le petit terrain a cote
        liste=[]
        DIM2=30
        for i in range (SUIVANT):
            liste2=[]
            for j in range (SUIVANT):
                liste2.append(self.__can_fsuivante.create_rectangle(j*DIM2,i*DIM2,(j+1)*DIM2,(i+1)*DIM2,fill="black"))
            liste.append(liste2)
        self.__les_suivants =liste
        self.__lbl_score = tkinter.Label(fr,text="Score : 0",fg="gray")
        self.__lbl_score.pack()
        #boutton recommencer , reprend,restart,recommencer
        self.__btn_crpr=tkinter.Button(fr,text="Commencer",command=self.met_a_jour_btn)
        self.__btn_crpr.pack()
        btnquitter=tkinter.Button(fr,text="Au revoir",command=self.__fen.destroy)
        btnquitter.pack()
    
    def fenetre(self):
        ''' VueTetris -> retourne l'instance Tk de l'application'''
        return self.__fen
    
    def dessine_case(self,i,j,coul):
        ''' VueTetris ,int,int,int-> none
            elle remplit la case en ligne i et la colonne j de la couleur a l'indice
            coul
        '''
        self.__can_terrain.itemconfigure(self.__les_cases[i][j],fill=COULEURS[coul])
    
    def dessine_terrain(self):
        ''' VueTetris -> none
            elle mis a jour la couleur deu terrain en fonction des valeurs de modeles
        '''
        for i in range (len(self.__les_cases)):
            for j in range (len(self.__les_cases[i])):
                self.dessine_case(i,j,self.__modele.get_valeur(i,j))
    
    def dessine_forme(self,coords,couleur):
        ''' VueTetris ,list(int,int),int->none
            remplit de couleur les cases dont les coordonnees sont donnee dans coords
            elle permet de faire apparaitre une forme dans le terrain '''
        for tup in coords:
            self.dessine_case(tup[1],tup[0],couleur)
        
    def met_a_jour_score(self,val):
        '''change le texte de lbl_score pour afficher val dans le score'''
        self.__lbl_score["text"] = "score :" + str(val)
        
        
    def met_a_jour_btn(self):
        '''Elle met a jour le button commencer,pause,recommencer'''
        if self.__btn_crpr["text"]=="Commencer" or self.__btn_crpr["text"]=="Reprendre" or self.__btn_crpr["text"]=="Recommencer" :
            self.__btn_crpr["text"]="Pause"
            self.__etat=True
        else:
            self.__btn_crpr["text"]="Reprendre"
            self.__etat=False
            
    def retourne_btn(self):
        '''retourne le boutton commencer,reprendre,pause,recommencer'''
        return [self.__btn_crpr,self.__btn_game]
    
    def change_etat(self):
        '''VueTetris -> bool
        Change l etat du jeu false si il est en pause (les formes ne tombent pas)'''
        self.__etat=not(self.__etat)
             
    def etat(self):
        '''VueTetris -> bool
        Retourne l etat du jeu false si il est en pause (les formes ne tombent pas)'''
        return self.__etat
        
    def dessine_case_suivante(self,x,y,coul):
        '''VueTetris,int,int,int ->none
        fonctionne comme dessine case'''
        self.__can_fsuivante.itemconfigure(self.__les_suivants[x][y],fill=COULEURS[coul])

    def nettoie_forme_suivante(self):
        '''VueTetris ->none
        remet du noir sur tous les carres de can__fsuivante'''
        for i in range (len(self.__les_suivants)):
            for j in range (len(self.__les_suivants[i])):
                self.dessine_case_suivante(i,j,-1)
    
    def dessine_forme_suivante(self,coords,coul):
        '''VueTeteris,[(int,int)],int ->none
        dessine la forme suivante dont les coordonnees et la couleur sont donnees en parametre'''
        self.nettoie_forme_suivante()
        for tup in coords:
            self.dessine_case_suivante(tup[1]+3,tup[0]+3,coul)
            
    def reinitialisation(self,mod):
        '''VueTeteris->none
        remet en noir tous les carres de self.__terrain
        modifie le modele pour recommencer une nouvelle partie'''
        self.__modele = mod
        
    
    def game(self):
        if self.__modele.fini():
            self.__btn_game["text"]="Game Over"
        else:
            self.__btn_game["text"]=" "
            
        
        