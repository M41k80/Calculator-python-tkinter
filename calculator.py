import tkinter as tk
from tkinter import messagebox

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('500x380')
        self.resizable(0,0)
        self.title('Calculator By M41k80')
        self.iconbitmap('calculadora.ico')

        #atributos de clase
        self.expression = ''
        ## caja de texto
        self. input_1= None
        ## stringVar lo utilizamos para obtener el valor del imput
        self.text_input = tk.StringVar()
        # crear los componentes
        self._components_creation()

    #metodos clase
    #metodo para crear componentes
    def _components_creation(self):
        #creamos un frame para la caja de texto
        input_frame = tk.Frame(self, width=500, height=50, bg='grey')
        input_frame.pack(side=tk.TOP)
        #caja de texto
        input_2 = tk.Entry(input_frame, font=('arial', 18, 'bold'),
                           textvariable=self.text_input, width=44, justify=tk.RIGHT)
        input_2.grid(row=0, column=0, ipady=10)

        #creamos otro frame para la parte inferior
        bottons_frame = tk.Frame(self, width=400, height=450, bg='grey')
        bottons_frame.pack()

        #primer renglon
        #boton limpiar
        botton_clear = tk.Button(bottons_frame, text='CLEAR', width=38, height=3,
                                 bd=0, bg='#eee', cursor='hand2', command=self._clear_event)
        botton_clear.grid(row=0, column=0, columnspan=3, padx=1, pady=1)
        #boton dividir
        botton_division = tk.Button(bottons_frame, text='/', width=10, height=3, bd=0,
                                    bg='#eee', cursor='hand2', command=lambda: self._click_event('/')
                                    )
        botton_division.grid(row=0, column=3, padx=1, pady=1)
        #segundo renglon
        #boton 7
        botton_seven = tk.Button(bottons_frame, text='7', width=10, height=3, bd=0, bg='#fff',
                                 cursor='hand2', command=lambda: self._click_event(7))
        botton_seven.grid(row=1, column=0, padx=1, pady=1)
        #boton 8
        botton_eight = tk.Button(bottons_frame, text='8', width=10, height=3, bd=0, bg='#fff',
                                 cursor='hand2', command=lambda: self._click_event(8))
        botton_eight.grid(row=1, column=1, padx=1, pady=1)
        #boton 9
        botton_nine = tk.Button(bottons_frame, text='9', width=10, height=3, bd=0, bg='#fff',
                                cursor='hand2', command=lambda: self._click_event(9))
        botton_nine.grid(row=1, column=2, padx=1, pady=1)
        ## boton_multiplicacion
        botton_multiplication = tk.Button(bottons_frame, text='*', width=10, height=3, bd=0, bg='#fff',
                                         cursor='hand2', command=lambda: self._click_event('*'))
        botton_multiplication.grid(row=1, column=3, padx=1, pady=1)

        #tercer renglon
        #boton 4
        botton_four = tk.Button(bottons_frame, text='4', width=10, height=3, bd=0, bg='#fff',
                                cursor='hand2', command=lambda: self._click_event(4))
        botton_four.grid(row=2, column=0, padx=1, pady=1)
        #boton 5
        botton_five = tk.Button(bottons_frame, text='5', width=10, height=3, bd=0, bg='#fff',
                                cursor='hand2', command=lambda: self._click_event(5))
        botton_five.grid(row=2, column=1, padx=1, pady=1)
        # boton 6
        botton_six = tk.Button(bottons_frame, text='6', width=10, height=3, bd=0, bg='#fff',
                               cursor='hand2', command=lambda: self._click_event(6))
        botton_six.grid(row=2, column=2, padx=1, pady=1)
        # boton resta
        botton_subtraction = tk.Button(bottons_frame, text='-', width=10, height=3, bd=0, bg='#fff',
                                       cursor='hand2', command=lambda: self._click_event('-'))
        botton_subtraction.grid(row=2, column=3, padx=1, pady=1)

        ### cuarto renglon
        #boton 1
        botton_one = tk.Button(bottons_frame, text='1', width=10, height=3, bd=0, bg='#fff',
                               cursor='hand2', command=lambda: self._click_event(1))
        botton_one.grid(row=3, column=0, padx=1, pady=1)
        # boton 2
        botton_two = tk.Button(bottons_frame, text='2', width=10, height=3, bd=0, bg='#fff',
                               cursor='hand2', command=lambda: self._click_event(2))
        botton_two.grid(row=3, column=1, padx=1, pady=1)
        # boton 3
        botton_three = tk.Button(bottons_frame, text='3', width=10, height=3, bd=0, bg='#fff',
                                 cursor='hand2', command=lambda: self._click_event(3))
        botton_three.grid(row=3, column=2, padx=1, pady=1)
        #boton suma
        botton_addition = tk.Button(bottons_frame, text='+', width=10, height=3, bd=0, bg='#fff',
                                    cursor='hand2', command=lambda: self._click_event('+'))
        botton_addition.grid(row=3, column=3, padx=1, pady=1)

        #quinto renglon..
        # boton 0
        botton_zero = tk.Button(bottons_frame, text='0', width=24, height=3, bd=0, bg='#fff',
                                cursor='hand2', command=lambda: self._click_event(0))
        botton_zero.grid(row=4, column=0, columnspan=2, padx=1, pady=1)
        # boton punto
        botton_spot = tk.Button(bottons_frame, text='.', width=10, height=3, bd=0, bg='#fff',
                                cursor='hand2', command=lambda: self._click_event('.'))
        botton_spot.grid(row=4, column=2, padx=1, pady=1)
        ##boton igual =
        botton_equal = tk.Button(bottons_frame, text='=', width=10, height=3, bd=0, bg='#fff',
                                 cursor='hand2', command=self._result_event)
        botton_equal.grid(row=4, column=3, padx=1, pady=1)








    def _result_event(self):
        # eval evalua la expresion str como una expresion aritmetica
        try:
            if self.expression:
                result = str(eval(self.expression))
                self.text_input.set(result)
        except Exception as e:
            messagebox.showerror('ERROR', f'Error: {e}')
            self.text_input.set('')
        finally:
            self.expression = ''

    def _clear_event(self):
        self.expression = ''
        self.text_input.set(self.expression)

    def _click_event(self, element):
        #concatenamos el nuevo elemento ala expresion ya existente
        self.expression = f'{self.expression}{element}'
        self.text_input.set(self.expression)





if __name__ == '__main__':
    calculator = Calculator()
    calculator.mainloop()
