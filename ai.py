quiz_data = [
    {
        "question": "What type of AI does not leverage past experience?",
        "options": {
            "a": "Self-Awareness",
            "b": "Theory of Mind",
            "c": "Reactive Machine",
            "d": "Limited Memory",
        },
        "correct_answer": "c",
    },
    {
        "question": "The opacity of an AI system refers to the fact that",
        "options": {
            "a": "the decisions made by the AI system are opaque to the input data.",
            "b": "the AI system naturally exhibits opacity to the training data.",
            "c": "the AI system limits opportunities for human participation.",
            "d": "users of the AI system will not know why a particular decision has been taken by the AI system.",
        },
        "correct_answer": "d",
    },
    {
        "question": "Which of the following is true about AI, Machine Learning, and Deep Learning?",
        "options": {
            "a": "Machine Learning and Deep Learning both are two competing technologies for AI",
            "b": "Deep Learning can learn deep patterns from the data more effectively than Machine Learning and AI",
            "c": "Deep Learning is a subset of Machine Learning and Machine Learning is a subset of AI",
            "d": "A data scientist chooses an algorithm from AI, Machine Learning, or Deep Learning that suits the "
                 "domain and type of the problem to solve.",
        },
        "correct_answer": "c",
    },
    {
        "question": "The time in the future when machines will become more intelligent than human beings and start "
                    "developing further AI is referred to as",
        "options": {
            "a": "singularity",
            "b": "AI Age",
            "c": "Machine Age",
            "d": "Machine Revolution",
        },
        "correct_answer": "a",
    },
    {
        "question": "For large Artificial Neural Networks, the initial values of weights",
        "options": {
            "a": "should be set very small to have a small prediction error",
            "b": "do not matter a lot",
            "c": "should be set high to have a high prediction accuracy",
            "d": "should be set very carefully as they affect the prediction accuracy",
        },
        "correct_answer": "d",
    },
    {
        "question": "Which of the following mechanisms is most likely to be used to access Facebook and Twitter data "
                    "that these companies have made available for public consumption?",
        "options": {
            "a": "Web events",
            "b": "Survey",
            "c": "Financial transactions",
            "d": "API",
        },
        "correct_answer": "d",
    },
    {
        "question": "Your team has just finished work on a data science project which involved the following steps...\n"

                    "A) Create a graph showing revenue of customers' subscription over time \n"
                    "B) Collecting data from the finance team \n"
                    "C) Create users' clusters and perform regression to predict which customers are most likely to "
                    "stay with the company the next year. \n"
                    "D) Correct data format on data collected for UK and USA customers \n"

                    "Which of the following is the right order of above-mentioned steps?",
        "options": {
            "a": "a-b-c-d",
            "b": "b-c-a-d",
            "c": "d-a-c-b",
            "d": "b-d-a-c",
        },
        "correct_answer": "d",
    },
    {
        "question": "A/B testing is often used to choose between two options. Following are the necessary steps "
                    "involved in A/B testing...\n"

                    "A) Check statistical significance \n"
                    "B) Choose Sample Size \n"
                    "C) Pick the metric to measure \n"
                    "D) Run the experiment \n",
        "options": {
            "a": "C-B-D-A",
            "b": "B-C-A-D",
            "c": "D-A-C-B",
            "d": "B-A-D-C",
        },
        "correct_answer": "a",
    },
    {
        "question": "While preparing training data for supervised learning data shuffling is performed to...",
        "options": {
            "a": "avoid seeing patterns that are just because observations were added to the data in a specific order",
            "b": "ensure we have sufficient data for training",
            "c": "avoid data overfitting which affects the accuracy of prediction",
            "d": "ensure that the model is not underfit",
        },
        "correct_answer": "a",
    },
    {
        "question": "In Principal Component Analysis, the first component...",
        "options": {
            "a": "is least important and can be ignored without impacting the prediction accuracy.",
            "b": "shows the direction of maximum variance",
            "c": "shows the direction which is orthogonal to the first feature.",
            "d": "shows the average value of all features",
        },
        "correct_answer": "b",
    },
    {
        "question": "If a supervised learning model has a very low error on training data set and very high error on "
                    "test data set this shows:",
        "options": {
            "a": "Overfitting",
            "b": "Underfitting",
            "c": "Too many unrelated features are used by the model",
            "d": "Sparse training data",
        },
        "correct_answer": "a",
    },
    {
        "question": "Which of the following statements applies to PCA (Principal Component Analysis)?",
        "options": {
            "a": "PCA works well for data with very few features.",
            "b": "PCA can only be used for classification problems.",
            "c": "PCA is used to reduce the dimensionality of data while preserving as much variance as possible.",
            "d": "PCA increases the dimensionality of data.",
        },
        "correct_answer": "c",

    },

    # Add more questions here...
    {
        "question": "Which of the following statements applies to k-means clustering?",
        "options": {
            "a": "k-means clustering is a supervised learning algorithm.",
            "b": "k-means clustering is a classification algorithm.",
            "c": "k-means clustering is a clustering algorithm.",
            "d": "k-means clustering is a regression algorithm.",
        },
        "correct_answer": "c",
    },

    {
        "question": "bayesian optimization is used to",
        "options": {
            "a": "find the best hyperparameters of a model",
            "b": "find the best model",
            "c": "find the best features of a model",
            "d": "find the best data for a model",
        },
        "correct_answer": "a",
    },
]
quiz_data += [
    {
        "question": "One-hot encoding is used to convert categorical data into numerical data which leads to",
        "options": {
            "a": "reduced dimensionality",
            "b": "increased dimensionality",
            "c": "increased training data",
            "d": "decreased training data",
        },
        "correct_answer": "b",
    },
    {
        "question": "The main goal of a linear regression algorithm is to find the slope and intercept of the line that",
        "options": {
            "a": "maximises the minimum loss",
            "b": "minimises the average loss",
            "c": "maximises the average loss",
            "d": "minimises the maximum loss",
        },
        "correct_answer": "b",
    },
    {
        "question": "k-NN classifier predicts the class of a test point based on the class of ______ nearest data "
                    "points and using _______.",
        "options": {
            "a": "1, voting",
            "b": "N, average",
            "c": "k, average",
            "d": "k, voting",
        },
        "correct_answer": "d",
    },
    {
        "question": "In linear regression, the slope of the best fit line can be",
        "options": {
            "a": "zero",
            "b": "negative",
            "c": "positive",
            "d": "all of the above",
        },
        "correct_answer": "d",
    },
    {
        "question": "A Multiple linear regression model is applicable to",
        "options": {
            "a": "only single-dimensional space",
            "b": "any-dimensional space",
            "c": "only three-dimensional space",
            "d": "only two-dimensional space",
        },
        "correct_answer": "b",
    },
    {
        "question": "Multivariant linear regression involves",
        "options": {
            "a": "a single independent variable affecting a single output variable.",
            "b": "more than one independent variable influencing more than one output variable.",
            "c": "a single output variable influencing a single input variable.",
            "d": "more than one independent variable influencing a single output variable.",
        },
        "correct_answer": "d",
    },
    {
        "question": "In k-NN classifier, the decision boundary becomes smoother by",
        "options": {
            "a": "decreasing the value of k",
            "b": "increasing the value of k",
            "c": "increasing the number of classes",
            "d": "decreasing the number of classes",
        },
        "correct_answer": "b",
    },
    {
        "question": "In k-NN classifier if k is set equal to the number of training data-points then",
        "options": {
            "a": "the model will be overfit",
            "b": "the accuracy on training data will be maximum",
            "c": "prediction will be same for all test points",
            "d": "the model will be goodfit",
        },
        "correct_answer": "b",
    },
    {
        "question": "Logistic Regression",
        "options": {
            "a": "is a regression algorithm",
            "b": "is a classifier",
            "c": "deals with logistic problems",
            "d": "is an efficient algorithm of linear regression",
        },
        "correct_answer": "b",
    },
    {
        "question": "One-Vs-Rest approach is used to",
        "options": {
            "a": "select one (the most important) feature and reject all others",
            "b": "select simple binary classifiers to classify multiple classes",
            "c": "select one optimal algorithm for classification",
            "d": "compare algorithm one with the rest of the algorithms",
        },
        "correct_answer": "b",
    },
    {
        "question": "Suppose you are designing a cancer test kit using a Machine learning algorithm. The algorithm "
                    "will use microscopic pictures of cells to identify if they are malignant (positive) or benign ("
                    "negative). Ideally, you would like to have",
        "options": {
            "a": "high sensitivity and low specificity",
            "b": "low sensitivity and low specificity",
            "c": "high sensitivity and high specificity",
            "d": "low sensitivity and high specificity",
        },
        "correct_answer": "c",
    },
    {
        "question": "In SVM, which of the following statements apply to support vectors?",
        "options": {
            "a": "Support vectors are data points that are at an equal distance from the hyperplane",
            "b": "Support vectors are data points that are closest to the hyperplane",
            "c": "Support vectors show the direction of increasing prediction to error",
            "d": "Support vectors are data points that are outliers and likely to appear because of random noise",
        },
        "correct_answer": "b",
    },
    {
        "question": "In Decision Trees, if all leaf nodes are pure nodes, the model is",
        "options": {
            "a": "Goodfit",
            "b": "Underfit",
            "c": "Overfit",
            "d": "100% accurate on test data",
        },
        "correct_answer": "a",
    },
    {
        "question": "Decision Trees can be used for regression problems as well. However, one important difference "
                    "between linear regression models and Decision Trees based regression models is",
        "options": {
            "a": "Linear regression models are much more efficient than Decision Trees based regression",
            "b": "Linear regression models can extrapolate while Decision Trees cannot",
            "c": "Linear regression models can work with any type of data while Decision Trees cannot",
            "d": "Linear regression models tend to overfit while Decision Trees based do not.",
        },
        "correct_answer": "d",
    },
    {
        "question": "Which of the following is true about SVM?",
        "options": {
            "a": "It is a model trained using unsupervised learning. It can be used for classification and regression.",
            "b": "It is a model trained using unsupervised learning. It can be used for classification but not for "
                 "regression.",
            "c": "It is a model trained using supervised learning. It can be used for classification and regression.",
            "d": "It is a model trained using unsupervised learning. It can be used for classification but not for "
                 "regression.",
        },
        "correct_answer": "c",
    },
]


 #Creating GUI app for the quiz using Tkinter
from tkinter import *
from tkinter import messagebox
import random

class QuizApp:
    def __init__(self, master):
        self.master = master
        self.master.title("AI Quiz")
        self.master.geometry("600x400")
        self.score = 0
        self.questions = []
        self.current_question = 0
        self.total_questions = 0
        self.start_screen()

    def start_screen(self):
        self.start_label = Label(self.master, text="Enter number of questions:", font=("Helvetica", 16))
        self.start_label.pack(pady=20)

        self.num_questions_entry = Entry(self.master, font=("Helvetica", 14))
        self.num_questions_entry.pack(pady=10)

        self.start_button = Button(self.master, text="Start Quiz", command=self.start_quiz)
        self.start_button.pack(pady=20)

    def start_quiz(self):
        num_questions = self.num_questions_entry.get()
        if num_questions.isdigit():
            num_questions = int(num_questions)
            if 1 <= num_questions <= len(quiz_data):
                self.total_questions = num_questions
                self.questions = random.sample(quiz_data, num_questions)
                self.clear_start_screen()
                self.create_widgets()
            else:
                messagebox.showerror("Error", "Please enter a valid number of questions.")
        else:
            messagebox.showerror("Error", "Please enter a valid number.")

    def clear_start_screen(self):
        self.start_label.destroy()
        self.num_questions_entry.destroy()
        self.start_button.destroy()


    def create_widgets(self):
        self.question_label = Label(self.master, text="", font=("Helvetica", 16), wraplength=500)
        self.question_label.pack(pady=20)

        self.var = StringVar()

        self.radio_a = Radiobutton(self.master, text="", variable=self.var, value="a")
        self.radio_b = Radiobutton(self.master, text="", variable=self.var, value="b")
        self.radio_c = Radiobutton(self.master, text="", variable=self.var, value="c")
        self.radio_d = Radiobutton(self.master, text="", variable=self.var, value="d")

        self.radio_a.pack(anchor="w")
        self.radio_b.pack(anchor="w")
        self.radio_c.pack(anchor="w")
        self.radio_d.pack(anchor="w")

        self.submit_button = Button(self.master, text="Submit", command=self.check_answer)
        self.submit_button.pack(pady=20)

        self.update_question()

    def update_question(self):
        if self.current_question < len(quiz_data):
            question = quiz_data[self.current_question]
            self.question_label.config(text=question["question"])
            self.radio_a.config(text=f"a. {question['options']['a']}")
            self.radio_b.config(text=f"b. {question['options']['b']}")
            self.radio_c.config(text=f"c. {question['options']['c']}")
            self.radio_d.config(text=f"d. {question['options']['d']}")
        else:
            self.finish_quiz()

    def check_answer(self):
        if self.var.get() == quiz_data[self.current_question]["correct_answer"]:
            self.score += 1
        self.current_question += 1
        self.update_question()

    def finish_quiz(self):
        messagebox.showinfo("Quiz Finished", f"Your score: {self.score}/{len(quiz_data)}")
        self.master.quit()

def main():
    root = Tk()
    app = QuizApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()