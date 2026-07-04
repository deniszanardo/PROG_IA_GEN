


import tkinter  as tk
import calculos as cl
from tkinter import ttk

# procodding -> programação seu a IA 


def run_imc():
    peso_ = float(peso.get() )
    altura_ = float(altura.get())
    resultado = cl.imc(peso_, altura_)
    r  =  round(resultado, 2)
    return mostrar_imc.config(text = r) 


def run_calculo_h():
    carga_ = float(carga.get())
    salario_ = float(salario.get())
    resultado = cl.calculo_sal_hora(carga_, salario_)
    r  =  round(resultado, 2)
    return mostrar_sal.config(text=r)

def run_extra():
    q  =  int(quantidade.get())
    carga_ = float(carga.get())
    salario_ = float(salario.get())
    resultado = cl.calculo_sal_hora(carga_, salario_)
    r  =  round(resultado, 2)
    rs =  cl.calculo_quantidade_extra50(q, r)
    return mostrar_extra.config( text =  rs)
    


janela  = tk.Tk()
janela.geometry('350x1300')


espaco_imc = ttk.Frame(janela, width=180)
espaco_imc.grid(padx=10, pady=10)

tk.Label(espaco_imc, text =  'SISTEMA DE CALCULOS').grid()

texto1 = tk.Label(espaco_imc, text =  'Peso', font=('arial', 15))
texto1.grid(column=0, row=1)
peso = tk.Entry(espaco_imc,font=('arial', 10))
peso.grid(column=0,row=2)



texto2 = tk.Label(espaco_imc, text =  'Altura', font=('arial', 15))
texto2.grid(column=1, row=1)
altura = tk.Entry(espaco_imc,font=('arial', 10))
altura.grid(column=1, row=2)


bt_imc = tk.Button(espaco_imc, text =  'imc', font=('arial', 15), command=run_imc)
bt_imc.grid(pady=20)


mostrar_imc = tk.Label(janela, text = '', font=('arial', 15))
mostrar_imc.grid()

# -------------------------------------------
# função 2


espaco_salario  =  tk.Frame(janela)
espaco_salario.grid()

texto_sal =  tk.Label(espaco_salario, text='CALCULE A SALARIO HORA')
texto_sal.grid(column=0, row=3)


texto3 = tk.Label(espaco_salario, text =  'Carga', font=('arial', 15))
texto3.grid(column=0, row=4)
carga = tk.Entry(espaco_salario,font=('arial', 10))
carga.grid(column=0,row=5)



texto2 = tk.Label(espaco_salario, text =  'Salario', font=('arial', 15))
texto2.grid(column=1, row=4)
salario = tk.Entry(espaco_salario,font=('arial', 10))
salario.grid(column=1, row=5)


bt_sal = tk.Button(espaco_salario, text =  'Salario hora', font=('arial', 15), command=run_calculo_h)
bt_sal.grid(pady=20, column=1, row=6)

mostrar_sal = tk.Label(espaco_salario, text = '', font=('arial', 15))
mostrar_sal.grid(column=0,row=7)


# --------------------------------------------



espaco_quantidade  =  tk.Frame(janela)
espaco_quantidade.grid()

texto_sal =  tk.Label(espaco_salario, text='')
texto_sal.grid(column=0, row=9)


texto3 = tk.Label(espaco_salario, text =  'Quantidade', font=('arial', 15))
texto3.grid(column=0, row=9)
quantidade = tk.Entry(espaco_salario,font=('arial', 10))
quantidade.grid(column=0,row=10)



# texto2 = tk.Label(espaco_salario, text =  'Extra', font=('arial', 15))
# texto2.grid(column=1, row=7)
# salario = tk.Entry(espaco_salario,font=('arial', 10))
# salario.grid(column=1, row=8)


bt_ex = tk.Button(espaco_salario, text =  'Hora extra', font=('arial', 15), command=run_extra)
bt_ex.grid(pady=20, column=0,row=11)

mostrar_extra = tk.Label(espaco_salario, text = '', font=('arial', 15))
mostrar_extra.grid(column=0,row=13)




janela.mainloop()