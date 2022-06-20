from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")

class QuizInterface():
    
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        #the window will be created in the init
        #we will have separate methods for the other objects
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.create_score_label()
        self.create_canvas()
        self.create_buttons()
        self.get_next_question()

        self.window.mainloop()

    def create_score_label(self):
        self.score_label = Label(text= "Score: 0", fg = "white", bg=THEME_COLOR, font= ("Arial", 20))
        self.score_label.grid(row=0, column=1)
    
    def create_canvas(self):
        self.canvas = Canvas(width=320, height=270, highlightthickness=0, bg="white")
        self.question = self.canvas.create_text(150, 125, text="Some question text", font = FONT, width= 270)
        self.canvas.grid(column=0, row=1,columnspan = 2, pady=50)
    
    def create_buttons(self):
        #true button
        self.false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=self.false_image, highlightthickness=0, command=self.answer_false)
        self.false_button.grid(row=2, column=1)

        #false button
        self.true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=self.true_image, highlightthickness=0, command=self.answer_true)
        self.true_button.grid(row=2, column=0)

    #a method that fetches the next question, if there are questions remaining
    def get_next_question(self):
        self.enable_buttons()
        self.canvas.config(bg="white")
        self.score_label.config(text=f"Score: {self.quiz.score}")
        if self.quiz.still_has_questions():
            #self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text = q_text)
        else:
            self.canvas.itemconfig(self.question, text="You have reached the end of the quiz!")
            self.disable_buttons()

    #method that checks if the answer is false
    def answer_false(self):
        user_answer = "False"
        is_wrong = self.quiz.check_answer(user_answer)
        self.give_feedback(is_wrong)
    
    #method that checks if the answer is true
    def answer_true(self):
        user_answer = "True"
        is_right = self.quiz.check_answer(user_answer)
        self.give_feedback(is_right)
    
    #a method that gives the user feedback if they got the answer right or wrong
    #this is done by flashing a red color on the canvas (wrong answer)
                              #a green color on the canvas (right answer) 
    def give_feedback(self, right_or_wrong):
        self.disable_buttons()
        if right_or_wrong == True:
            self.canvas.config(bg="green")
        elif right_or_wrong == False:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)
    
    #a method that enables the buttons
    def enable_buttons(self):
        self.true_button.config(state="active")
        self.false_button.config(state="active")
    
    #a method that disables the buttons
    def disable_buttons(self):
        self.true_button.config(state="disabled")
        self.false_button.config(state="disabled")
