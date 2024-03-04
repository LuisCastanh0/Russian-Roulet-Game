## TODO Seta para indicar de quem é o turno.
## TODO Imagem para girar o tambor.
## TODO Interações direto pelo teclado (sem botões).
## TODO Permitir que o usuário digite seu desejo no meio do diálogo.

from tkinter import *
from PIL import Image, ImageTk
import random as rd
from time import *
import os

# Função para ler o texto do arquivo
def read_dialogue(filename):
    with open(filename, 'r',encoding='utf-8') as file:
        return [line.rstrip() for line in file.readlines()] # Remove a quebra de linha
    
def read_dialogue_words(filename, delimiter='='):
    with open(filename, 'r', encoding='utf-8') as file:
        lines = [line.strip() for line in file.readlines()]
        dialogues = {}
        for line in lines:
            key, value = line.split(delimiter)
            dialogues[key.strip()] = value.strip()
        return dialogues

path = os.path.dirname(os.path.abspath(__file__))
cont = 0
language = 'txtsPT'
txts_Game = read_dialogue_words(os.path.join(path,"textos",language,"txt_Game.txt"))
txts_VorgothMono = read_dialogue(os.path.join(path,"textos",language,"txt_VorgothMonologue.txt"))
txts_CpuTurn = read_dialogue(os.path.join(path,"textos",language,"txt_CpuTurn.txt"))
txts_PlayerTurn = read_dialogue(os.path.join(path,"textos",language,"txt_PlayerTurn.txt"))

bullets = [0]*6 # Cada index da lista simula uma possivel bala da arma
bullets[rd.randint(0,5)] = 1 # 0 posição vazia, 1 posição carregada

window = Tk()

class Game(): 
    def __init__(self):
        self.window = window
        self.Window()
        self.frame = Frame(window)
        self.MenuScreen()
        window.mainloop()

    def Window(self):
        self.window.title("Vorgoth")        
        self.window.attributes('-fullscreen', True) # Adicionar Botão no menu para Usuario escolher
        global txts_Game

    def MenuScreen(self):
        self.frame.destroy()
        self.frame = Frame(window,bg='#040404') # Primeiro Frame / Menu
        self.frame.pack(fill=BOTH,expand=True)
        self.Txt_Title = Label(self.frame,text="VORGOTH",
                               bg='#040404',
                               fg='#e00a0b',font=('Niagara Solid',100,'underline'),justify=CENTER,
                               padx=10,pady=10,underline=8
                               )
        self.Txt_Title.pack(side=TOP,pady=100)

        self.button_Start = Button(self.frame,
                                  command=self.DialogueScreen,
                                  bd=2,borderwidth=3,relief='ridge',width=10,height=1,
                                  background='#1f0404',padx=10,pady=10,
                                  foreground= '#e00a0b', font=('Niagara Solid',25), text=txts_Game['start'],justify='center',
                                  highlightbackground='#e00a0b',activebackground='#e00a0b',
                                  cursor='pirate')

        self.button_Options = Button(self.frame,
                                  command=self.OptionsScreen,
                                  bd=2,borderwidth=3,relief='ridge',width=10,height=1,
                                  background='#1f0404',padx=10,pady=10,
                                  foreground= '#e00a0b', font=('Niagara Solid',25), text=txts_Game['options'],justify='center',
                                  highlightbackground='#e00a0b',activebackground='#e00a0b',
                                  cursor='pirate')
        
        self.button_Quit = Button(self.frame,
                                  command=self.window.destroy,
                                  bd=2,borderwidth=3,relief='ridge',width=10,height=1,
                                  background='#1f0404',padx=10,pady=10,
                                  foreground= '#e00a0b', font=('Niagara Solid',25), text=txts_Game['quit'],justify='center',
                                  highlightbackground='#e00a0b',activebackground='#e00a0b',
                                  cursor='pirate')

        self.button_Start.place(relx=0.5, rely=0.5, anchor=CENTER)  # Center horizontally and vertically
        self.button_Options.place(relx=0.5, rely=0.6, anchor=CENTER)
        self.button_Quit.place(relx=0.5,rely=0.7,anchor=CENTER)

        self.Credits = Label(self.frame,text=txts_Game['made_by'], 
                            bg='#040404',
                            fg='#e00a0b',font=('Niagara Solid',20,),justify=CENTER,)
        self.Credits.pack(side=BOTTOM,pady=10)

    def OptionsScreen(self): 
        self.frame.destroy()
        self.frame = Frame(window,bg='#040404') # Segundo Frame / Introdução
        self.frame.pack(fill=BOTH,expand=True)

        self.Txt_Options = Label(self.frame,text=txts_Game['options'],
                               bg='#040404',
                               fg='#e00a0b',font=('Niagara Solid',100,'underline'),justify=CENTER,
                                padx=10,pady=10,underline=8
                               )
        self.Txt_Options.pack(side=TOP,pady=100)

        self.button_Idiomas = Button(self.frame,
                                  command=self.LanguageScreen,
                                  bd=2,borderwidth=3,relief='ridge',width=10,height=1,
                                  background='#1f0404',padx=10,pady=10,
                                  foreground= '#e00a0b', font=('Niagara Solid',25), text=txts_Game['language'],justify='center',
                                  highlightbackground='#e00a0b',activebackground='#e00a0b',
                                  cursor='pirate') 
        
        self.button_Return = Button(self.frame,
                                    command=self.MenuScreen, text=txts_Game['return'],
                                    bd=2,borderwidth=3,relief='ridge',width=10,height=1,
                                    background='#1f0404',padx=10,pady=10,
                                    foreground= '#e00a0b', font=('Niagara Solid',25),justify='center',
                                    highlightbackground='#e00a0b',activebackground='#e00a0b',
                                    cursor='pirate')
        
        self.button_Idiomas.place(relx=0.5,rely=0.3,anchor=CENTER)
        self.button_Return.place(relx=0.5,rely=0.8,anchor=CENTER)

    def ChangeLanguage_PT(self): # Função utilizada para alterar o idioma do jogo
        global language,txts_Game,txts_CpuTurn,txts_PlayerTurn,txts_VorgothMono
        language = "txtsPT"
        txts_Game = read_dialogue_words(os.path.join(path,"textos",language,"txt_Game.txt"))
        txts_VorgothMono = read_dialogue(os.path.join(path,"textos",language,"txt_VorgothMonologue.txt"))
        txts_CpuTurn = read_dialogue(os.path.join(path,"textos",language,"txt_CpuTurn.txt"))
        txts_PlayerTurn = read_dialogue(os.path.join(path,"textos",language,"txt_PlayerTurn.txt"))
        self.OptionsScreen()

    def ChangeLanguage_ENG(self): # Função utilizada para alterar o idioma do jogo
        global language,txts_Game,txts_CpuTurn,txts_PlayerTurn,txts_VorgothMono
        language = "txtsENG"
        txts_Game = read_dialogue_words(os.path.join(path,"textos",language,"txt_Game.txt"))
        txts_VorgothMono = read_dialogue(os.path.join(path,"textos",language,"txt_VorgothMonologue.txt"))
        txts_CpuTurn = read_dialogue(os.path.join(path,"textos",language,"txt_CpuTurn.txt"))
        txts_PlayerTurn = read_dialogue(os.path.join(path,"textos",language,"txt_PlayerTurn.txt"))
        self.OptionsScreen()

    def LanguageScreen(self): 
        self.frame.destroy()
        self.frame = Frame(window,bg='#040404') # Segundo Frame / Introdução
        self.frame.pack(fill=BOTH,expand=True)

        self.Txt_Options = Label(self.frame,text=txts_Game['language'],
                               bg='#040404',
                               fg='#e00a0b',font=('Niagara Solid',100,'underline'),justify=CENTER,
                                padx=10,pady=10,underline=8
                               )
        self.Txt_Options.pack(side=TOP,pady=100)

        self.button_ENG = Button(self.frame,
                                  command=self.ChangeLanguage_ENG, text="English",
                                  bd=2,borderwidth=3,relief='ridge',width=10,height=1,
                                  background='#1f0404',padx=10,pady=10,
                                  foreground= '#e00a0b', font=('Niagara Solid',25),justify='center',
                                  highlightbackground='#e00a0b',activebackground='#e00a0b',
                                  cursor='pirate')
        self.button_PT = Button(self.frame,
                                  command=self.ChangeLanguage_PT, text="Português",
                                  bd=2,borderwidth=3,relief='ridge',width=10,height=1,
                                  background='#1f0404',padx=10,pady=10,
                                  foreground= '#e00a0b', font=('Niagara Solid',25),justify='center',
                                  highlightbackground='#e00a0b',activebackground='#e00a0b',
                                  cursor='pirate')
        
        self.button_Return = Button(self.frame,
                                    command=self.OptionsScreen, text=txts_Game['return'],
                                    bd=2,borderwidth=3,relief='ridge',width=10,height=1,
                                    background='#1f0404',padx=10,pady=10,
                                    foreground= '#e00a0b', font=('Niagara Solid',25),justify='center',
                                    highlightbackground='#e00a0b',activebackground='#e00a0b',
                                    cursor='pirate')
        
        self.button_ENG.place(relx=0.5,rely=0.3,anchor=CENTER)
        self.button_PT.place(relx=0.5,rely=0.4,anchor=CENTER)
        self.button_Return.place(relx=0.5,rely=0.8,anchor=CENTER)

    def change_txt(self):  # Função utilizada para alterar os textos de DialogueScreen
        global cont
        cont+=1
        if cont < len(txts_VorgothMono):
            self.txt_historia.config(text=txts_VorgothMono[cont])
        else: # Quando os textos chegam ao fim
            self.button_next.destroy()
            self.txt_historia.config(text=txts_Game['ready_to_play'])
            self.buttonYes = Button(self.frame,text=txts_Game['yes'],command=self.ifYes,
                                  bd=2,borderwidth=3,relief='ridge',
                                  background='#040404',padx=10,
                                  foreground= 'WHITE', font=('Arial',16),
                                  width=2,height=1
                                  )
            self.buttonNo = Button(self.frame,text=txts_Game['no'],command=self.ifNo,
                                  bd=2,borderwidth=3,relief='ridge',
                                  background='#040404',padx=10,
                                  foreground= 'WHITE', font=('Arial',16),
                                  width=2,height=1
                                  )
            self.buttonYes.place(relx=0.45, rely=0.99, anchor='s')
            self.buttonNo.place(relx=0.55, rely=0.99, anchor='s')
    
    def DialogueScreen(self):
        self.frame.destroy()

        self.frame = Frame(window,bg='#040404') # Segundo Frame / Introdução
        self.frame.pack(fill=BOTH,expand=True)

        image = Image.open(os.path.join(path,'Imagens','Vorgoth.jpg')) # Carrega Imagem
        photo = ImageTk.PhotoImage(image)
        label_image = Label(self.frame, image=photo,bd=-1,width=600,height=600) 
        label_image.image = photo
        label_image.pack(side=TOP,expand=True)

        self.txt_historia = Label(self.frame,text=txts_VorgothMono[cont],
                                bg='#040404',fg='WHITE',font=('Arial',18),pady=50,relief='ridge') # Label onde os textos para a introdução são mostrados
        self.txt_historia.pack(side=BOTTOM,fill=X,pady=100,padx=100) 
        
        self.button_next = Button(self.frame,text='>>>',command=self.change_txt,
                                  bd=2,borderwidth=3,relief='ridge',
                                  background='#040404',padx=10,
                                  foreground= 'WHITE', font=('Arial',16),
                                  width=2,height=1
                                  ) # Avança o texto em txt_historia
        self.button_next.place(relx=0.95, rely=0.99, anchor='se')
        
    def ifYes(self):
        self.txt_historia.config(text=txts_Game['lets_go'])
        self.window.after(2000, lambda: self.GameScreen())

    def ifNo(self):
        self.txt_historia.config(text=txts_Game['no_choice'])
        self.window.after(2000, lambda: self.GameScreen())

    def RR_PlayerTurn(self):
        global bullets,txts_PlayerTurn
        self.button_play.config(state=DISABLED)
        
        if bullets[0] == 1:
            image = Image.open(os.path.join(path,'Imagens','BANG!.jpg')) 
            photo = ImageTk.PhotoImage(image)
            self.label_Shoot.config(image=photo,width=500,height=500)
            self.label_Shoot.image = photo
            self.label_Shoot.place(relx=0.5,rely=0.5,anchor='center')

            self.txt_game.config(text=txts_Game['loss'])
            self.frame.after(5000, self.window.destroy)
        else:
            self.label_Shoot.config(bg='#010200',bd=-1,text='*click*',font=('Niagara Solid',50,'bold'),fg='WHITE')
            self.label_Shoot.place(relx=0.5,rely=0.5,anchor='center')

            self.frame.after(2000, lambda: self.txt_game.config(text=txts_PlayerTurn[rd.randint(0,len(txts_CpuTurn)-1)]))
            self.frame.after(4500, lambda: self.label_Shoot.config(text=''))
            self.frame.after(5500, lambda: self.txt_game.config(text=txts_Game['Cpu_turn']))
            self.frame.after(8000, self.RR_CpuTurn)
    
    def RR_CpuTurn(self):
        global bullets,txts_CpuTurn

        if bullets[1] == 1:
            image = Image.open(os.path.join(path,'Imagens',"BANG!.jpg")) 
            photo = ImageTk.PhotoImage(image)
            self.label_Shoot.config(image=photo,width=500,height=500)
            self.label_Shoot.image = photo
            self.label_Shoot.place(relx=0.5,rely=0.5,anchor='center')
            
            self.txt_game.config(text=txts_Game['win'])
            self.frame.after(5000, self.window.destroy)
        else:
            self.label_Shoot.config(bg='#010200',bd=-1,text='*click*',font=('Niagara Solid',50,'bold'),fg='WHITE')
            self.label_Shoot.place(relx=0.5,rely=0.5,anchor='center')

            self.frame.after(2000, lambda:self.txt_game.config(text=txts_CpuTurn[rd.randint(0,len(txts_CpuTurn)-1)]))
            self.frame.after(4500, lambda: self.label_Shoot.config(text=''))
            self.frame.after(5500, lambda: self.txt_game.config(text=txts_Game['Player_turn']))
            self.frame.after(5002, lambda: self.button_spin.config(state=ACTIVE))

    def spinGun(self):
        global bullets
        self.button_spin.config(state=DISABLED)
        rd.shuffle(bullets)

        label_spinning = Label(self.frame,text='...........',bg='#040404',fg='WHITE',font=('Arial',16),pady=10,padx=10,relief='ridge')
        label_spinning.place(relx=0.5, rely=0.5, anchor='center')
    
        self.frame.after(2000, lambda: label_spinning.destroy())
        self.frame.after(2001, lambda: self.button_play.config(state=ACTIVE))
        
        self.frame.after(2200, lambda: self.txt_game.config(text=txts_Game['instructions2']))

    def GameScreen(self):
        self.frame.destroy()
        self.frame = Frame(window,bg='#010200') # Terceiro Frame / Jogo 
        self.frame.pack(fill=BOTH,expand=True)
        
        image1 = Image.open(os.path.join(path,'Imagens','Vorgoth_semArma.jpg')) # Carrega a imagem canto superior direito (Vorgoth)
        photo = ImageTk.PhotoImage(image1)
        label_image1 = Label(self.frame,image=photo,width=350,height=350)
        label_image1.image = photo
        label_image1.place(relx=1,rely=0,anchor='ne')

        image2 = Image.open(os.path.join(path,'Imagens','Sombra.jpg')) # Carrega a imagem canto inferior esquerdo (Sombra)
        photo = ImageTk.PhotoImage(image2)
        label_image2 = Label(self.frame,image=photo,width=500,height=400)
        label_image2.image = photo
        label_image2.place(relx=0.07,rely=1,anchor='sw')

        self.txt_game = Label(self.frame,text=txts_Game['instructions'],
                                bg='#040404',fg='WHITE',font=('Arial',16),pady=20,padx=10,relief='ridge')
        self.txt_game.pack(side=TOP,fill=X,anchor='n',padx=400,pady=125)

        self.label_Shoot = Label(self.frame)
        self.button_spin = Button(self.frame, text=txts_Game['spin'], command=self.spinGun,
                                bd=2, borderwidth=3, relief='ridge',
                                background='#040404', padx=10,
                                foreground='WHITE', font=('Arial', 16),
                                width=5, height=2, justify='center',
                                highlightbackground='#040404',
                                activebackground='#040404',
                                activeforeground='WHITE')

        self.button_play = Button(self.frame,text=txts_Game['shoot'],command=self.RR_PlayerTurn,
                                bd=2, borderwidth=3, relief='ridge',
                                background='#040404', padx=10,
                                foreground='WHITE', font=('Arial', 16),
                                width=5, height=2, justify='center',
                                highlightbackground='#040404',
                                activebackground='#040404',
                                activeforeground='WHITE')
        
        self.button_play.place(relx=0.55,rely=0.9,anchor='s')
        self.button_spin.place(relx=0.45,rely=0.9,anchor='s')
        self.button_play.config(state=DISABLED)
        

Game()    
