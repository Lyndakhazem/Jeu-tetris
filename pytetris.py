import modele
import vue
import time

    
class Controleur:
    
    def __init__(self,mod):
        self.__tetris = mod
        #creation d une instance de la class Vuetetris
        self.__vue = vue.VueTetris(self.__tetris)
        #recuperation de la fenetre Tk (la fenetre du jeu )
        self.__fen = self.__vue.fenetre()
        #le lien pour le deplacement a gauche (on doit faire le lien entre la touche (la fenetre) et la fonction a gauche du modele
        self.__fen.bind("<Key-Left>",self.forme_a_gauche)
        #le lien pour le deplacement a droite
        self.__fen.bind("<Key-Right>",self.forme_a_droite) #on ferme la fonction sans () car avec bind la fonction a_gauche ne prend pas de parametre
        #pour deplacer la forme plus vite vers le bas
        self.__fen.bind("<Key-Down>",self.forme_tombe)
        #pour deplacer la forme directement en bas (vitesse max) en cliquant sur space (espace)
        self.__fen.bind("<space>",self.forme_tombe2)
        #enter pour commencer, pause,recommencer,reprendre
        self.__fen.bind("<Return>",self.change_etat_jeu)
        #pour tourner la forme
        self.__fen.bind("<Key-Up>",self.forme_tourne)
        self.__delai = 300 #l'ecart entre chaque carre quand la forme tombe (la vitesse)
        self.__delai1 = 300
        #dessiner la forme courante par la vue
        self.__vue.dessine_forme(self.__tetris.get_coords_forme(),self.__tetris.get_couleur_forme())
        self.joue()
        #lancer la boucle d ecoute des evenements
        self.__fen.mainloop()
        
    def etat(self):
        return self.__vue.etat()
    
    def joue(self) :
        '''Controleur -> None
        boucle principale du jeu. Fait tomber une forme d’une ligne.
        '''
        if not self.__tetris.fini():
            self.affichage()
            self.__fen.after(self.__delai,self.joue)
            
        else:
            self.__vue.change_etat()
            self.__vue.retourne_btn()[0]["text"]="Recommencer"
            self.__vue.game()
            self.__tetris=self.__tetris.reinitialisation()
            self.__vue.reinitialisation(self.__tetris)
            self.joue()
                
    def affichage(self):
        if self.__vue.etat():
            self.__vue.game()
            self.__vue.dessine_forme_suivante(self.__tetris.get_coords_suivante(),self.__tetris.get_couleur_suivante())
            #demander au modele de faire tomber la forme
            boolean = self.__tetris.forme_tombe() #boulean pour recuperer le boolean
            #retourne par la fonction forme tombe
            #si la forme est tombee et il y a eu collision et s est pose on initialise le delai (la vitesse)
            if boolean: #true donc y a collision donc la forme s est pose
                self.__delai = 300
                self.__vue.dessine_forme_suivante(self.__tetris.get_coords_suivante(),self.__tetris.get_couleur_suivante())
        #demande a la vue de redessiner le terrain
            self.__vue.dessine_terrain()
        #demande a la vue de redessiner la forme
            self.__vue.dessine_forme(self.__tetris.get_coords_forme(),self.__tetris.get_couleur_forme())
        
            self.__vue.met_a_jour_score(self.__tetris.get_score())
        
    def forme_a_gauche(self,event):
        '''Controleur,event-> none
        demande au modele de deplacer la forme a gauche'''
        self.__tetris.forme_a_gauche()
      
    def forme_a_droite(self,event):
        '''Controleur,event-> none
        demande au modele de deplacer la forme a droite'''
        self.__tetris.forme_a_droite()
        
    def forme_tombe(self,event):
        '''Controleur,event ->none
        modifie la valeur de l'attribut self.__delai
        pour augumenter la vitesse'''
        self.__delai = 100
    
    def forme_tombe2(self,event):
        '''Controleur,event ->none
        modifie la valeur de l'attribut self.__delai
        pour faire tomber la forme directement la vitesse au maximum'''
        self.__delai = 0
        
    def forme_tourne(self,event):
        '''Controleur ,event ->none
        demande au modele de faire tourner la forme'''
        self.__tetris.forme_tourne()
        
    def change_etat_jeu(self,event):
        '''juste pour le boutton return'''
        self.__vue.met_a_jour_btn()
        
        
if __name__ == "__main__" :
    # creation du modele
    tetris = modele.ModeleTetris()
    # creation du contrˆoleur. c’est lui qui cree la vue
    # et lance la boucle d’´ecoute des ´evts
    ctrl = Controleur(tetris)