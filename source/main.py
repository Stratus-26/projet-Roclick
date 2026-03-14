#Projet : Roclick
#Auteurs : Ibrahim Bilal, Flavio Bonnano, Antoine Kauffman, Rafael Kamacho
import pygame
pygame.init()
pygame.mixer.init()

#création et jeu musique
style=pygame.mixer.Sound('../data/musique et effet/force.mp3')
style.play(loops=-1)

#création de la page
screen1 = pygame.display.set_mode((960,500),pygame.SCALED)
#les différentes écritures
police1 = pygame.font.Font(None, 50)
font10=pygame.font.SysFont("Comic Sans ms",9)
#la variable pour que le programme reste ouvert
running1 = True

#Cette fonction permet d'écrire le texte voulu avec le texte, la police, la couleur de l'écriture et la position en x et y
def draw_text(text, font, text_col, x, y):
  img = font.render(text, True, text_col)
  screen1.blit(img, (x, y))

#l'animation d'ouverture
animation_frames1= []
for i in range(1,299):
    frame1 = pygame.image.load(f"../data/animation1/{i}.png").convert_alpha()
    animation_frames1.append(frame1)

animation_speed1 = 6
frame_counter1 = 0
animation1=True
animating1 = True
current_frame1 = 0

# le chargement des images
image1 = pygame.image.load("../data/Robot (1).png").convert_alpha()
start = pygame.image.load("../data/start_btn.png").convert_alpha()
background10 = pygame.image.load("../data/Ete fi.png").convert_alpha()

#la gestion de la fermeture de la page
while running1:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            #l'ouverture de la page principale
            if event.key == pygame.K_RETURN:
                running1 = False
                style.stop()
        if event.type == pygame.QUIT:
            running1 = False

#l'affichage de l'animation du début
    if animation1==True:
        if animating1==True:
            screen1.blit(animation_frames1[current_frame1], (0,0))

        frame_counter1 += 1
        if frame_counter1 >= animation_speed1:
            frame_counter1 = 0
            current_frame1 += 1

            if current_frame1 >= len(animation_frames1):
                animating1 = False


    #rafraichissement de la page + l'affichage des images
    pygame.display.flip()
    screen1.fill((160,195,195))
    screen1.blit(background10,(0,0))
    screen1.blit(image1,(150, 270))
    screen1.blit(start,(325, 155))

    #écriture
    draw_text("La bienvenue sur ROCLICK",police1,(255,255,255),240,80)
    draw_text("APPUYER SUR LA TOUCHE ENTRER",font10,(255,255,255),400,140)


#ouverture du programme principale
import pygame
import button

pygame.init()

aziz=0.5
#chargement des musiques et effect
pygame.mixer.init()
effect=pygame.mixer.Sound('../data/musique et effet/click-sound.mp3')


musique2=pygame.mixer.Sound('../data/musique et effet/aw2.mp3')
musique=pygame.mixer.Sound('../data/musique et effet/aw.mp3')
musique3=pygame.mixer.Sound('../data/musique et effet/aw3.mp3')
musique4=pygame.mixer.Sound('../data/musique et effet/aw4.mp3')
musique.play(loops=-1)
musique.set_volume(aziz)

clock = pygame.time.Clock()
#création de la page
screen = pygame.display.set_mode((960,500),pygame.SCALED)
# nomination de la page
pygame.display.set_caption("RoClick")
#les différentes écritures
font=pygame.font.SysFont("Comic Sans ms",9)
font2=pygame.font.SysFont("Comic Sans ms",14)
police = pygame.font.Font(None, 50)
#la variable pour que le programme reste ouvert
running = True
#le score qui va augmenté
score = 0
#la multiplication du score
multi = 1
#Les textes dans le mode histoires
texte1=True
texte2=False
texte3=True
texte4=True
texte5=True
#les boutons de multiplication
my_button_enabled=False
my_button_enabled1=False
#les variables pour le changement de fond d'écran
back0=True
back=False
back2=False
back3=False
#le nombre de score par clique
argent=100

#auto_click2=False

#C'est pour une gestion de menu de jeu
game_paused = False
menu_state = "main"
#une couleur que je vais utiliser par la suite
TEXT_COL = (255, 255, 255)




#chargement d'image
resume_img = pygame.image.load("../data/button_resume.png").convert_alpha()
options_img = pygame.image.load("../data/button_options.png").convert_alpha()
quit_img = pygame.image.load("../data/button_quit.png").convert_alpha()
video_img = pygame.image.load('../data/button_video.png').convert_alpha()
audio_img = pygame.image.load('../data/button_audio.png').convert_alpha()

back_img = pygame.image.load('../data/button_back.png').convert_alpha()

#création de bouton
resume_button = button.Button(365, 75, resume_img, 1)
options_button = button.Button(360, 300, options_img, 1)
quit_button = button.Button(400, 325, quit_img, 1)
video_button = button.Button(300, 75, video_img, 1)
audio_button = button.Button(300, 200, audio_img, 1)
back_button = button.Button(400, 325, back_img, 1)

#le commencement du timer dans le mode danger
start_time = pygame.time.get_ticks()
#variable du timer dans le mode danger
action_done = False
action_done1=False
action_done3=True
#Cette fonction permet d'écrire le texte voulu avec le texte, la police, la couleur de l'écriture et la position en x et y
def draw_text(text, font, text_col, x, y):
  img = font.render(text, True, text_col)
  screen.blit(img, (x, y))
#variable pour l'eau dans le mode danger
remplir1=True
remplir2=True
remplir3=True

#c'est une variable qui ne sert à rien
pas_argent=False
#variable pour les boutiques
boutique_ouverte=True
menu_boutique="tout"

#auto_click=False


#l'énoncé des questions
énoncé01="Quel est l'arbre le"
énoncé02="plus grand au monde?"
énoncé_rect=pygame.Rect((825,100),(100,32))

énoncé12="Les manchots sont des"
énoncé11="animaux qui ne peuvent pas voler"
énoncé10_rect=pygame.Rect((780,200),(150,31))

énoncé21="Quel est le plus grand océan "
énoncé22="de la planète en superficie ?"
énoncé20_rect=pygame.Rect((800,300),(150,31))

énoncé51="Les êtres vivants qui se nourrissent"
énoncé52="de végétaux et d’animaux sont…"

énoncé31="Comment appelle-t-on l’organe "
énoncé32="reproducteur mâle d’une fleur?"

énoncé42="Quel insecte était vénéré "
énoncé41="par les Égyptiens ?"

énoncé61="Quelle a été le permier"
énoncé62="message de l'informatique?"

énoncé72="Comment nomme-t-on "
énoncé71="le cri des éléphants?"

énoncé81="Quel pourcentage d’eau"
énoncé82="recouvre la planète Terre?"

énoncé91="Quelle est l'animal le plus"
énoncé92= "lourd de la Terre?"
énoncé_rect=pygame.Rect((820,100),(120,32))

énoncé102="Quelle la valeur décimale de"
énoncé101="ce nombre binaire: 01000011"
énoncé10_rect=pygame.Rect((820,200),(134,31))

énoncé111="Quelle est l'animal le plus"
énoncé112="rapide de la Terre?"
énoncé20_rect=pygame.Rect((820,300),(120,31))
#l'input du questionnaire
user_texte="insérer la réponse"
user_texte1="insérer la réponse"
user_texte2="insérer la réponse"
user_texte3="insérer la réponse"
user_texte4="insérer la réponse"
user_texte5="insérer la réponse"
user_texte6="insérer la réponse"
user_texte7="insérer la réponse"
user_texte8="insérer la réponse"
user_texte9="insérer la réponse"
user_texte10="insérer la réponse"
user_texte11="insérer la réponse"

#gestion des questions si elle est allumée
active=True
active1=True
active2=True
active3=True
active4=True
active5=True
active6=True
active7=True
active8=True
active9=True
active10=True
active11=True
#l'emplacement de l'input du questionnaire
input_rect=pygame.Rect((835,150),(14,32))
input_rect1=pygame.Rect((835,250),(14,32))
input_rect2=pygame.Rect((835,350),(14,32))
input_rect3=pygame.Rect((835,150),(14,32))
input_rect4=pygame.Rect((835,250),(14,32))
input_rect5=pygame.Rect((835,350),(14,32))
input_rect6=pygame.Rect((835,150),(14,32))
input_rect7=pygame.Rect((835,250),(14,32))
input_rect8=pygame.Rect((835,350),(14,32))
input_rect9=pygame.Rect((835,150),(14,32))
input_rect10=pygame.Rect((835,250),(14,32))
input_rect11=pygame.Rect((835,350),(14,32))




animation=True
#L'animation
animation_frames = []
for i in range(1,30):
    frame = pygame.image.load(f"../data/animation/{i}.png").convert_alpha()
    animation_frames.append(frame)

animating = False
current_frame = 0
animation_speed = 0
frame_counter = 0

#le fonctionnement des boutons du multiplicateur
class Button:
    def __init__(self,text,x_pos,y_pos,enabled):
        self.text=text
        self.x_pos=x_pos
        self.y_pos=y_pos
        self.enabled=enabled
        self.draw()

    def draw(self):
        button_text=font.render(self.text,True,'black')
        button_rect=pygame.rect.Rect((self.x_pos,self.y_pos),(78,14.5))

        if self.enabled:
            if self.check_click():
                pygame.draw.rect(screen,'dark gray',button_rect,0,5)
            else:
                pygame.draw.rect(screen,'light gray',button_rect,0,5)
        else:
            pygame.draw.rect(screen,'black',button_rect,0,10)
        pygame.draw.rect(screen,'black',button_rect,2,5)
        screen.blit(button_text,(self.x_pos+3,self.y_pos))

    def check_click(self):
        mouse_pos=pygame.mouse.get_pos()
        left_click=pygame.mouse.get_pressed()[0]
        button_rect=pygame.rect.Rect((self.x_pos,self.y_pos),(75,12.5))
        if left_click and button_rect.collidepoint(mouse_pos) and self.enabled:
            return True
        else:
            return False

#nomination de tout les images + création des boutons
background = pygame.image.load("../data/Ete fi.png").convert_alpha()
background2= pygame.image.load("../data/Hiver. fi.png").convert_alpha()
background3=pygame.image.load("../data/PRI fi.png").convert_alpha()
image  = pygame.image.load("../data/Rea.png").convert_alpha()
image_size = pygame.Rect((324,150),(185,200))
rea = pygame.image.load("../data/Rea_petit.png").convert_alpha()
rea_bouton=button.Button(15, 70, rea, 1)

achtung_img= pygame.image.load("../data/achtung.png").convert_alpha()
achtung2_img= pygame.image.load("../data/achtung2.png").convert_alpha()
achtung_bouton=button.Button(80,225, achtung_img, 1)
achtung2_bouton=button.Button(80,225, achtung2_img, 1)
achtung2_bouton2=button.Button(80,150, achtung2_img, 1)


gravas = pygame.image.load("../data/Logo_gravas.png").convert_alpha()


mis_rempli= pygame.image.load("../data/mis rempli.png").convert_alpha()
mis_rempli_bouton=button.Button(15, 170, mis_rempli, 1)
rempli= pygame.image.load("../data/rempli.png").convert_alpha()
rempli_bouton=button.Button(15, 170, rempli, 1)
non_rempli= pygame.image.load("../data/non rempli.png").convert_alpha()
non_rempli_bouton=button.Button(15, 170, non_rempli, 1)

robot_img= pygame.image.load("../data/robot.png").convert_alpha()
robot_bouton = button.Button(100,50, robot_img, 1)

background1 = pygame.image.load("../data/Autfi.png").convert_alpha()

dix_img = pygame.image.load('../data/100.png').convert_alpha()
dix_bouton = button.Button(110, 250, dix_img, 1)

neuf_img = pygame.image.load('../data/90.png').convert_alpha()
neuf_bouton = button.Button(170, 250, neuf_img, 1)

huit_img = pygame.image.load('../data/80.png').convert_alpha()
huit_bouton = button.Button(230, 250, huit_img, 1)

sept_img = pygame.image.load('../data/70.png').convert_alpha()
sept_bouton = button.Button(290, 250, sept_img, 1)

six_img = pygame.image.load('../data/60.png').convert_alpha()
six_bouton = button.Button(350, 250, six_img, 1)

cinq_img = pygame.image.load('../data/50.png').convert_alpha()
cinq_bouton = button.Button(460, 250, cinq_img, 1)

quatre_img = pygame.image.load('../data/40.png').convert_alpha()
quatre_bouton = button.Button(570, 250, quatre_img, 1)

trois_img = pygame.image.load('../data/30.png').convert_alpha()
trois_bouton = button.Button(630, 250, trois_img, 1)

deux_img = pygame.image.load('../data/20.png').convert_alpha()
deux_bouton = button.Button(690, 250, deux_img, 1)

un_img = pygame.image.load('../data/10.png').convert_alpha()
un_bouton = button.Button(750, 250, un_img, 1)

zero_img = pygame.image.load('../data/0.png').convert_alpha()
zero_bouton = button.Button(810, 250, zero_img, 1)

#boutique_img = pygame.image.load('../data/BOUTIQUE.png').convert_alpha()
#boutique_bouton = button.Button(5, 70, boutique_img, 1)

cailloux_img=pygame.image.load('../data/CAILLOUX.png').convert_alpha()
cailloux_bouton = button.Button(5, 70, cailloux_img, 1)

citrine_img=pygame.image.load('../data/citrine1_petit.png').convert_alpha()
citrine_bouton= button.Button(5, 70, citrine_img, 1)
citrine_img=pygame.image.load('../data/citrine1.png').convert_alpha()

oeil_img=pygame.image.load('../data/Oeil du tigre_petit.png').convert_alpha()
oeil_bouton= button.Button(5, 300, oeil_img, 1)
oeil_img=pygame.image.load('../data/Oeil du tigre.png').convert_alpha()

kirby_gif=pygame.image.load('../data/kirby.gif').convert_alpha()
kirby_bouton= button.Button(300, 12, kirby_gif, 1)

mode_histoire_img= pygame.image.load('../data/MODE HISTOIRE.png').convert_alpha()
mode_histoire_bouton= button.Button(5, 150, mode_histoire_img, 1)

danger_img= pygame.image.load('../data/Danger.png').convert_alpha()
danger_bouton= button.Button(5,230, danger_img, 1)

jaspe_img=pygame.image.load("../data/Jaspe_rougeV2.png").convert_alpha()
jaspe_bouton=button.Button(5, 150, jaspe_img, 1)
jaspe_img=pygame.image.load("../data/Jaspe_rougeV2_grand.png").convert_alpha()

Labradorite_img = pygame.image.load('../data/Labradorite.png').convert_alpha()
Labradorite_bouton = button.Button(5, 230, Labradorite_img, 1)
Labradorite_img = pygame.image.load('../data/Labradorite_grand.png').convert_alpha()

Sodalite_img = pygame.image.load('../data/Sodalite_petit.png').convert_alpha()
Sodalite_bouton = button.Button(5, 300, Sodalite_img, 1)
Sodalite_img = pygame.image.load('../data/Sodalite.png').convert_alpha()

Aigue_Marine_petit_img = pygame.image.load('../data/Aigue Marine_petit.png').convert_alpha()
Aigue_Marine_bouton = button.Button(5, 300, Aigue_Marine_petit_img, 1)
Aigue_Marine_img = pygame.image.load('../data/Aigue Marine.png').convert_alpha()

pierre_du_soleil_petit_img = pygame.image.load('../data/Pierre du Soleil_petit.png').convert_alpha()
pierre_du_soleil_bouton = button.Button(5, 150, pierre_du_soleil_petit_img, 1)
pierre_du_soleil_img = pygame.image.load('../data/Pierre du Soleil.png').convert_alpha()

nacre_img=pygame.image.load("../data/Nacre_petit.png").convert_alpha()
nacre_bouton=button.Button(5, 230, nacre_img, 1)
nacre_img=pygame.image.load("../data/Nacre.png").convert_alpha()

hematite_img=pygame.image.load("../data/Hematite_petit.png").convert_alpha()
hematite_bouton=button.Button(5, 70, hematite_img, 1)
hematite_img=pygame.image.load("../data/Hematite.png").convert_alpha()

pyrite_img=pygame.image.load("../data/Pyrite_petit.png").convert_alpha()
pyrite_bouton=button.Button(5, 150, pyrite_img, 1)
pyrite_img=pygame.image.load("../data/Pyrite.png").convert_alpha()

quartz_fumee_img=pygame.image.load("../data/Quartz fumee_petit.png").convert_alpha()
quartz_fumee_bouton=button.Button(5, 230, quartz_fumee_img, 1)
quartz_fumee_img=pygame.image.load("../data/Quartz fumee.png").convert_alpha()

amethyst_img=pygame.image.load('../data/Amethyst_petit.png').convert_alpha()
amethyst_bouton= button.Button(5, 70, amethyst_img, 1)
amethyst_img=pygame.image.load('../data/Amethyst.png').convert_alpha()

grenat_img = pygame.image.load('../data/grenat_petit.png').convert_alpha()
grenat_bouton = button.Button(5, 150, grenat_img, 1)
grenat_img = pygame.image.load('../data/grenat.png').convert_alpha()

quartz_img=pygame.image.load("../data/Quartz rose_petit.png").convert_alpha()
quartz_bouton=button.Button(5, 230, quartz_img, 1)
quartz_img=pygame.image.load("../data/Quartz rose.png").convert_alpha()

Rodocrosite_img = pygame.image.load('../data/Rodocrosite_petit.png').convert_alpha()
Rodocrosite_bouton = button.Button(5, 320, Rodocrosite_img, 1)
Rodocrosite_img = pygame.image.load('../data/Rodocrosite.png').convert_alpha()

#le début de la boucle
while running == True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            #Le menu des options etc.
            if event.key == pygame.K_TAB:
                game_paused = True
                boutique_ouverte=False
                animation=False
        #Le fonctionnement de la fenêtre
        if event.type == pygame.QUIT:
            running = False
        #Le clickage
        if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1) and image_size.collidepoint(event.pos):
            score += argent*multi
            effect.play()
            animation=True
            animating = True
            current_frame = 0
            if game_paused==True or menu_boutique!="tout" or boutique_ouverte==False:
                score=score-argent*multi

        #La première question
        if game_paused==False:
            if event.type==pygame.MOUSEBUTTONDOWN and input_rect.collidepoint(pygame.mouse.get_pos()):
                active=True
            elif event.type==pygame.MOUSEBUTTONDOWN and not input_rect.collidepoint(pygame.mouse.get_pos()):
                active=False
            if event.type==pygame.KEYDOWN:
                if active == True:
                    if event.key == pygame.K_BACKSPACE:
                        user_texte=user_texte[:-1]
                    else:
                        user_texte += event.unicode
            #La deuxième question
            if event.type==pygame.MOUSEBUTTONDOWN and input_rect1.collidepoint(pygame.mouse.get_pos()):
                active1=True
            elif event.type==pygame.MOUSEBUTTONDOWN and not input_rect1.collidepoint(pygame.mouse.get_pos()):
                active1=False
            if event.type==pygame.KEYDOWN:
                if active1 == True:
                    if event.key == pygame.K_BACKSPACE:
                        user_texte1=user_texte1[:-1]
                    else:
                        user_texte1 += event.unicode

            #La troisième question
            if event.type==pygame.MOUSEBUTTONDOWN and input_rect2.collidepoint(pygame.mouse.get_pos()):
                active2=True
            elif event.type==pygame.MOUSEBUTTONDOWN and not input_rect2.collidepoint(pygame.mouse.get_pos()):
                active2=False
            if event.type==pygame.KEYDOWN:
                if active2 == True:
                    if event.key == pygame.K_BACKSPACE:
                        user_texte2=user_texte2[:-1]
                    else:
                        user_texte2 += event.unicode

            #La quatrième question
            if event.type==pygame.MOUSEBUTTONDOWN and input_rect3.collidepoint(pygame.mouse.get_pos()):
                active3=True
            elif event.type==pygame.MOUSEBUTTONDOWN and not input_rect3.collidepoint(pygame.mouse.get_pos()):
                active3=False
            if event.type==pygame.KEYDOWN:
                if active3 == True:
                    if event.key == pygame.K_BACKSPACE:
                        user_texte3=user_texte3[:-1]
                    else:
                        user_texte3 += event.unicode

            #La cinquième question
            if event.type==pygame.MOUSEBUTTONDOWN and input_rect4.collidepoint(pygame.mouse.get_pos()):
                active4=True
            elif event.type==pygame.MOUSEBUTTONDOWN and not input_rect4.collidepoint(pygame.mouse.get_pos()):
                active4=False
            if event.type==pygame.KEYDOWN:
                if active4 == True:
                    if event.key == pygame.K_BACKSPACE:
                        user_texte4=user_texte4[:-1]
                    else:
                        user_texte4 += event.unicode

            #La sixième question
            if event.type==pygame.MOUSEBUTTONDOWN and input_rect5.collidepoint(pygame.mouse.get_pos()):
                active5=True
            elif event.type==pygame.MOUSEBUTTONDOWN and not input_rect5.collidepoint(pygame.mouse.get_pos()):
                active5=False
            if event.type==pygame.KEYDOWN:
                if active5 == True:
                    if event.key == pygame.K_BACKSPACE:
                        user_texte5=user_texte5[:-1]
                    else:
                        user_texte5 += event.unicode


            #La septième question
            if event.type==pygame.MOUSEBUTTONDOWN and input_rect6.collidepoint(pygame.mouse.get_pos()):
                active6=True
            elif event.type==pygame.MOUSEBUTTONDOWN and not input_rect6.collidepoint(pygame.mouse.get_pos()):
                active6=False
            if event.type==pygame.KEYDOWN:
                if active6 == True:
                    if event.key == pygame.K_BACKSPACE:
                        user_texte6=user_texte6[:-1]
                    else:
                        user_texte6 += event.unicode

            #La huiptième question
            if event.type==pygame.MOUSEBUTTONDOWN and input_rect7.collidepoint(pygame.mouse.get_pos()):
                active7=True
            elif event.type==pygame.MOUSEBUTTONDOWN and not input_rect7.collidepoint(pygame.mouse.get_pos()):
                active7=False
            if event.type==pygame.KEYDOWN:
                if active7 == True:
                    if event.key == pygame.K_BACKSPACE:
                        user_texte7=user_texte7[:-1]
                    else:
                        user_texte7 += event.unicode

            #La neuvième question
            if event.type==pygame.MOUSEBUTTONDOWN and input_rect8.collidepoint(pygame.mouse.get_pos()):
                active8=True
            elif event.type==pygame.MOUSEBUTTONDOWN and not input_rect8.collidepoint(pygame.mouse.get_pos()):
                active8=False
            if event.type==pygame.KEYDOWN:
                if active8 == True:
                    if event.key == pygame.K_BACKSPACE:
                        user_texte8=user_texte8[:-1]
                    else:
                        user_texte8 += event.unicode

            #La 10ème question
            if event.type==pygame.MOUSEBUTTONDOWN and input_rect9.collidepoint(pygame.mouse.get_pos()):
                active9=True
            elif event.type==pygame.MOUSEBUTTONDOWN and not input_rect9.collidepoint(pygame.mouse.get_pos()):
                active9=False
            if event.type==pygame.KEYDOWN:
                if active9 == True:
                    if event.key == pygame.K_BACKSPACE:
                        user_texte9=user_texte9[:-1]
                    else:
                        user_texte9 += event.unicode

            #La 11ème question
            if event.type==pygame.MOUSEBUTTONDOWN and input_rect10.collidepoint(pygame.mouse.get_pos()):
                active10=True
            elif event.type==pygame.MOUSEBUTTONDOWN and not input_rect10.collidepoint(pygame.mouse.get_pos()):
                active10=False
            if event.type==pygame.KEYDOWN:
                if active10 == True:
                    if event.key == pygame.K_BACKSPACE:
                        user_texte10=user_texte10[:-1]
                    else:
                        user_texte10 += event.unicode

            #La 12ème question
            if event.type==pygame.MOUSEBUTTONDOWN and input_rect11.collidepoint(pygame.mouse.get_pos()):
                active11=True
            elif event.type==pygame.MOUSEBUTTONDOWN and not input_rect11.collidepoint(pygame.mouse.get_pos()):
                active11=False
            if event.type==pygame.KEYDOWN:
                if active11 == True:
                    if event.key == pygame.K_BACKSPACE:
                        user_texte11=user_texte11[:-1]
                    else:
                        user_texte11 += event.unicode

#Le menu des boutiques
    if menu_boutique=="tout":
        #if boutique_bouton.draw(screen):
         #   menu_boutique="boutique"
          #  animation = False
           # effect.stop()
        if cailloux_bouton.draw(screen):
            menu_boutique="cailloux"
            menu_boutique!='tout'
            animation = False
            effect.stop()
        if mode_histoire_bouton.draw(screen):
            menu_boutique="mode_histoire"
        if danger_bouton.draw(screen):
            menu_boutique="danger"



#Le menu des pierres dans la première saison.
    if menu_boutique=="cailloux" and back0==True and boutique_ouverte==True:
        effect.stop()
        action_done=False
        action_done1=False
        action_done3=False
        back_button = button.Button(300, 125, back_img, 1)
        draw_text("Prix : gratuit",font,TEXT_COL,120,80)
        draw_text(" Une PIERRE",font,TEXT_COL,120,100)

        draw_text("Prix : 10k gravas",font,TEXT_COL,120,160)
        draw_text("La pierre du Soleil",font,TEXT_COL,120,180)

        draw_text("Prix : 50k gravas",font,TEXT_COL,120,245)
        draw_text("Nacre",font,TEXT_COL,120,265)

        draw_text("Prix : 75k gravas",font,TEXT_COL,120,310)
        draw_text("Aigue marine",font,TEXT_COL,120,330)
        if rea_bouton.draw(screen):
            image=image
            argent=100
        if pierre_du_soleil_bouton.draw(screen) and score>=10000:
            image=pierre_du_soleil_img
            argent=300
        if nacre_bouton.draw(screen) and score>=50000:
            image=nacre_img
            argent=500
        if Aigue_Marine_bouton.draw(screen) and score>=75000:
            image=Aigue_Marine_img
            argent=600
        if back_button.draw(screen):
            menu_boutique="tout"
            pas_argent=False
            animation=True
    elif boutique_ouverte==False:
        menu_boutique="tout"
        animation = True



#Le menu des pierres dans la deuxième saison.
    if menu_boutique=="cailloux" and back==True and boutique_ouverte==True:
        action_done=False
        action_done1=False
        action_done3=False
        effect.stop()
        back_button = button.Button(300, 125, back_img, 1)
        draw_text("Prix : 120k gravas",font,TEXT_COL,120,80)
        draw_text("Citrine",font,TEXT_COL,120,100)

        draw_text("Prix : 400k gravas",font,TEXT_COL,120,160)
        draw_text("jaspe_rouge",font,TEXT_COL,120,180)

        draw_text("Prix : 600k gravas",font,TEXT_COL,120,245)
        draw_text("Labradorite",font,TEXT_COL,120,265)

        draw_text("Prix : 850k gravas",font,TEXT_COL,120,310)
        draw_text("L'oeil du tigre",font,TEXT_COL,120,330)
        if back_button.draw(screen):
            menu_boutique="tout"
            pas_argent=False
        if citrine_bouton.draw(screen) and score>=120000:
            image=citrine_img
            argent=1000
        if jaspe_bouton.draw(screen) and score>=400000:
            image=jaspe_img
            argent=2000
        if Labradorite_bouton.draw(screen) and score>=600000:
            image=Labradorite_img
            argent=5000
        if oeil_bouton.draw(screen) and score>=850000:
            image= oeil_img
            argent=7500
        if back_button.draw(screen):
            menu_boutique="tout"
            pas_argent=False


#Le menu des pierres dans la troisième saison.
    if menu_boutique=="cailloux" and back2==True and boutique_ouverte==True:
        action_done=False
        action_done1=False
        action_done3=False
        effect.stop()
        back_button = button.Button(300, 125, back_img, 1)
        draw_text("Prix : 1.5M gravas",font,TEXT_COL,120,80)
        draw_text(" Hematite",font,TEXT_COL,120,100)

        draw_text("Prix : 5M gravas",font,TEXT_COL,120,160)
        draw_text("",font,TEXT_COL,120,180)

        draw_text("Prix : 7.5M gravas",font,TEXT_COL,120,245)
        draw_text("Nacre",font,TEXT_COL,120,265)

        draw_text("Prix : 8.8M gravas",font,TEXT_COL,120,310)
        draw_text("Aigue marine",font,TEXT_COL,120,330)
        if back_button.draw(screen):
            menu_boutique="tout"
            pas_argent=False
        if hematite_bouton.draw(screen) and score>=1500000:
            image=hematite_img
            argent=10000
        if pyrite_bouton.draw(screen) and score>=5000000:
            image=pyrite_img
            argent=20000
        if quartz_fumee_bouton.draw(screen) and score>=7500000:
            image=quartz_fumee_img
            argent=30000
        if Sodalite_bouton.draw(screen) and score>=8800000:
            image= Sodalite_img
            argent=50000

#Le menu des pierres dans la quatrième saison.
    if menu_boutique=="cailloux" and back3==True and boutique_ouverte==True:
        action_done=False
        action_done1=False
        action_done3=False
        effect.stop()
        back_button = button.Button(300, 125, back_img, 1)
        draw_text("Prix : 25M gravas",font,TEXT_COL,120,80)
        draw_text(" Hematite",font,TEXT_COL,120,100)

        draw_text("Prix : 50M gravas",font,TEXT_COL,120,160)
        draw_text("Améthyste",font,TEXT_COL,120,180)

        draw_text("Prix : 75M gravas",font,TEXT_COL,120,340)
        draw_text("Rodoscorite",font,TEXT_COL,120,360)

        draw_text("Prix : 100M gravas",font,TEXT_COL,120,245)
        draw_text("Quartz rosée",font,TEXT_COL,120,265)
        if back_button.draw(screen):
            menu_boutique="tout"
            pas_argent=False
        if amethyst_bouton.draw(screen) and score>=25000000:
            image=amethyst_img
            argent=100000
        if grenat_bouton.draw(screen) and score>=50000000:
            image=grenat_img
            argent=200000
        if Rodocrosite_bouton.draw(screen) and score>=75000000:
            image=Rodocrosite_img
            argent=300000
        if quartz_bouton.draw(screen) and score>=100000000:
            image= quartz_img
            argent=500000
        if back_button.draw(screen):
            menu_boutique="tout"
            pas_argent=False




    #if menu_boutique=="boutique" and boutique_ouverte==True:
        #effect.stop()
        #animation=False
        #action_done=False
        #action_done1=False
        #action_done3=False
        #back_button = button.Button(300, 125, back_img, 1)
        #if curseur_bouton.draw(screen) and score>=1000:
         #   auto_click=True
        #if curseur2_bouton.draw(screen) and score>=50000:
         #   auto_click2=True
        #    auto_click=False
       # if back_button.draw(screen):
      #      menu_boutique="tout"
     #       animation=True


    if action_done3==True:
            if achtung2_bouton2.draw(screen):
                pas_argent=False




    #Le menu du mode histoire.
    if menu_boutique=="mode_histoire" and boutique_ouverte==True:
        effect.stop()
        animation=False
        action_done=False
        action_done1=False
        action_done3=False
        back_button = button.Button(500, 325, back_img, 1)
        if robot_bouton.draw(screen):
            texte1=False
            texte2=True
        if back_button.draw(screen):
            menu_boutique="tout"
            animation=True
#Le menu danger.
    if menu_boutique=="danger" and boutique_ouverte==True:
        back_button = button.Button(100, 280, back_img, 1)
        draw_text("Cliquer sur le réservoir pour augmenter la quantité d'eau",font2,TEXT_COL,0,140)
        action_done=False
        action_done1=False
        action_done3=False
        if remplir1==True:
            if rempli_bouton.draw(screen) :
                start_time=start_time
        if remplir2==False:
            if mis_rempli_bouton.draw(screen):
                start_time=start_time+30000
                remplir1=True
                remplir2=True
                action_done=True
        if remplir3==False:
            if non_rempli_bouton.draw(screen):
                start_time=start_time+70000
                remplir3=True
                remplir1=True
        if back_button.draw(screen):
            menu_boutique="tout"
    if active==True or active1==True or active2==True  :
        game_paused=False
    if action_done==True:
        if achtung_bouton.draw(screen):
            pas_argent=False
    if action_done1==True:
        if achtung2_bouton.draw(screen):
            pas_argent=False

    current_time = pygame.time.get_ticks()

    if current_time - start_time <= 30000:
        remplir1=True
        remplir2=True
        remplir3=True
        action_done=False
        action_done1=False

    if current_time - start_time >= 30000:
        remplir2=False
        remplir1=False
        action_done=True

    if current_time - start_time >= 60000:
        remplir3=False
        remplir2=True
        action_done1=True
    if back0==True:
        if current_time - start_time >= 90000:
            score=score-1

    if back==True:
        if current_time - start_time >= 90000:
            score=score-100

    if back2==True:
        if current_time - start_time >= 90000:
            score=score-1000
    if back3==True:
        if current_time - start_time >= 90000:
            score=score-100000


#Le menu pause
    if game_paused == True:
        back_button = button.Button(400, 325, back_img, 1)
    #check menu state
        active=False
        active1=False
        active2=False
        #auto_click=False
        #auto_click2=False
        animation=False
        effect.stop()
        if menu_state == "main":
      #draw pause screen buttons
            if resume_button.draw(screen):
                game_paused=False
                boutique_ouverte=True
                animation = True
            if options_button.draw(screen):
                menu_state="options"

        #check if the options menu is open
        if menu_state=="options":
        #draw the different options buttons
            back_button = button.Button(400, 400, back_img, 1)
            if video_button.draw(screen):
                menu_state="Effect"
            if audio_button.draw(screen):
                menu_state="Audio_Settings"
            if back_button.draw(screen):
                menu_state = "main"
        #Le menu du volume pour les effects
        if menu_state=="Effect":
            draw_text("mettez le volume voulus",police,(255,255,255),250,100)
            if dix_bouton.draw(screen):
                effect.set_volume(1.0)
            if neuf_bouton.draw(screen):
                effect.set_volume(0.9)
            if huit_bouton.draw(screen):
                effect.set_volume(0.8)
            if sept_bouton.draw(screen):
                effect.set_volume(0.7)
            if six_bouton.draw(screen):
                effect.set_volume(0.6)
            if cinq_bouton.draw(screen):
                effect.set_volume(0.5)
            if quatre_bouton.draw(screen):
                effect.set_volume(0.4)
            if trois_bouton.draw(screen):
                effect.set_volume(0.3)
            if deux_bouton.draw(screen):
                effect.set_volume(0.2)
            if un_bouton.draw(screen):
                effect.set_volume(0.1)
            if zero_bouton.draw(screen):
                effect.set_volume(0)
            if back_button.draw(screen):
                menu_state = "options"
        #Le menu du volume des musiques.
        if menu_state=="Audio_Settings":
            draw_text("mettez le volume voulus",police,(255,255,255),250,100)
            if dix_bouton.draw(screen):
                musique.set_volume(1.0)
                musique2.set_volume(1.0)
                musique3.set_volume(1.0)
                musique4.set_volume(1.0)
            if neuf_bouton.draw(screen):
                musique.set_volume(0.9)
                musique2.set_volume(0.9)
                musique3.set_volume(0.9)
                musique4.set_volume(0.9)
            if huit_bouton.draw(screen):
                musique.set_volume(0.8)
                musique2.set_volume(0.8)
                musique3.set_volume(0.8)
                musique4.set_volume(0.8)
            if sept_bouton.draw(screen):
                musique.set_volume(0.7)
                musique2.set_volume(0.7)
                musique3.set_volume(0.7)
                musique4.set_volume(0.7)
            if six_bouton.draw(screen):
                musique.set_volume(0.6)
                musique2.set_volume(0.6)
                musique3.set_volume(0.6)
                musique4.set_volume(0.6)
            if cinq_bouton.draw(screen):
                musique.set_volume(0.5)
                musique2.set_volume(0.5)
                musique3.set_volume(0.5)
                musique4.set_volume(0.5)
            if quatre_bouton.draw(screen):
                musique.set_volume(0.4)
                musique2.set_volume(0.4)
                musique3.set_volume(0.4)
                musique4.set_volume(0.4)
            if trois_bouton.draw(screen):
                musique.set_volume(0.3)
                musique2.set_volume(0.3)
                musique3.set_volume(0.3)
                musique4.set_volume(0.3)
            if deux_bouton.draw(screen):
                musique.set_volume(0.2)
                musique2.set_volume(0.2)
                musique3.set_volume(0.2)
                musique4.set_volume(0.2)
            if un_bouton.draw(screen):
                musique.set_volume(0.1)
                musique2.set_volume(0.1)
                musique3.set_volume(0.1)
                musique4.set_volume(0.1)
            if zero_bouton.draw(screen):
                musique.set_volume(0)
                musique2.set_volume(0)
                musique3.set_volume(0)
                musique4.set_volume(0)
            if back_button.draw(screen):
                menu_state = "options"

    else:
        draw_text("appuyer sur TAB pour", font, TEXT_COL, 630, 50)
        draw_text("mettre en pause le jeu", font, TEXT_COL, 630, 70)


    #partie des boutons multiplicateurs
    my_button=Button("multiplicateur x2 ",10,10,my_button_enabled )
    my_button2=Button("multiplicateur x4 ",10,40,my_button_enabled1)
    if event.type == pygame.MOUSEBUTTONDOWN and score>=50000:
        my_button_enabled=True
        if my_button.check_click():
            button_text=font.render("un multiplicateur x2 est activé",True,'black')
            screen.blit(button_text,(100,10))
            multi=2
    if event.type == pygame.MOUSEBUTTONDOWN and score>=100000:
        my_button_enabled1=True
        if my_button2.check_click():
            button_text2=font.render("un multiplicateur x4 est activé",True,'black')
            screen.blit(button_text2,(100,10))
            multi=4






    #Le questionnaires pour chaque saison.
    if back3==True:

        énoncé91="Quelle est l'animal le plus"
        énoncé92= "lourd de la Terre?"
        énoncé_rect=pygame.Rect((820,100),(120,32))

        énoncé101="Quelle la valeur décimale de"
        énoncé102="ce nombre binaire: 01000011"
        énoncé10_rect=pygame.Rect((820,200),(134,31))

        énoncé111="Quelle est l'animal le plus"
        énoncé112="rapide de la Terre?"
        énoncé20_rect=pygame.Rect((820,300),(120,31))


        if score>=30000000:
            pygame.draw.rect(screen,"Black",énoncé_rect,2)
            pygame.draw.rect(screen,"Black",input_rect9,2)
            if user_texte9.lower()=="baleine bleue" :
                score=score+10000000
                user_texte9="récompense obtenu"
                active9=False
            if user_texte9=="récompense obtenu":
                active9=False
            draw_text("+10M",font,(0,255,0),755,100)
            screen.blit(énoncé19_surface,(830,104))
            screen.blit(énoncé20_surface,(830,116))
            input_rect9.w=max(50,texte_surface9.get_width()+10)
            screen.blit(texte_surface9,(input_rect9.x+5,input_rect9.y+5))

        if score>=50000000:
            pygame.draw.rect(screen,"Black",énoncé10_rect,2)
            pygame.draw.rect(screen,"Black",input_rect10,2)
            if user_texte10=="67":
                score=score+500000
                user_texte10="récompense obtenu"
                active10=False
            if user_texte10=="récompense obtenu":
                active10=False
            screen.blit(énoncé21_surface,(825,202))
            screen.blit(énoncé22_surface,(825,217))
            draw_text("+10M",font,(0,255,0),755,200)
            input_rect10.w=max(50,texte_surface10.get_width()+10)
            screen.blit(texte_surface10,(input_rect10.x+5,input_rect10.y+5))

        if score>=75000000:
            pygame.draw.rect(screen,"Black",énoncé20_rect,2)
            pygame.draw.rect(screen,"Black",input_rect11,2)
            if user_texte11=="léopard" or user_texte11=="Léopard":
                score=score+10000000
                user_texte11="récompense obtenu"
                active11=False
            if user_texte11=="récompense obtenu":
                active11=False
            screen.blit(énoncé23_surface,(825,302))
            screen.blit(énoncé24_surface,(825,317))
            draw_text("+10M",font,(0,255,0),755,300)
            input_rect11.w=max(50,texte_surface11.get_width()+10)
            screen.blit(texte_surface11,(input_rect11.x+5,input_rect11.y+5))


    if back2==True:

        if score>=3000000:
            énoncé61="Quelle a été le permier"
            énoncé62="message de l'informatique?"
            énoncé_rect=pygame.Rect((825,100),(130,32))

            énoncé71="Comment nomme-t-on "
            énoncé72="le cri des éléphants?"
            énoncé10_rect=pygame.Rect((820,200),(110,31))

            énoncé81="Quel pourcentage d’eau"
            énoncé82="recouvre la planète Terre?"
            énoncé20_rect=pygame.Rect((820,300),(120,31))


            pygame.draw.rect(screen,"Black",énoncé_rect,2)
            pygame.draw.rect(screen,"Black",input_rect6,2)
            if user_texte6=="Hello world":
                score=score+1000000
                user_texte6="récompense obtenu"
                active6=False
            if user_texte6=="récompense obtenu":
                active6=False
            draw_text("+1M",font,(0,255,0),755,100)
            screen.blit(énoncé13_surface,(830,104))
            screen.blit(énoncé14_surface,(830,116))
            input_rect6.w=max(50,texte_surface6.get_width()+10)
            screen.blit(texte_surface6,(input_rect6.x+5,input_rect6.y+5))

        if score>=5000000:
            pygame.draw.rect(screen,"Black",énoncé10_rect,2)
            pygame.draw.rect(screen,"Black",input_rect7,2)
            if user_texte7.lower()=="barissement":
                score=score+1000000
                user_texte7="récompense obtenu"
                active7=False
            if user_texte7=="récompense obtenu" :
                active7=False
            screen.blit(énoncé15_surface,(825,202))
            screen.blit(énoncé16_surface,(825,217))
            draw_text("+1M",font,(0,255,0),755,200)
            input_rect7.w=max(50,texte_surface7.get_width()+10)
            screen.blit(texte_surface7,(input_rect7.x+5,input_rect7.y+5))

        if score>=7500000:
            pygame.draw.rect(screen,"Black",énoncé20_rect,2)
            pygame.draw.rect(screen,"Black",input_rect8,2)
            if user_texte8=="72%":
                score=score+1000000
                user_texte8="récompense obtenu"
                active8=False
            if user_texte8=="récompense obtenu" :
                active8=False
            screen.blit(énoncé17_surface,(825,302))
            screen.blit(énoncé18_surface,(825,317))
            draw_text("+1M",font,(0,255,0),755,300)
            input_rect8.w=max(50,texte_surface8.get_width()+10)
            screen.blit(texte_surface8,(input_rect8.x+5,input_rect8.y+5))

    if back==True:

        énoncé31="Comment appelle-t-on l’organe "
        énoncé32="reproducteur mâle d’une fleur?"
        énoncé_rect=pygame.Rect((810,100),(140,32))

        énoncé42="Quel insecte était vénéré "
        énoncé41="par les Égyptiens ?"
        énoncé10_rect=pygame.Rect((820,200),(130,31))

        énoncé51="Les êtres vivants qui se nourrissent"
        énoncé52="de végétaux et d’animaux sont…"
        énoncé20_rect=pygame.Rect((795,300),(160,31))
        if score>=300000:
            pygame.draw.rect(screen,"Black",énoncé_rect,2)
            pygame.draw.rect(screen,"Black",input_rect,2)
            if user_texte3=="étamine" or user_texte3=="Etamine":
                score=score+100000
                user_texte3="récompense obtenu"
                active3=False
            if user_texte3=="récompense obtenu":
                active3=False
            screen.blit(énoncé7_surface,(815,104))
            screen.blit(énoncé8_surface,(815,116))
            draw_text("+100000",font,(0,255,0),755,100)
            input_rect3.w=max(50,texte_surface3.get_width()+10)
            screen.blit(texte_surface3,(input_rect3.x+5,input_rect3.y+5))

        if score>=500000:
            pygame.draw.rect(screen,"Black",énoncé10_rect,2)
            pygame.draw.rect(screen,"Black",input_rect4,2)
            if user_texte4=="Scarabée" or user_texte4=="scarabée":
                score=score+100000
                user_texte4="récompense obtenu"
                active4=False
            if user_texte4=="récompense obtenu":
                active4=False
            screen.blit(énoncé10_surface,(830,202))
            screen.blit(énoncé9_surface,(845,217))
            draw_text("+100000",font,(0,255,0),755,200)
            input_rect4.w=max(50,texte_surface4.get_width()+10)
            screen.blit(texte_surface4,(input_rect4.x+5,input_rect4.y+5))

        if score>=750000:
            pygame.draw.rect(screen,"Black",énoncé20_rect,2)
            pygame.draw.rect(screen,"Black",input_rect5,2)
            if user_texte5.lower()=="omnivores":
                score=score+100000
                user_texte5="récompense obtenu"
                active5=False
            if user_texte5=="récompense obtenu" :
                active2=False
            screen.blit(énoncé11_surface,(800,302))
            screen.blit(énoncé12_surface,(805,317))
            draw_text("+100000",font,(0,255,0),755,300)
            input_rect5.w=max(50,texte_surface5.get_width()+10)
            screen.blit(texte_surface5,(input_rect5.x+5,input_rect5.y+5))


    if back0==True:
        énoncé01="Quel est l'arbre le"
        énoncé02="plus grand au monde?"
        énoncé_rect=pygame.Rect((825,100),(100,32))

        énoncé12="Les manchots sont des"
        énoncé11="animaux qui ne peuvent pas voler"
        énoncé10_rect=pygame.Rect((800,200),(150,31))

        énoncé21="Quel est le plus grand océan "
        énoncé22="de la planète en superficie ?"
        énoncé20_rect=pygame.Rect((800,300),(150,31))
        if score>=30000:
            pygame.draw.rect(screen,"Black",énoncé_rect,2)
            pygame.draw.rect(screen,"Black",input_rect,2)
            if user_texte=="hypérion":
                score=score+7000
                user_texte="récompense obtenu"
                active=False
            if user_texte=="récompense obtenu":
                active=False
            draw_text("+7000",font,(0,255,0),755,100)
            screen.blit(énoncé1_surface,(830,104))
            screen.blit(énoncé2_surface,(830,116))
            input_rect.w=max(50,texte_surface.get_width()+10)
            screen.blit(texte_surface,(input_rect.x+5,input_rect.y+5))

        if score>=50000:
            pygame.draw.rect(screen,"Black",énoncé10_rect,2)
            pygame.draw.rect(screen,"Black",input_rect1,2)
            if user_texte1=="Faux" or user_texte1=="faux":
                score=score+10000
                user_texte1="récompense obtenu"
                active1=False
            if user_texte1=="Vrai" or user_texte1=="vrai":
                user_texte1="réponse fausse"
            if user_texte1=="récompense obtenu" or user_texte1=="réponse fausse":
                active1=False
            screen.blit(énoncé4_surface,(825,202))
            screen.blit(énoncé3_surface,(805,217))
            draw_text("+10000",font,(0,255,0),755,200)
            input_rect1.w=max(50,texte_surface1.get_width()+10)
            screen.blit(texte_surface1,(input_rect1.x+5,input_rect1.y+5))

        if score>=75000:
            pygame.draw.rect(screen,"Black",énoncé20_rect,2)
            pygame.draw.rect(screen,"Black",input_rect2,2)
            if user_texte2=="océan pacifique":
                score=score+10000
                user_texte2="récompense obtenu"
                active2=False
            if user_texte2=="récompense obtenu":
                active2=False
            screen.blit(énoncé5_surface,(810,302))
            screen.blit(énoncé6_surface,(810,317))
            draw_text("+10000",font,(0,255,0),755,300)
            input_rect2.w=max(50,texte_surface2.get_width()+10)
            screen.blit(texte_surface2,(input_rect2.x+5,input_rect2.y+5))


    #la surface de l'input
    texte_surface=font.render(user_texte,True,(0,255,0))
    texte_surface1=font.render(user_texte1,True,(0,255,0))
    texte_surface2=font.render(user_texte2,True,(0,255,0))
    texte_surface3=font.render(user_texte3,True,(0,255,0))
    texte_surface4=font.render(user_texte4,True,(0,255,0))
    texte_surface5=font.render(user_texte5,True,(0,255,0))
    texte_surface6=font.render(user_texte6,True,(0,255,0))
    texte_surface7=font.render(user_texte7,True,(0,255,0))
    texte_surface8=font.render(user_texte8,True,(0,255,0))
    texte_surface9=font.render(user_texte9,True,(0,255,0))
    texte_surface10=font.render(user_texte10,True,(0,255,0))
    texte_surface11=font.render(user_texte11,True,(0,255,0))


    #la surface des énoncés
    énoncé1_surface=font.render(énoncé01,True,(0,255,0))
    énoncé2_surface=font.render(énoncé02,True,(0,255,0))
    énoncé3_surface=font.render(énoncé11,True,(0,255,0))
    énoncé4_surface=font.render(énoncé12,True,(0,255,0))
    énoncé5_surface=font.render(énoncé21,True,(0,255,0))
    énoncé6_surface=font.render(énoncé22,True,(0,255,0))
    énoncé7_surface=font.render(énoncé31,True,(0,255,0))
    énoncé8_surface=font.render(énoncé32,True,(0,255,0))
    énoncé9_surface=font.render(énoncé41,True,(0,255,0))
    énoncé10_surface=font.render(énoncé42,True,(0,255,0))
    énoncé11_surface=font.render(énoncé51,True,(0,255,0))
    énoncé12_surface=font.render(énoncé52,True,(0,255,0))
    énoncé13_surface=font.render(énoncé61,True,(0,255,0))
    énoncé14_surface=font.render(énoncé62,True,(0,255,0))
    énoncé15_surface=font.render(énoncé71,True,(0,255,0))
    énoncé16_surface=font.render(énoncé72,True,(0,255,0))
    énoncé17_surface=font.render(énoncé81,True,(0,255,0))
    énoncé18_surface=font.render(énoncé82,True,(0,255,0))
    énoncé19_surface=font.render(énoncé91,True,(0,255,0))
    énoncé20_surface=font.render(énoncé92,True,(0,255,0))
    énoncé21_surface=font.render(énoncé101,True,(0,255,0))
    énoncé22_surface=font.render(énoncé102,True,(0,255,0))
    énoncé23_surface=font.render(énoncé111,True,(0,255,0))
    énoncé24_surface=font.render(énoncé112,True,(0,255,0))



#à chaque changement de saison les pierres dans la boutique change, le fond etc...
    if score>=100000 and user_texte=="récompense obtenu" and (user_texte1=="récompense obtenu" or user_texte1=="réponse fausse" ) and user_texte2=="récompense obtenu" :
        background1 = background2
        pygame.mixer.Sound.stop(musique)
        musique2.play(loops=-1)
        back0=False
        back=True


    if score>=1000000 and user_texte3=="récompense obtenu" and user_texte4=="récompense obtenu" and user_texte5=="récompense obtenu":
        background1=background3
        pygame.mixer.Sound.stop(musique2)
        musique3.play(loops=-1)
        back=False
        back2=True

    if score>=10000000 and user_texte6=="récompense obtenu" and user_texte7=="récompense obtenu" and user_texte8=="récompense obtenu" :
        pygame.mixer.Sound.stop(musique3)
        musique4.play(loops=-1)
        background1=background
        back2=False
        back3=True

    if score>=100000000 and user_texte9=="récompense obtenu" and user_texte10=="récompense obtenu" and user_texte11=="récompense obtenu" :
        draw_text("Merci d'avoir sauver cette pousse d'arbre",police,TEXT_COL,130,160)
        draw_text("et d'avoir joué à notre jeu",police,TEXT_COL,250,220)


    #le menu du mode histoire
    if menu_boutique=="mode_histoire" and boutique_ouverte==True and back0==True:
        if texte1==True:
            draw_text("J'ai découvert cette pousse d’arbre sur cette",font2,TEXT_COL,130,160)
            draw_text("petite colline et j'ai commencé à avoir de ",font2,TEXT_COL,130,190)
            draw_text("l’affection pour cette pousse d’arbre. ",font2,TEXT_COL,130,220)
            draw_text("Durant les 4 saisons, je vais protéger cette ",font2,TEXT_COL,130,250)
            draw_text("arbre des catastrophes naturelles fréquentes ",font2,TEXT_COL,130,280)
            draw_text("avec certaines de mes habiletés de robot. ",font2,TEXT_COL,130,310)

        if texte2==True:
            draw_text("Pour passer à la prochaine saison tu dois",font2,TEXT_COL,130,160)
            draw_text("avoir au minimum 100000 de gravas et avoir ",font2,TEXT_COL,130,190)
            draw_text("réussi à répondre à tout les questions débloquable",font2,TEXT_COL,115,220)
            draw_text(" ",font2,TEXT_COL,130,250)
            draw_text(" ",font2,TEXT_COL,130,280)
            draw_text(" ",font2,TEXT_COL,130,310)

    if menu_boutique=="mode_histoire" and boutique_ouverte==True and back==True:
       if texte3==True:
            draw_text("Pour passer à la prochaine saison tu dois",font2,TEXT_COL,130,160)
            draw_text("avoir au minimum 1M de gravas et avoir ",font2,TEXT_COL,130,190)
            draw_text("réussi à répondre à tout les questions débloquable",font2,TEXT_COL,115,220)

    if menu_boutique=="mode_histoire" and boutique_ouverte==True and back2==True:
       if texte4==True:
            draw_text("Pour passer à la prochaine saison tu dois",font2,TEXT_COL,130,160)
            draw_text("avoir au minimum 10M de gravas et avoir ",font2,TEXT_COL,130,190)
            draw_text("réussi à répondre à tout les questions débloquable",font2,TEXT_COL,115,220)
    if menu_boutique=="mode_histoire" and boutique_ouverte==True and back3==True:
       if texte5==True:
            draw_text("Pour que tu réussisses à finir le jeu tu dois",font2,TEXT_COL,122,160)
            draw_text("avoir au minimum 100M de gravas et avoir ",font2,TEXT_COL,130,190)
            draw_text("réussi à répondre à tout les questions débloquable",font2,TEXT_COL,115,220)

    #rafraichissement de la page + l'affichage des images importantes
    pygame.display.flip()
    screen.fill((160,195,195))
    screen.blit(background1,(0,0))
    screen.blit(gravas,(290,10))
#l'animation de chaque clic
    if animation==True:
        if animating==True:
            screen.blit(animation_frames[current_frame], (220, 120))
        frame_counter += 1
        if frame_counter >= animation_speed:
            frame_counter = 0
            current_frame += 1

            if current_frame >= len(animation_frames):
                animating = False

    screen.blit(image,(385, 155))
    #cheat code
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]:
        score += 100000
    if pressed[pygame.K_RIGHT]:
        score=0
    if pressed[pygame.K_m]:
        skipped=True



    #L'affichage du score
    if score < 1000:
        score_str = "Gravas : " + str(score)
    elif score < 1000000:
        score_str = "Gravas : " + str(round(score/1000,2)) + "k"
    else:
        score_str = "Gravas : " + str(round(score/1000000,2))+"M"
    #L'affichage des multiplicateurs et score
    multi_str=str(multi)
    texte_multi= police.render("x"+multi_str,True,(255,255,255))
    screen.blit(texte_multi,(589,0))
    texte_score = police.render(score_str,True,(255,255,255))
    screen.blit(texte_score,(375,25))
pygame.quit()


