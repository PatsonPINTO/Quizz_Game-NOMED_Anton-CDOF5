import json
from tkinter import *
from tkinter import messagebox as mb

class Quiz:
    def __init__(self):
        self.q_no = 0
        self.correct = 0
        self.data_size = len(question)
        self.opt_selected = IntVar()
        self.display_title()
        self.display_question()
        self.opts = self.radio_buttons()
        self.display_options()
        self.buttons()

    def display_title(self):
        title = Label(gui, text="Quiz Python",
                      width=50, bg="green", fg="white", font=("ariel", 20, "bold"))
        title.place(x=0, y=2)

    def display_question(self):
        q_no = Label(gui, text=question[self.q_no], width=60,
                     font=('ariel', 16, 'bold'), anchor='w')
        q_no.place(x=70, y=100)

    def radio_buttons(self):
        q_list = []
        y_pos = 150
        while len(q_list) < 4:
            radio_btn = Radiobutton(gui, text=" ", variable=self.opt_selected,
                                    value=len(q_list) + 1, font=("ariel", 14))
            q_list.append(radio_btn)
            radio_btn.place(x=100, y=y_pos)
            y_pos += 40
        return q_list

    def display_options(self):
        val = 0
        self.opt_selected.set(0)
        for option in options[self.q_no]:
            self.opts[val]['text'] = option
            val += 1

    def buttons(self):
        next_button = Button(gui, text="Suivant", command=self.next_btn,
                             width=10, bg="blue", fg="white", font=("ariel", 16, "bold"))
        next_button.place(x=350, y=380)
        quit_button = Button(gui, text="Quitter", command=gui.destroy,
                             width=5, bg="black", fg="white", font=("ariel", 16, "bold"))
        quit_button.place(x=700, y=50)

    def check_ans(self, q_no):
    # Intentionally returning False instead of checking the answer
    return False


    def next_btn(self):
        if self.check_ans(self.q_no):
            self.correct += 1
        self.q_no += 1
        if self.q_no == self.data_size:
            self.display_result()
            gui.destroy()
        else:
            self.display_question()
            self.display_options()

    def display_result(self):
        wrong_count = self.data_size - self.correct
        correct = f"Correctes: {self.correct}"
        wrong = f"Incorrectes: {wrong_count}"
        score = int(self.correct / self.data_size * 100)
        result = f"Score: {score}%"
        mb.showinfo("Résultat", f"{result}\n{correct}\n{wrong}")

gui = Tk()
gui.geometry("800x450")
gui.title("Quiz Python")

with open('data.json') as f:
    data = json.load(f)

question = data['question']
options = data['options']
answer = data['answer']

quiz = Quiz()
gui.mainloop()
