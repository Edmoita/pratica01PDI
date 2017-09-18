from tkinter import *
from tkinter import filedialog
from transformations import *
from utils import *

class Application(Frame):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        # Configurar janela
        self.master.title("PDI - Prática 01 - Transformação de Imagens")
        self.master.geometry("1600x1200+300+300")
        # Criar menu
        self.create_menu()
        # Criar labels onde ficarão as figuras
        self.create_image_labels()
        # Criar label que identifica a transformação transformação
        self.lbl_transform = Label(self.master, text='Transformação', font=('', 18), justify=CENTER)
        self.lbl_transform.place(x=520, y=80)
        # Criar a label de fórmula
        self.lbl_formula = Label(self.master, text='Fórmula')
        self.lbl_formula.place(x=600, y=130)
        '''
        # Limiar m
        self.lbl_threshold = Label(self.master, text='m (limiar)', width=10, justify=LEFT)
        self.lbl_threshold.place(x=520, y=200)
        self.txt_threshold = Entry(self.master, bd=5, state=DISABLED)
        self.txt_threshold.place(x=610, y=200)
        # Inclinação E
        self.lbl_E = Label(self.master, text='E (inclinação)', width=10, justify=LEFT)
        self.lbl_E.place(x=500, y=240)
        self.txt_E = Entry(self.master, bd=5, state=DISABLED)
        self.txt_E.place(x=610, y=240)
        '''
        # Novo mínimo
        self.lbl_min = Label(self.master, text='Novo mínimo', width=20, justify=LEFT)
        self.lbl_min.place(x=485, y=200)
        self.txt_min = Entry(self.master, bd=5, state=DISABLED)
        self.txt_min.place(x=610, y=200)
        # Novo máximo
        self.lbl_max = Label(self.master, text='Novo máximo', width=20, justify=LEFT)
        self.lbl_max.place(x=485, y=240)
        self.txt_max = Entry(self.master, bd=5, state=DISABLED)
        self.txt_max.place(x=610, y=240)
        # Constante c
        self.lbl_constant = Label(self.master, text='c', width=10, justify=LEFT)
        self.lbl_constant.place(x=520, y=280)
        self.txt_constant = Entry(self.master, bd=5, state=DISABLED)
        self.txt_constant.place(x=610, y=280)
        # Gamma y
        self.lbl_gamma = Label(self.master, text='y (gamma)', width=10, justify=LEFT)
        self.lbl_gamma.place(x=520, y=320)
        self.txt_gamma = Entry(self.master, bd=5, state=DISABLED)
        self.txt_gamma.place(x=610, y=320)
        # Bit plane layer
        self.lbl_bit = Label(self.master, text='Plano de Bits', width=20, justify=LEFT)
        self.lbl_bit.place(x=485, y=360)
        self.txt_bit = Entry(self.master, bd=5, state=DISABLED)
        self.txt_bit.place(x=610, y=360)
        # Botão Transformar
        self.btn_transform = Button(self.master, text='TRANSFORMAR', state=DISABLED, relief=RAISED, bd='4')
        self.btn_transform.place(x=630, y=490)

    def create_menu(self):
        menubar = Menu(self.master)
        self.master.config(menu=menubar)
        filemenu = Menu(menubar)
        filemenu.add_command(label='Carregar imagem', command=self.load_image)
        filemenu.add_separator()
        filemenu.add_command(label='Q1', command=self.q1)
        filemenu.add_command(label='Q2', command=self.q2)
        filemenu.add_command(label='Q3', command=self.q3)
        filemenu.add_command(label='Q4', command=self.q4)
        filemenu.add_command(label='Q5', command=self.q5)
        filemenu.add_separator()
        filemenu.add_command(label='Sair', command=self.on_exit)
        menubar.add_cascade(label='File', menu=filemenu)

    def create_image_labels(self):
        self.orig_img = Label(self.master, text="Figura Original")
        self.orig_img['bg'] = 'white'
        self.orig_img['padx'] = 20
        self.orig_img['width'] = 51
        self.orig_img['height'] = 21
        self.orig_img['borderwidth'] = 2
        self.orig_img['relief'] = RAISED
        self.orig_img.place(x=30, y=150)
        # Criar Figura Transformada vazia
        self.empty_transf()

    def empty_transf(self):
        self.new_img = Label(self.master, text="Figura Transformada")
        self.new_img['bg'] = 'white'
        self.new_img['width'] = 51
        self.new_img['height'] = 21
        self.new_img['padx'] = 20
        self.new_img['borderwidth'] = 2
        self.new_img['relief'] = RAISED
        self.new_img.place(x=880, y=150)

    def create_original_image(self, img=None):
        self.orig_img = Label(self.master, image=img, bg='white')
        self.orig_img.image = img
        self.orig_img['padx'] = 20
        self.orig_img['width'] = 450
        self.orig_img['height'] = 300
        self.orig_img['borderwidth'] = 2
        self.orig_img['relief'] = RAISED
        self.orig_img.place(x=30, y=150)

    def create_transformed_image(self, img=None):
        self.new_img = Label(self.master, image=img, bg='white')
        self.new_img.image = img
        self.new_img['width'] = 450
        self.new_img['height'] = 300
        self.new_img['padx'] = 20
        self.new_img['borderwidth'] = 2
        self.new_img['relief'] = RAISED
        self.new_img.place(x=880, y=150)

    def load_image(self):
        image_types =[ ( "Image files",("*.jpg", "*.jpeg", "*.png", "*.gif") ), ("All files", ("*.*"))]
        dlg = filedialog.Open(self, initialdir = 'images', filetypes = image_types)
        self.filename = dlg.show()
        opencv_image = load_opencv_image(self.filename)
        tk_image = convert_image_opencv_to_tk(opencv_image)
        self.create_original_image(tk_image)

    def disable_entries(self):
        '''
        self.txt_threshold['state'] = DISABLED
        self.txt_E['state'] = DISABLED
        '''
        self.txt_min['state'] = DISABLED
        self.txt_max['state'] = DISABLED
        self.txt_constant['state'] = DISABLED
        self.txt_gamma['state'] = DISABLED
        self.txt_bit['state'] = DISABLED
        self.empty_transf()

    def q1(self):
        self.disable_entries()
        self.lbl_transform['text'] = 'ALARGAMENTO DE CONTRASTE'
        self.btn_transform['state'] = NORMAL
        '''
        self.lbl_formula['text'] = 's = 1/(1 + (m/r)^E)'
        self.txt_threshold['state'] = NORMAL
        self.txt_E['state'] = NORMAL
        '''
        self.lbl_formula['text'] = 's = (r - novo_minimo) * (255 / (novo_maximo - novo_minimo))'
        self.txt_min['state'] = NORMAL
        self.txt_max['state'] = NORMAL
        self.btn_transform['command'] = self.transf_q1

    def q2(self):
        self.disable_entries()
        self.lbl_transform['text'] = 'TRANSFORMAÇÃO LOGARÍTMICA'
        self.lbl_formula['text'] = 's = c * log(1+r)'
        self.btn_transform['state'] = NORMAL
        self.txt_constant['state'] = NORMAL
        self.btn_transform['command'] = self.transf_q2

    def q3(self):
        self.disable_entries()
        self.lbl_transform['text'] = 'TRANSFORMAÇÃO DE POTÊNCIA'
        self.lbl_formula['text'] = 's = c * r^y'
        self.btn_transform['state'] = NORMAL
        self.txt_constant['state'] = NORMAL
        self.txt_gamma['state'] = NORMAL
        self.btn_transform['command'] = self.transf_q3

    def q4(self):
        self.disable_entries()
        self.lbl_transform['text'] = 'FATIAMENTO NO PLANO DE BITS'
        self.lbl_formula['text'] = 's = n-esimo bit de r'
        self.btn_transform['state'] = NORMAL
        self.txt_bit['state'] = NORMAL
        self.btn_transform['command'] = self.transf_q4

    def q5(self):
        self.disable_entries()
        self.lbl_transform['text'] = 'NEGATIVO - RAIO X'
        self.lbl_formula['text'] = 's = L-1-r'
        self.btn_transform['state'] = NORMAL
        self.btn_transform['command'] = self.transf_q5

    def transf_q1(self):
        new_min = int(self.txt_min.get())
        self.txt_min.delete(0, END)
        new_max = int(self.txt_max.get())
        self.txt_max.delete(0, END)
        image = load_opencv_image(self.filename)
        new_image = imgCorrection(image, new_min, new_max)
        tk_image = convert_image_opencv_to_tk(new_image)
        self.create_transformed_image(tk_image)
        '''
        threshold = int(self.txt_threshold.get())
        self.txt_threshold.delete(0, END)
        E = float(self.txt_E.get())
        self.txt_E.delete(0, END)
        image = load_opencv_image(self.filename)
        new_image = contrastStretching(image, threshold, E)
        tk_image = convert_image_opencv_to_tk(new_image)
        self.create_transformed_image(tk_image)
        '''

    def transf_q2(self):
        constant = float(self.txt_constant.get())
        self.txt_constant.delete(0, END)
        image = load_opencv_image(self.filename)
        new_image = logarithmTransformation(image, constant)
        tk_image = convert_image_opencv_to_tk(new_image)
        self.create_transformed_image(tk_image)

    def transf_q3(self):
        constant = float(self.txt_constant.get())
        self.txt_constant.delete(0, END)
        gamma = float(self.txt_gamma.get())
        self.txt_gamma.delete(0, END)
        image = load_opencv_image(self.filename)
        new_image = gammaCorrection(image, gamma, constant)
        tk_image = convert_image_opencv_to_tk(new_image)
        self.create_transformed_image(tk_image)

    def transf_q4(self):
        bit = int(self.txt_bit.get())
        self.txt_bit.delete(0, END)
        image = load_opencv_image(self.filename)
        new_image = bitsLayer(image, bit)
        tk_image = convert_image_opencv_to_tk(new_image)
        self.create_transformed_image(tk_image)

    def transf_q5(self):
        image = load_opencv_image(self.filename)
        new_image = imgNegative(image)
        tk_image = convert_image_opencv_to_tk(new_image)
        self.create_transformed_image(tk_image)

    def on_exit(self):
        self.quit()

def main():

    root = Tk()
    app = Application()
    root.mainloop()

if __name__ == '__main__':
    main()
