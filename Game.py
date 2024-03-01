## TODO Seta para indicar de quem é o turno.
## TODO Imagem para girar o tambor.
## TODO Animações.
## TODO Interações direto pelo teclado (sem botões).
## TODO Botão 'Mais' no menu inicial.

from tkinter import *
from PIL import Image, ImageTk
import random as rd
from time import *

cont = 0
txts = ['Olha só quem resolveu aparecer! Há quanto tempo não te vejo!',
        'Lembra de mim? Não? Que pena. Sou Vorgoth, o diabo que você fez um acordo há muito tempo atrás.',
        'Qual foi seu desejo mesmo?',
        'Já faz muito tempo... Não me lembro mais.',
        'Mas vamos ao que interessa! ',
        'Você me procurou no passado, oferecendo sua alma em troca de algo que não lembramos.',
        'Espero que tenha aproveitado seja lá o que pediu, pois vim cobrar minha dívida!',
        'Para sua sorte, ando muito entediado recentemente...',
        'Preciso de emoção, então resolvi que vamos jogar um jogo.',
        'Um jogo de roleta russa! Sabe como funciona né?',
        'Um revólver, uma bala. Gire o tambor, aperte o gatilho. Quem tiver a sorte de levar o tiro, perde!',
        'Se você vencer, sua dívida será perdoada. Se perder, coleto sua alma e sigo minha vida.',
        '...',
        'Ah, quase me esqueci! Para deixar o jogo mais interessante, você vai girar o tambor antes de cada disparo!']

txts_CpuTurn = ['Finalmente um pouco de emoção!', 
                'HaHaHa, vamos de novo!!!', 
                'As coisas estão ficando interessantes...', 
                'Quanta adrenalina!!',
                'Parece que estou com sorte hoje!']

txts_PlayerTurn = ['Ops, parece que você escapou desta vez.',
                   'Poxa, isso foi anticlimático.',
                   'Uau! Você está vivo! Por enquanto...',
                   'Vamos ver até quando sua sorte vai durar...',
                   'Maldito... Me da essa arma logo.']

bullets = [0]*6 # Cada index da lista simula uma possivel bala da arma
bullets[rd.randint(0,5)] = 1 # 0 posição vazia, 1 posição carregada

window = Tk()

class Game(): 
    def __init__(self):
        self.window = window
        self.frame = Frame(window,bg='#040404') # Primeiro Frame / Menu
        self.Window()
        self.FirstScreen()
        window.mainloop()

    def Window(self):
        self.window.title("Vorgoth")        
        self.window.geometry("1024x1024")
        self.window.resizable(True,True)
        self.window.attributes('-fullscreen', True) # Adicionar Botão no menu para Usuario escolher

    def FirstScreen(self):
        self.frame.pack(fill=BOTH,expand=True)
        self.Txt_Title = Label(self.frame,text="VORGOTH",
                               bg='#040404',
                               fg='#e00a0b',font=('Niagara Solid',100,'underline'),justify=CENTER,
                               padx=10,pady=10,underline=8
                               )
        self.Txt_Title.pack(side=TOP,pady=100)

        self.button_Start = Button(self.frame,
                                  command=self.SecondScreen,
                                  bd=2,borderwidth=3,relief='ridge',width=10,height=1,
                                  background='#1f0404',padx=10,pady=10,
                                  foreground= '#e00a0b', font=('Niagara Solid',20), text='Inicio',justify='center',
                                  highlightbackground='#e00a0b',activebackground='#e00a0b',
                                  cursor='pirate')

        self.button_Quit = Button(self.frame,
                                  command=self.window.destroy,
                                  bd=2,borderwidth=3,relief='ridge',width=10,height=1,
                                  background='#1f0404',padx=10,pady=10,
                                  foreground= '#e00a0b', font=('Niagara Solid',20), text='Sair',justify='center',
                                  highlightbackground='#e00a0b',activebackground='#e00a0b',
                                  cursor='pirate')

        self.button_Start.place(relx=0.5, rely=0.5, anchor=CENTER)  # Center horizontally and vertically
        self.button_Quit.place(relx=0.5, rely=0.6, anchor=CENTER)

        self.Credits = Label(self.frame,text='Made by Luis Castanho', 
                            bg='#040404',
                            fg='#e00a0b',font=('Niagara Solid',20,),justify=CENTER,)
        self.Credits.pack(side=BOTTOM,pady=10)

    def change_txt(self):  #Função para alterar os textos que aparecem em historia
        global cont
        cont+=1
        if cont < len(txts):
            self.txt_historia.config(text=txts[cont])
        else: # Quando os textos chegam ao fim
            self.button_next.destroy()
            self.txt_historia.config(text='Esta pronto para jogar?')
            self.buttonYes = Button(self.frame,text='Sim',command=self.ifYes,
                                  bd=2,borderwidth=3,relief='ridge',
                                  background='#040404',padx=10,
                                  foreground= 'WHITE', font=('Arial',16),
                                  width=2,height=1
                                  )
            self.buttonNo = Button(self.frame,text='Não',command=self.ifNo,
                                  bd=2,borderwidth=3,relief='ridge',
                                  background='#040404',padx=10,
                                  foreground= 'WHITE', font=('Arial',16),
                                  width=2,height=1
                                  )
            self.buttonYes.place(relx=0.45, rely=0.99, anchor='s')
            self.buttonNo.place(relx=0.55, rely=0.99, anchor='s')
    
    def SecondScreen(self):
        self.frame.destroy()

        self.frame = Frame(window,bg='#040404') # Segundo Frame / Introdução
        self.frame.pack(fill=BOTH,expand=True)

        image = Image.open("D:\Estudos\Codes\Russian-Roulet-Game\Imagens\Vorgoth.jpg") # Carrega Imagem
        photo = ImageTk.PhotoImage(image)
        label_image = Label(self.frame, image=photo,bd=-1,width=600,height=600) 
        label_image.image = photo
        label_image.pack(side=TOP,expand=True)

        self.txt_historia = Label(self.frame,text=txts[cont],
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
        self.txt_historia.config(text='Muito bem, vamos lá!')
        self.window.after(2000, lambda: self.ThirdScreen())

    def ifNo(self):
        self.txt_historia.config(text='Você não tem escolha.')
        self.window.after(2000, lambda: self.ThirdScreen())

    def RR_PlayerTurn(self):
        global bullets,txts_PlayerTurn
        self.button_play.config(state=DISABLED)
        
        if bullets[0] == 1:
            image = Image.open("D:\Estudos\Codes\Russian-Roulet-Game\Imagens\BANG!.jpg") 
            photo = ImageTk.PhotoImage(image)
            self.label_Shoot.config(image=photo,width=500,height=500)
            self.label_Shoot.image = photo
            self.label_Shoot.place(relx=0.5,rely=0.5,anchor='center')

            self.txt_game.config(text='HaHaHa, sua alma é minha agora!')
            self.frame.after(5000, self.window.destroy)
        else:
            self.label_Shoot.config(bg='#010200',bd=-1,text='*click*',font=('Niagara Solid',50,'bold'),fg='WHITE')
            self.label_Shoot.place(relx=0.5,rely=0.5,anchor='center')

            self.frame.after(2000, lambda: self.txt_game.config(text=txts_PlayerTurn[rd.randint(0,len(txts_CpuTurn)-1)]))
            self.frame.after(4500, lambda: self.label_Shoot.config(text=''))
            self.frame.after(5500, lambda: self.txt_game.config(text='Minha vez agora!'))
            self.frame.after(8000, self.RR_CpuTurn)
    
    def RR_CpuTurn(self):
        global bullets,txts_CpuTurn

        if bullets[1] == 1:
            image = Image.open("D:\Estudos\Codes\Russian-Roulet-Game\Imagens\BANG!.jpg") 
            photo = ImageTk.PhotoImage(image)
            self.label_Shoot.config(image=photo,width=500,height=500)
            self.label_Shoot.image = photo
            self.label_Shoot.place(relx=0.5,rely=0.5,anchor='center')
            
            self.txt_game.config(text='Você deu sorte... mas fizemos um acordo, então agora você está livre.')
            self.frame.after(5000, self.window.destroy)
        else:
            self.label_Shoot.config(bg='#010200',bd=-1,text='*click*',font=('Niagara Solid',50,'bold'),fg='WHITE')
            self.label_Shoot.place(relx=0.5,rely=0.5,anchor='center')

            self.frame.after(2000, lambda:self.txt_game.config(text=txts_CpuTurn[rd.randint(0,len(txts_CpuTurn)-1)]))
            self.frame.after(4500, lambda: self.label_Shoot.config(text=''))
            self.frame.after(5500, lambda: self.txt_game.config(text='Sua vez agora! Gire de novo.'))
            self.frame.after(5002, lambda: self.button_spin.config(state=ACTIVE))

    def spinGun(self):
        global bullets
        self.button_spin.config(state=DISABLED)
        rd.shuffle(bullets)

        label_spinning = Label(self.frame,text='...........',bg='#040404',fg='WHITE',font=('Arial',16),pady=10,padx=10,relief='ridge')
        label_spinning.place(relx=0.5, rely=0.5, anchor='center')
    

        self.frame.after(2000, lambda: label_spinning.destroy())
        self.frame.after(2001, lambda: self.button_play.config(state=ACTIVE))
        
        self.frame.after(2200, lambda: self.txt_game.config(text='Agora é só atirar!'))

    def ThirdScreen(self):
        self.frame.destroy()
        self.frame = Frame(window,bg='#010200') # Terceiro Frame / Jogo 
        self.frame.pack(fill=BOTH,expand=True)
        
        image1 = Image.open("D:\Estudos\Codes\Russian-Roulet-Game\Imagens\Vorgoth_semArma.jpg") # Carrega a imagem canto superior direito (Vorgoth)
        photo = ImageTk.PhotoImage(image1)
        label_image1 = Label(self.frame,image=photo,width=350,height=350)
        label_image1.image = photo
        label_image1.place(relx=1,rely=0,anchor='ne')

        image2 = Image.open("D:\Estudos\Codes\Russian-Roulet-Game\Imagens\Sombra.jpg") # Carrega a imagem canto inferior esquerdo (Sombra)
        photo = ImageTk.PhotoImage(image2)
        label_image2 = Label(self.frame,image=photo,width=500,height=400)
        label_image2.image = photo
        label_image2.place(relx=0.07,rely=1,anchor='sw')

        self.txt_game = Label(self.frame,text='É só girar o tambor e apertar o gatilho!',
                                bg='#040404',fg='WHITE',font=('Arial',16),pady=20,padx=10,relief='ridge')
        self.txt_game.pack(side=TOP,fill=X,anchor='n',padx=400,pady=125)

        self.label_Shoot = Label(self.frame)
        self.button_spin = Button(self.frame, text='GIRAR', command=self.spinGun,
                                bd=2, borderwidth=3, relief='ridge',
                                background='#040404', padx=10,
                                foreground='WHITE', font=('Arial', 16),
                                width=5, height=2, justify='center',
                                highlightbackground='#040404',
                                activebackground='#040404',
                                activeforeground='WHITE')

        self.button_play = Button(self.frame,text='ATIRAR',command=self.RR_PlayerTurn,
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
