"""module principal"""
import pygame
from random import*
from math import*



"""Couleurs RGB"""
NOIR = (152, 151, 153)
BLANC = (255, 255, 255)
CYAN = (15, 240, 254)


"""Taille de la fenêtre"""


LARGEUR = 900
HAUTEUR = 600
"""Liste pour stocker le score de chaque jeu"""
L_scores=[]

"""Initalisations des modules de pygame"""
pygame.init()
"""Inialisation du module qui permet d'avoir du son"""
pygame.mixer.init()
"""Creation de la fenêtre"""
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
"""Nom de la fenêtre"""
pygame.display.set_caption('Pong')
"""Sauvegarde de l'image de l'arrière-plan"""
bg = pygame.image.load("Background3.jpg")

"""Sauvegarde des polices d'écriture"""
font_mm = pygame.font.Font(r'8-bit Arcade In.ttf', 45)
font_mm2 = pygame.font.Font(r'8-bit Arcade In.ttf', 20)


class Raquette:
#Creation de la classe raquette  
    def __init__(self, x_raquette, y_raquette):
        """Initialisations de la raquette et ses proprietés"""
        self.x_raquette = x_raquette
        self.y_raquette = y_raquette
        self.largeur_raq = 100
        self.hauteur_raq = 10
        self.deplacement_raq = 0
        self.dir=1
        self.rect_raquette = pygame.Rect(x_raquette, y_raquette, self.largeur_raq, self.hauteur_raq)

    def afficher(self):
        """Afichage de la raquette dans la fenêtre"""
        pygame.draw.rect(fenetre, BLANC, self.rect_raquette)

    def actualiser(self):
        """Deplacement de la raquette et vérification qu'elle reste aux limites de la fenêtre"""
        self.x_raquette += self.deplacement_raq
        # Assurer que la raquette reste dans les limites de la fenêtre
        self.x_raquette = max(0, min(self.x_raquette, LARGEUR - self.largeur_raq))
        self.rect_raquette = pygame.Rect(self.x_raquette, self.y_raquette, self.largeur_raq, self.hauteur_raq)

"""Mise en fenêtre de la raquette"""
raquette_joueur = Raquette(HAUTEUR - 30, 450)



    

class Balle:
    #Creation de la classe balle
    
    def __init__(self, x_balle, y_balle):
        """Initialisation de la balle et ses proprietés"""
        self.x_balle = x_balle
        self.y_balle = y_balle
        self.rayon_balle = 10
        self.couleur = BLANC
        self.vitesse = 8
        self.x_direction = 1
        self.y_direction = 1

    def afficher(self):
        """Affichage de la balle"""
        return pygame.draw.circle(fenetre, self.couleur, (self.x_balle, self.y_balle), self.rayon_balle)
      
      
    def auto_play(self):
        """Jeu automatique"""
        if raquette_joueur.dir==1:
            raquette_joueur.deplacement_raq =  self.vitesse
            raquette_joueur.x_raquette=self.x_balle-45
        else:
            raquette_joueur.deplacement_raq =  -self.vitesse
            raquette_joueur.x_raquette=self.x_balle-55
            
        
            
            
    
        
     
        

    def actualiser(self):
        """Paramètres pour le déplacement et barrières de la balle"""
        
        self.x_balle += self.vitesse * self.x_direction
        self.y_balle += self.vitesse * self.y_direction
        


        if self.y_balle - self.rayon_balle <= 0:
            self.y_direction = -self.y_direction
            if game_mode1 or game_mode3:
                pygame.mixer.music.load('Wall_sound.mp3')
                pygame.mixer.music.play() 
        elif self.y_balle + self.rayon_balle >= HAUTEUR:
            self.reinitialiser_jeu()
        if self.x_balle - self.rayon_balle*2 <= 0 or self.x_balle + self.rayon_balle*2 >= LARGEUR:
            self.x_direction = -self.x_direction
            if self.x_balle + self.rayon_balle*2 >= LARGEUR:
               raquette_joueur.dir=-1
            elif self.x_balle - self.rayon_balle<= 0:
                raquette_joueur.dir=1
            if game_mode1 or game_mode3:
                pygame.mixer.music.load('Wall_sound.mp3')
                pygame.mixer.music.play() 
            
           
           

    def reinitialiser_jeu(self):
        """Réinitialisation du jeu"""
        pygame.mixer.music.load('End_of_game.mp3')
        pygame.mixer.music.play()  
        if game_mode1:
            global game_end
            game_end=True
        elif game_mode3:
            global game_end3
            game_end3=True
        raquette_joueur.x_raquette=550
        self.vitesse = 8
        self.x_balle = LARGEUR // 2
        self.y_balle = HAUTEUR // 2
        self.x_direction = 1
        self.y_direction = 1
        global score  # Accéder à la variable globale du score
        global H_score
        L_scores.append(score)
        score = 0  # Réinitialiser le score
        H_score = max(L_scores)
        if game_mode3:   
            b1= Balle(LARGEUR // 2, HAUTEUR // 2)
            b2 = Balle(LARGEUR // 2+50, HAUTEUR // 2)
            b3 = Balle(LARGEUR // 2-50, HAUTEUR // 2)
            b4 = Balle(LARGEUR // 2+randint(-100,100), HAUTEUR // 2)
            b5 = Balle(LARGEUR // 2+randint(-200,200), HAUTEUR // 2)
            b6 = Balle(LARGEUR // 2+randint(-200,200), HAUTEUR // 2+randint(-300,50))
            score_txt=0
            b_c=0
            n=0
            L_B=[b1,b2,b3,b4,b5,b6]

            
        
        
        
class Triangle:
    #Création de la classe Triangle
    def __init__(self, x_triangle, y_triangle,sommets):
        #"""Initialisation de la classe triangle""
        self.x_triangle=x_triangle
        self.y_triangle=y_triangle
        self.couleur=BLANC
        self.sommets=sommets
        self.game_mode=0

        
    def afficher(self):
        """affichage du triangle"""
        return pygame.draw.polygon(fenetre, self.couleur, self.sommets)
    
    def deplacement(self,y_offset):
        """déplacement du triangle pour choisir un mode de jeu"""
        sommets=self.sommets
        if y_offset<0:
            self.game_mode-=1
        else:
            self.game_mode+=1
        for i in range(3):
            sommets[i]=(sommets[i][0],sommets[i][1]+y_offset)
        return pygame.draw.polygon(fenetre, self.couleur, self.sommets)
    
    
class Raquette_H:
    #création de la classe raquette horizontale
    def __init__(self, x_raquette_H, y_raquette_H):
        """Initialisations de la raquette et ses proprietés"""
        self.x_raquette_H = x_raquette_H
        self.y_raquette_H = y_raquette_H
        self.largeur_raq_H = 10
        self.hauteur_raq_H = 100
        self.deplacement_raq_H = 0
        self.dir_H=1
        self.rect_raquette_H = pygame.Rect(x_raquette_H, y_raquette_H, self.largeur_raq_H, self.hauteur_raq_H)

    def afficher(self):
        """Afichage de la raquette dans la fenêtre"""
        pygame.draw.rect(fenetre, BLANC, self.rect_raquette_H)

    def actualiser(self):
        """Déplacement de la raquette et vérification qu'elle reste aux limites de la fenêtre"""
        self.y_raquette_H += self.deplacement_raq_H
        # Assurer que la raquette reste dans les limites de la fenêtre
        self.y_raquette_H = max(0, min(self.y_raquette_H, HAUTEUR - self.hauteur_raq_H))
        self.rect_raquette_H = pygame.Rect(self.x_raquette_H, self.y_raquette_H, self.largeur_raq_H, self.hauteur_raq_H)
"""Instance de la classe Raquette_H"""   
raquette_joueur1_H = Raquette_H(40, HAUTEUR // 2)
raquette_joueur2_H = Raquette_H(LARGEUR-40, HAUTEUR // 2)

"""Score de chaque joueur pour le mode 2"""
score2j1=0
score2j2=0

class Balle_H:
    #Creation de la classe Balle Horizontalle
    
    def __init__(self, x_balle_H, y_balle_H):
        """Initialisation de la balle et ses proprietes"""
        self.x_balle_H = x_balle_H
        self.y_balle_H = y_balle_H
        self.rayon_balle_H = 10
        self.couleur_H = BLANC
        self.vitesse_H = 10
        self.x_direction_H = -1
        self.y_direction_H = 1

    def afficher(self):
        """Affichage de la balle"""
        return pygame.draw.circle(fenetre, self.couleur_H, (self.x_balle_H, self.y_balle_H), self.rayon_balle_H)
      
          

    def actualiser(self):
        """Parametres pour le deplacement et barriers de la balle"""
        
        self.x_balle_H += self.vitesse_H * self.x_direction_H
        self.y_balle_H += self.vitesse_H * self.y_direction_H
        

        if self.x_balle_H + self.rayon_balle_H>=LARGEUR:
            global score2j1
            score2j1 += 1
            self.reinitialiser_jeu()
            if game_mode2:
                pygame.mixer.music.load('Wall_sound.mp3')
                pygame.mixer.music.play()  
        elif self.x_balle_H<=0 :
            global score2j2
            score2j2 += 1
            self.reinitialiser_jeu()
        if self.y_balle_H - self.rayon_balle_H <= 0 or self.y_balle_H + self.rayon_balle_H>=HAUTEUR :
            if self.y_balle_H + self.rayon_balle_H>=HAUTEUR:
               self.y_balle_H= HAUTEUR-10
            else:
                self.y_balle_H= 10
            self.y_direction_H = -self.y_direction_H
            if game_mode2:
                pygame.mixer.music.load('Wall_sound.mp3')
                pygame.mixer.music.play()  
            
           
           

    def reinitialiser_jeu(self):
        """Reinitialisation du jeu"""
        pygame.mixer.music.load('End_of_game.mp3')
        pygame.mixer.music.play()  
        self.y_direction_H= 1
        self.vitesse_H = 8
        self.x_balle_H = LARGEUR // 2
        self.y_balle_H = HAUTEUR // 2
        raquette_joueur1_H.y_raquette_H=HAUTEUR // 2
        raquette_joueur2_H.y_raquette_H=HAUTEUR // 2
        L=[-1,1]
        self.x_direction_H=choice(L)
        self.y_direction_H=choice(L)
        
        


def line():
    """Affichage d'une ligne horizontale au milieu de la fenêtre"""
    L=[]
    for i in range(20):
        L.append((LARGEUR//2, i*30+30))   
    pygame.draw.lines(fenetre, BLANC ,True ,L,width=4)
    
    

    

        
    

        

# Création des objets 

triangle=Triangle(0,0,[(180, 385), (180, 415), (210, 400)])
game_mode1 = False
game_mode2= False
game_mode3 = False
score = 0
H_score=0
mm=True
game_end=False
game_end2=False
game_end3=False
game_on = True
"""Variables du chronomètre"""
n=0
n1=0
n2=0
"""Variable pour afficher le score à la fin du jeu"""
score_txt=0



# Boucle principal pour afficher le menu du jeu
while game_on:
    
    pygame.mixer.music.load('mihele 2.mp3')
    pygame.mixer.music.play(-1) 
    while mm:
        H_score=0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                mm = False
                game_on = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    mm=False
                    game_mode1=True
                if event.key == pygame.K_DOWN and triangle.game_mode<2:
                    triangle.deplacement(60)
                elif event.key == pygame.K_UP and triangle.game_mode>0:
                    triangle.deplacement(-60)
                if event.key == pygame.K_RETURN and triangle.sommets == [(180, 385), (180, 415), (210, 400)]:
                    mm=False
                    game_mode1=True
                elif event.key == pygame.K_RETURN and triangle.sommets == [(180, 445), (180, 475), (210, 460)]:
                    mm=False
                    game_mode2=True
                elif event.key == pygame.K_RETURN and triangle.sommets == [(180, 505), (180, 535), (210, 520)]:
                    mm=False
                    game_mode3=True
                    
                    

            
                    
                

        
       
        # Dessiner les objets
        fenetre.fill(NOIR)  # It is mandatory to have a backround, if not the  moving things will stretch
        fenetre.blit(bg, (0, 0))
        triangle.afficher()
        
        
        
        texte_mm = font_mm.render('NEW GAME', True, BLANC)
        fenetre.blit(texte_mm, ((LARGEUR // 2)-240 , (HAUTEUR//2)-130))
         
        texte_mm_d = font_mm2.render('SELECT A GAME MODE', True, BLANC)
        fenetre.blit(texte_mm_d, ((LARGEUR // 2)-225 , (HAUTEUR//2)-50))
        
        texte_mm_m1 = font_mm2.render('CLASSIC MODE', True, BLANC)
        fenetre.blit(texte_mm_m1, (300 , 380))
        
        texte_mm_m2 = font_mm2.render('TWO PLAYER GAME', True, BLANC)
        fenetre.blit(texte_mm_m2, (270 , 440))
        
        texte_mm_m3 = font_mm2.render('SPECIAL MODE', True, BLANC)
        fenetre.blit(texte_mm_m3, (300 , 500))
        
        n1+=1

        pygame.display.update()
        pygame.time.Clock().tick(30)
     
    if game_mode1:
        raquette_joueur = Raquette(HAUTEUR - 30, 450)
        balle = Balle(LARGEUR // 2, HAUTEUR // 2)
        
        
    while game_mode1:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_mode1 = False
                game_on=False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    raquette_joueur.deplacement_raq = -15
                elif event.key == pygame.K_RIGHT:
                    raquette_joueur.deplacement_raq = 15
            elif event.type == pygame.KEYUP:
                raquette_joueur.deplacement_raq = 0
            

                

        
        # Vérifier la collision avec la raquette
        if pygame.Rect.colliderect(balle.afficher(), raquette_joueur.rect_raquette) and (raquette_joueur.x_raquette<=balle.x_balle+balle.rayon_balle<=raquette_joueur.x_raquette+110 or raquette_joueur.x_raquette<=balle.x_balle-balle.rayon_balle<=raquette_joueur.x_raquette+100) and balle.y_balle<=raquette_joueur.y_raquette:
            pygame.mixer.music.load('Colision_Sound.mp3')
            pygame.mixer.music.play() 
            if balle.vitesse>25:
                balle.vitesse+=0.25
            else:
                balle.vitesse+=0.5
            balle.vitesse=min(55,balle.vitesse) 
            balle.y_direction = -balle.y_direction+random()/100
            score += 1
            score_txt=score

        

        
                


        # Mettre à jour les objets
        raquette_joueur.actualiser()
        balle.actualiser()
        
        
        
        # Dessiner les objets
        fenetre.fill(NOIR)  # It is mandatory to have a backround, if not the  moving things will stretch
        fenetre.blit(bg, (0, 0))
        balle.afficher()
        raquette_joueur.afficher()
        

        # Afficher le score
        fonte = pygame.font.Font(r"8-bit Arcade In.ttf", 15)
        texte_score = fonte.render('SCORE  ' + str(score), True, BLANC)
        fenetre.blit(texte_score, ((LARGEUR // 2) - 100, 0))
        
        #afficher le meilleur score
        Highscore = pygame.font.Font(r"8-bit Arcade In.ttf", 15)
        texte_timer = fonte.render('BEST  '+str(H_score), True, BLANC)
        fenetre.blit(texte_timer, ((LARGEUR-165),0))

        pygame.display.update()
        pygame.time.Clock().tick(30)
        
        if game_end:
            pygame.mixer.music.load('mihele 3.mp3')
            pygame.mixer.music.play(-1) 
        #boucle du menu du fin de jeu
        while game_end:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_end = False
                    game_mode1=False
                    game_on=False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        game_end = False
                elif event.type == pygame.MOUSEBUTTONDOWN :
                    mouse_pos = pygame.mouse.get_pos()
                    if 700 <= mouse_pos[0] <= 900 and 0 <= mouse_pos[1] <= 30:
                        game_end = False
                        game_mode1 = False
                        mm = True
                        L_scores = []
                        score = 0
                        raquette_joueur = Raquette(HAUTEUR - 30, LARGEUR // 2)
                        balle = Balle(LARGEUR // 2, HAUTEUR // 2)
                                    
            fenetre.fill(NOIR)  # It is mandatory to have a backround, if not the  moving things will stretch
            fenetre.blit(bg, (0, 0))

            texte_mm = font_mm.render('GAME OVER', True, BLANC)
            fenetre.blit(texte_mm, ((LARGEUR // 2)-275 , (HAUTEUR//2)-100))
            
            fonteS = pygame.font.Font(r"8-bit Arcade In.ttf", 17)
            texte_mms=fonteS.render('YOUR SCORE  '+str(score_txt), True, BLANC)
            fenetre.blit(texte_mms, ((LARGEUR // 2)-150 , (HAUTEUR//2)-10))
                
            texte_mmbs=fonteS.render('BEST SCORE  '+str(H_score), True, BLANC)
            fenetre.blit(texte_mmbs, ((LARGEUR // 2)-150 , (HAUTEUR//2)+37))
            
            texte_mm_d = font_mm2.render('PRESS SPACE TO RESTART', True, BLANC)
            fenetre.blit(texte_mm_d, ((LARGEUR // 2)-295 , (HAUTEUR//2)+80))
            
            texte_mm_mm = fonteS.render('MAIN MENU', True, BLANC)
            fenetre.blit(texte_mm_mm, (LARGEUR-220 , 0))
                    
            pygame.display.update()
            pygame.time.Clock().tick(30)

            
    if game_mode2:
        raquette_joueur1_H = Raquette_H(30, HAUTEUR // 2)
        balle_H =  Balle_H(LARGEUR // 2, HAUTEUR // 2)
        raquette_joueur2_H = Raquette_H(LARGEUR-40, HAUTEUR // 2)
        balle_H.vitesse_H = 8
    
        
    while game_mode2:
        
        if score2j1==11  or  score2j2==11:
            game_mode2=False
            game_end2=True
            
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_mode2 = False
                game_on=False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    raquette_joueur1_H.deplacement_raq_H = -30
                elif event.key == pygame.K_s:
                    raquette_joueur1_H.deplacement_raq_H = 30
                elif event.key == pygame.K_UP:
                    raquette_joueur2_H.deplacement_raq_H = -30
                elif event.key == pygame.K_DOWN:
                    raquette_joueur2_H.deplacement_raq_H = 30
            elif event.type == pygame.KEYUP:
                raquette_joueur1_H.deplacement_raq_H = 0
                raquette_joueur2_H.deplacement_raq_H = 0
            
                
                
        
        
        if pygame.Rect.colliderect(balle_H.afficher(), raquette_joueur1_H.rect_raquette_H):
            pygame.mixer.music.load('Colision_Sound.mp3')
            pygame.mixer.music.play()  
            if raquette_joueur1_H.y_raquette_H+40<=balle_H.y_balle_H<=raquette_joueur1_H.y_raquette_H+50:
               balle_H.y_direction_H *= 0.5
               balle_H.x_direction_H = 1.2
               
            elif raquette_joueur1_H.y_raquette_H+50<=balle_H.y_balle_H<=raquette_joueur1_H.y_raquette_H+60:
               balle_H.y_direction_H *= -0.5
               balle_H.x_direction_H = 1.2
               
            elif raquette_joueur1_H.y_raquette_H+20<balle_H.y_balle_H<=raquette_joueur1_H.y_raquette_H+50:
               balle_H.y_direction_H *= 0.8
               balle_H.x_direction_H = 1.4
               
            
            elif raquette_joueur1_H.y_raquette_H+60<balle_H.y_balle_H<=raquette_joueur1_H.y_raquette_H+80:
               balle_H.y_direction_H *= -0.8
               balle_H.x_direction_H = 1.4
               
                
            elif raquette_joueur1_H.y_raquette_H+20>=balle_H.y_balle_H:
               balle_H.y_direction_H = -1-random()/100
               balle_H.x_direction_H = 1
               
            else:
                balle_H.y_direction_H = 1+random()/100
                balle_H.x_direction_H = 1
                
            balle_H.vitesse_H=min(25,balle_H.vitesse_H+1)
            
               
        if pygame.Rect.colliderect(balle_H.afficher(), raquette_joueur2_H.rect_raquette_H):
            pygame.mixer.music.load('Colision_Sound.mp3')
            pygame.mixer.music.play()  
            if raquette_joueur2_H.y_raquette_H+40<=balle_H.y_balle_H<=raquette_joueur2_H.y_raquette_H+50:
               balle_H.y_direction_H *= -0.5
               balle_H.x_direction_H = -1.2
            
            elif raquette_joueur2_H.y_raquette_H+50<=balle_H.y_balle_H<=raquette_joueur2_H.y_raquette_H+60:
               balle_H.y_direction_H *= 0.5
               balle_H.x_direction_H = -1.2
               
            elif raquette_joueur2_H.y_raquette_H+20<balle_H.y_balle_H<=raquette_joueur2_H.y_raquette_H+50:
               balle_H.y_direction_H *= -0.8
               balle_H.x_direction_H = -1.4
               
            
            elif raquette_joueur2_H.y_raquette_H+60<balle_H.y_balle_H<=raquette_joueur2_H.y_raquette_H+80:
               balle_H.y_direction_H *= 0.8
               balle_H.x_direction_H = -1.4
               
                
            elif raquette_joueur2_H.y_raquette_H+20>=balle_H.y_balle_H:
               balle_H.y_direction_H = -1-random()/100
               balle_H.x_direction_H = -1
               
            else:
                balle_H.y_direction_H = 1+random()/100
                balle_H.x_direction_H = -1
                
            balle_H.vitesse_H=min(25,balle_H.vitesse_H+1)
            
            
            
        
            
            
        

        
        
        raquette_joueur1_H.actualiser()
        raquette_joueur2_H.actualiser()
        balle_H.actualiser()
        
        
        
        
        # Dessiner les objets
        fenetre.fill(NOIR)  # It is mandatory to have a backround, if not the  moving things will stretch
        fenetre.blit(bg, (0, 0))
        raquette_joueur1_H.afficher()
        raquette_joueur2_H.afficher()
        balle_H.afficher()
        if n2>30:
            line()
    
       
       

        # Afficher le score
        fonte = pygame.font.Font(r"8-bit Arcade In.ttf", 15)
        texte_score = fonte.render('SCORE  ' + str(score2j1)+" - "+str(score2j2), True, BLANC)
        fenetre.blit(texte_score, ((LARGEUR // 2) - 100, 0))
        
        if n2<30:
            fonteT = pygame.font.Font(r"8-bit Arcade In.ttf", 17)
            texte_t=fonteT.render('FIRST TO 11 WINS', True, BLANC)
            fenetre.blit(texte_t, ((LARGEUR // 2)-150 , (HAUTEUR//2)-10))
        
        
        
        n2+=1
        pygame.display.update()
        pygame.display.flip()
        pygame.time.Clock().tick(30)
        if game_end2:
           pygame.mixer.music.load('mihele 3.mp3')
           pygame.mixer.music.play(-1)  
           
           
        while game_end2:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_end2 = False
                    game_mode2=False
                    game_on=False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        score2j1=0
                        score2j2=0
                        game_end2 = False
                        game_mode2 = True
                        raquette_joueur1_H = Raquette_H(30, HAUTEUR // 2)
                        balle_H =  Balle_H(LARGEUR // 2, HAUTEUR // 2)
                        raquette_joueur2_H = Raquette_H(LARGEUR-30, HAUTEUR // 2)
                elif event.type == pygame.MOUSEBUTTONDOWN :
                    mouse_pos = pygame.mouse.get_pos()
                    if 700 <= mouse_pos[0] <= 900 and 0 <= mouse_pos[1] <= 30:
                        game_end2 = False
                        game_mode2 = False
                        mm = True
                        L_scores = []
                        score = 0
                        raquette_joueur_H = Raquette_H(30, LARGEUR // 2)
                        balle_H = Balle_H(LARGEUR // 2, HAUTEUR // 2)
                        score2j1=0
                        score2j2=0
                                    
            fenetre.fill(NOIR)  # It is mandatory to have a backround, if not the  moving things will stretch
            fenetre.blit(bg, (0, 0))

            texte_mm = font_mm.render('GAME OVER', True, BLANC)
            fenetre.blit(texte_mm, ((LARGEUR // 2)-275 , (HAUTEUR//2)-100))
            
            fonteS = pygame.font.Font(r"8-bit Arcade In.ttf", 17)
            texte_mms=fonteS.render('YOUR SCORE  '+str(score2j1)+" - "+str(score2j2), True, BLANC)
            fenetre.blit(texte_mms, ((LARGEUR // 2)-150 , (HAUTEUR//2)-10))
            
            if score2j1>score2j2:
                RES = pygame.font.Font(r"8-bit Arcade In.ttf", 17)
                texte_res=RES.render('PLAYER ONE WINS', True, BLANC)
                fenetre.blit(texte_res, ((LARGEUR // 2)-155 , (HAUTEUR//2)+35))
                
            else:
                RES = pygame.font.Font(r"8-bit Arcade In.ttf", 17)
                texte_res=RES.render('PLAYER TWO WINS', True, BLANC)
                fenetre.blit(texte_res, ((LARGEUR // 2)-155 , (HAUTEUR//2)+35))
                
            
                
            
            texte_mm_d = font_mm2.render('PRESS SPACE TO RESTART', True, BLANC)
            fenetre.blit(texte_mm_d, ((LARGEUR // 2)-295 , (HAUTEUR//2)+80))
            
            texte_mm_mm = fonteS.render('MAIN MENU', True, BLANC)
            fenetre.blit(texte_mm_mm, (LARGEUR-220 , 0))
                    
            pygame.display.update()
            pygame.time.Clock().tick(30)
            
            
            
            
        
        
        
    if game_mode3:   
        raquette_joueur = Raquette(HAUTEUR - 30, 450)
        b1= Balle(LARGEUR // 2, HAUTEUR // 2)
        b6 = Balle(LARGEUR // 2+randint(-200,200), HAUTEUR // 2+randint(-300,50))
        b5 = Balle(LARGEUR // 2+randint(-200,200), HAUTEUR // 2+randint(-300,50))
        b4 = Balle(LARGEUR // 2+randint(-100,100), HAUTEUR // 2)
        b3 = Balle(LARGEUR // 2+randint(-200,200), HAUTEUR // 2)
        b2 = Balle(LARGEUR // 2+randint(-200,200), HAUTEUR // 2+randint(-300,50))
        score_txt=0
        b_c=0
        n=0
        L_B=[b1,b2,b3,b4,b5,b6]
        L_D=[-1,1]
        for balle in L_B[1:]:
            balle.y_direction +=randint(0,1)/10+0.000001
            balle.y_direction =-1
            balle.x_direction *=choice(L_D)
            balle.vitesse=6
            
        
        
    while game_mode3:
        
        if n%300==0 and b_c<4:
            b_c+=1
            n=0
        elif n%600==0 and 4<=b_c<6:
            b_c+=1
            n=0
        
            
                
            
                
            
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_mode3 = False
                game_on=False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                        raquette_joueur.deplacement_raq = -25  
                elif event.key == pygame.K_RIGHT:
                        raquette_joueur.deplacement_raq = 25
            elif event.type == pygame.KEYUP:
                raquette_joueur.deplacement_raq = 0
                

                

            
            # Vérifier la collision avec la raquette
        for ballec in L_B[:b_c]:
            if pygame.Rect.colliderect(ballec.afficher(), raquette_joueur.rect_raquette) and raquette_joueur.x_raquette<=ballec.x_balle+ballec.rayon_balle<=raquette_joueur.x_raquette+110 and ballec.y_balle<=raquette_joueur.y_raquette:
                pygame.mixer.music.load('Colision_Sound.mp3')
                pygame.mixer.music.play()  # Play the sound
                ballec.vitesse+=1
                ballec.vitesse=min(7,ballec.vitesse) 
                ballec.y_direction = -ballec.y_direction+random()/100
                score += 1
                score_txt=score


        
            
                    


            # Mettre à jour les objets
        raquette_joueur.actualiser()
        for balleact in L_B[:b_c]:
            balleact.actualiser()
            
            
            

            # Dessiner les objets
        
        fenetre.fill(NOIR)
        # It is mandatory to have a backround, if not the  moving things will stretch
        fenetre.blit(bg, (0, 0))
        for balleaf in L_B[:b_c]:
            balleaf.afficher()
        raquette_joueur.afficher()
        
        

            # Afficher le score
        fonte = pygame.font.Font(r"8-bit Arcade In.ttf", 15)
        texte_score = fonte.render('SCORE  ' + str(score), True, BLANC)
        fenetre.blit(texte_score, ((LARGEUR // 2) - 70, 0))
            
            #afficher le meilleur score
            
        Highscore = pygame.font.Font(r"8-bit Arcade In.ttf", 15)
        texte_s = fonte.render('BEST  '+str(H_score), True, BLANC)
        fenetre.blit(texte_s, ((LARGEUR-165),0))
        
        Timer=pygame.font.Font(r"8-bit Arcade In.ttf", 15)
        if b_c<4:
            timer_txt=round((300-n)/30,1)
        else:
            timer_txt=round((600-n)/30,1)
        texte_timer = fonte.render('NEXT BALL IN '+str(timer_txt), True, BLANC)
        fenetre.blit(texte_timer, ((10,0)))
        
        pygame.display.update()
        pygame.time.Clock().tick(30)
        n+=1
        

            
        
        
            #boucle du fin de jeu
        
        if game_end3:
            pygame.mixer.music.load('mihele 3.mp3')
            pygame.mixer.music.play(-1)  # Play the sound
            raquette_joueur = Raquette(HAUTEUR - 30, 450)
            b1= Balle(LARGEUR // 2, HAUTEUR // 2)
            b6 = Balle(LARGEUR // 2+50, HAUTEUR // 2)
            b5 = Balle(LARGEUR // 2-50, HAUTEUR // 2)
            b4 = Balle(LARGEUR // 2+randint(-100,100), HAUTEUR // 2)
            b3 = Balle(LARGEUR // 2+randint(-200,200), HAUTEUR // 2)
            b2 = Balle(LARGEUR // 2+randint(-200,200), HAUTEUR // 2+randint(-300,50))
            b_c=0
            n=0
            L_B=[b1,b2,b3,b4,b5,b6]
            for balle in L_B[1:]:
                balle.y_direction +=randint(0,1)/10+0.000001
                balle.y_direction =-1
                balle.vitesse=5
                
        while game_end3:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_end3 = False
                    game_mode3 = False
                    game_on=False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        game_end3 = False
                elif event.type == pygame.MOUSEBUTTONDOWN :
                    mouse_pos = pygame.mouse.get_pos()
                    if 700 <= mouse_pos[0] <= 900 and 0 <= mouse_pos[1] <= 30:
                        game_end3=False
                        game_mode3 = False
                        mm = True
                        L_scores = []
                        score = 0
                        raquette_joueur = Raquette(HAUTEUR - 30, LARGEUR // 2)
                        balle = Balle(LARGEUR // 2, HAUTEUR // 2)
                                    
            fenetre.fill(NOIR)  # It is mandatory to have a backround, if not the  moving things will stretch
            fenetre.blit(bg, (0, 0))

            texte_mm = font_mm.render('GAME OVER', True, BLANC)
            fenetre.blit(texte_mm, ((LARGEUR // 2)-275 , (HAUTEUR//2)-100))
            
            fonteS = pygame.font.Font(r"8-bit Arcade In.ttf", 17)
            texte_mms=fonteS.render('YOUR SCORE  '+str(score_txt), True, BLANC)
            fenetre.blit(texte_mms, ((LARGEUR // 2)-150 , (HAUTEUR//2)-10))
                
            texte_mmbs=fonteS.render('BEST SCORE  '+str(H_score), True, BLANC)
            fenetre.blit(texte_mmbs, ((LARGEUR // 2)-150 , (HAUTEUR//2)+37))
            
            texte_mm_d = font_mm2.render('PRESS SPACE TO RESTART', True, BLANC)
            fenetre.blit(texte_mm_d, ((LARGEUR // 2)-295 , (HAUTEUR//2)+80))
            
            texte_mm_mm = fonteS.render('MAIN MENU', True, BLANC)
            fenetre.blit(texte_mm_mm, (LARGEUR-220 , 0))
                    
            pygame.display.update()
            pygame.time.Clock().tick(30)
            
pygame.quit()





