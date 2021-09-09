import tkinter as tk 

LIGHT_GRAY = "#F5F5F5"
LABLE_COLOR = "#25265E"
SMALL_FONT_STYLE = ("Arial", 16)
LARGE_FONT_STYLE = ("Arial", 40, "bold")
WHITE = "#FFFFFF"
DIGITS_FONT_STYLE = ("Arial", 24, "bold")
DEFAULT_FONT_STYLE = ("Arial", 20)
OFF_WHITE = "#F8FAFF"
LIGHT_BLUE ="#CCEDFF"

class Calculator:

    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("375x667")
        self.window.resizable(0,0)
        self.window.title("Calculator")

        self.total_expresion = ""
        self.current_expresion = ""

        self.display_frame = self.create_display_frame()

        self.total_lable, self.lable = self.create_display_lables()

        self.digits = {
            7: (1,1), 8: (1,2), 9: (1,3), 
            4: (2,1), 5: (2,2), 6: (2,3),
            1: (3,1), 2: (3,2), 3: (3,3),
            0: (4,2), '.':(4,1)
        }

        self.operations = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"}

        self.buttons_frame = self.create_buttons_frame()
        self.buttons_frame.rowconfigure(0, weight=1)

        for x in range(1, 5):
            self.buttons_frame.rowconfigure(x, weight=1)
            self.buttons_frame.columnconfigure(x, weight=1)

        self.create_digit_buttons()
        self.create_operator_buttons()
        self.create_special_buttons()
        self.bind_keys()

    def bind_keys(self):
        self.window.bind("<Return>", lambda event: self.evaluate())
        for key in self.digits:
            self.window.bind(str(key), lambda event, digit=key: self.add_to_expression(digit))
        
        for key in self.operations:
            self.window.bind(key, lambda event, operator=key: self.append_operator(operator))

    def create_special_buttons(self):
        self.create_clear_button()
        self.create_equals_button()
        self.create_square_button()
        self.create_sqrt_button()

    def create_display_lables(self): 
        total_lable = tk.Label(self.display_frame, text=self.total_expresion, anchor=tk.E, bg=LIGHT_GRAY, 
        fg=LABLE_COLOR, padx=24, font=SMALL_FONT_STYLE)
        total_lable.pack(expand=True, fill="both")

        lable = tk.Label(self.display_frame, text=self.current_expresion, anchor=tk.E, bg=LIGHT_GRAY, 
        fg=LABLE_COLOR, padx=24, font=LARGE_FONT_STYLE)
        lable.pack(expand=True, fill="both")

        return total_lable, lable

    def create_display_frame(self):
        frame = tk.Frame(self.window, height = 221, bg=LIGHT_GRAY)
        frame.pack(expand=True, fill="both")

        return frame

    def add_to_expression(self, value):
        self.current_expresion +=str(value)
        self.update_lable()

    def append_operator(self, operator):
        self.current_expresion += operator
        self.total_expresion += self.current_expresion
        self.current_expresion = ""
        self.update_total_lable()
        self.update_lable()

    def create_operator_buttons(self):
        i = 0

        for operator, symbol in self.operations.items():
            button = tk.Button(self.buttons_frame, text=symbol, bg=OFF_WHITE, fg=LABLE_COLOR, font=DIGITS_FONT_STYLE, borderwidth=0, command=  lambda x= operator: self.append_operator(x))
            button.grid(row=i, column=4, sticky = tk.NSEW)
            i += 1



    def create_digit_buttons(self):
        for digit, grid_value in self.digits.items():
            button = tk.Button(self.buttons_frame, text=str(digit),bg=WHITE,fg=LABLE_COLOR,font=DIGITS_FONT_STYLE,borderwidth=0, command= lambda x=digit: self.add_to_expression(x))
            button.grid(row=grid_value[0],column=grid_value[1], sticky=tk.NSEW)

    def clear(self):
        self.current_expresion = ""
        self.total_expresion = ""
        self.update_lable()
        self.update_total_lable()

    def create_clear_button(self):
         button = tk.Button(self.buttons_frame, text='C', bg=OFF_WHITE, fg=LABLE_COLOR, font=DIGITS_FONT_STYLE, borderwidth=0, command= self.clear)
         button.grid(row=0, column=1, sticky = tk.NSEW)

    def square(self):
        self.current_expresion = str(eval(f"{self.current_expresion}**2"))
        self.update_lable()

    def create_square_button(self):
         button = tk.Button(self.buttons_frame, text="x\u00b2", bg=OFF_WHITE, fg=LABLE_COLOR, font=DIGITS_FONT_STYLE, borderwidth=0, command= self.square)
         button.grid(row=0, column=2, sticky = tk.NSEW)

    def sqrt(self):
        self.current_expresion = str(eval(f"{self.current_expresion}**0.5"))
        self.update_lable()

    def create_sqrt_button(self):
         button = tk.Button(self.buttons_frame, text="\u221ax", bg=OFF_WHITE, fg=LABLE_COLOR, font=DIGITS_FONT_STYLE, borderwidth=0, command= self.sqrt)
         button.grid(row=0, column=3, sticky = tk.NSEW)

    def evaluate(self):
        self.total_expresion += self.current_expresion
        self.update_total_lable()
        try:
             self.current_expresion = str(eval(self.total_expresion))

             self.total_expresion = ""
        
        except Exception as e:
            self.current_expresion = "Error"

        finally:
            self.update_lable()        

    def create_equals_button(self):
         button = tk.Button(self.buttons_frame, text='=', bg=LIGHT_BLUE, fg=LABLE_COLOR, font=DIGITS_FONT_STYLE, borderwidth=0, command=self.evaluate)
         button.grid(row=4, column=3, columnspan = 2, sticky = tk.NSEW)

    def create_buttons_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill="both")

        return frame

    def update_total_lable(self):
        expression = self.total_expresion
        for operator, symbol in self.operations.items():
            expression = expression.replace(operator, f" {symbol}")
        self.total_lable.config(text=expression)

    def update_lable(self):
        self.lable.config(text=self.current_expresion[:11])

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    calc = Calculator()
    calc.run()
