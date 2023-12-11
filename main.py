# This is a sample Python script.

# quiz
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
        "correct_answer": "b",
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
        "question": "Multivariate linear regression involves",
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
        "correct_answer": "c",
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
    {
        "question": "Discriminating between poor and best customer experience is an example of:",
        "options": {
            "a": "Regression",
            "b": "Clustering",
            "c": "Dimensionality Reduction",
            "d": "Classification"
        },
        "correct_answer": "d"
    },
    {
        "question": "Choose the right answer after calculating RMSE for the following values: Actual values=[2,-4,-3,"
                    "8], Predicted values=[1,-5,-2,6]",
        "options": {
            "a": "1.012",
            "b": "1.431",
            "c": "1.232",
            "d": "1.320",
            "e": "1.323"
        },
        "correct_answer": "e"
    },
    {
        "question": "Support vectors are the data points that lie closest to the decision surface (hyperplane).",
        "options": {
            "a": "True",
            "b": "False"
        },
        "correct_answer": "a"
    },
    {
        "question": "Recognizing the language of a website is an example of:",
        "options": {
            "a": "Regression",
            "b": "Clustering",
            "c": "Classification",
            "d": "Association"
        },
        "correct_answer": "c"
    },
    {
        "question": "If your classification problem changes from four classes to two classes, how many times do you need to train an SVM classifier using the one-vs-all method?",
        "options": {
            "a": "Four",
            "b": "Once",
            "c": "Twice",
            "d": "Three times"
        },
        "correct_answer": "b"
    },
    {
        "question": "Bayes’ theorem describes the probability of an event based on prior knowledge of conditions that are related to the event. If the sensitivity and specificity of the classifier are 70% and 80% respectively, assuming 2% of the population has cancer, what is the probability that a random person who tests positive is a cancer patient?",
        "options": {
            "a": "6.67%",
            "b": "5.24%",
            "c": "3.20%",
            "d": "6.07%"
        },
        "correct_answer": "a"  # Assuming this is the correct answer after calculation
    },
    {
        "question": "Which of the following classification algorithms can generate rules?",
        "options": {
            "a": "Support vector machines",
            "b": "Logistic regression",
            "c": "Artificial neural networks",
            "d": "Decision trees"
        },
        "correct_answer": "d"
    },
    {
        "question": "The conditional probability P(X|Y) shows:",
        "options": {
            "a": "the chances of occurring event X and not event Y.",
            "b": "the chances of occurring event Y given that event X has happened.",
            "c": "the chances of occurring both events X and Y simultaneously.",
            "d": "the chances of occurring event X given that event Y has happened."
        },
        "correct_answer": "d"
    },
    {
        "question": "Multiple linear regression involves:",
        "options": {
            "a": "a single output variable influencing a single input variable.",
            "b": "more than one independent variable influencing a single output variable.",
            "c": "more than one independent variable influencing more than one output variables.",
            "d": "a single independent variable affecting a single output variable."
        },
        "correct_answer": "b"
    },
    {
        "question": "Generalization error is usually:",
        "options": {
            "a": "lower than the testing error",
            "b": "higher than the testing error",
            "c": "higher than the training error",
            "d": "lower than the training error"
        },
        "correct_answer": "c"
    },
    {
        "question": "While clustering, Object-1 and Object-2 are similar data points if:",
        "options": {
            "a": "Similarity < 0",
            "b": "Similarity = 0",
            "c": "Similarity = 1",
            "d": "Similarity > 0"
        },
        "correct_answer": "c"
    },
    {
        "question": "If a decision tree model is too complex, which of the following can be used to decrease its "
                    "complexity?",
        "options": {
            "a": "Add constraint on the tree depth",
            "b": "Maximize the number of pure nodes",
            "c": "Make decision tree as broad as possible",
            "d": "Have more than one root nodes"
        },
        "correct_answer": "a"
    }
]

# import the necessary libraries
import random


# Function to conduct the quiz and return the score and the correct answers and limit to allow user to choose the
# amount of questions to answer

def quiz(limit):
    score = 0
    correct_answers = []

    # shuffle the quiz data
    random.shuffle(quiz_data)

    for i in range(limit):
        print(f"Question {i + 1}: {quiz_data[i]['question']}")
        for option in quiz_data[i]['options']:
            print(f"{option}: {quiz_data[i]['options'][option]}")
        answer = input("Enter your answer: ")
        if answer == quiz_data[i]['correct_answer']:
            score += 1
            correct_answers.append(i + 1)
    return score, correct_answers


# Function to display the score and the correct answers
def display(score, correct_answers):
    print(f"Your score is {score}/{limit}")
    if score == limit:
        print("Well done! You got all the answers correct")
    elif score == 0:
        print("You got all the answers wrong")
        print("The correct answers are:")
        for i in range(limit):
            print(f"Question {i + 1}: {quiz_data[i]['question']}")
            print(f"Correct answer: {quiz_data[i]['correct_answer']}")
            print()
    else:
        print("You got the following answers wrong:")
        for i in range(limit):
            if i + 1 not in correct_answers:
                print(f"Question {i + 1}: {quiz_data[i]['question']}")
                print(
                    f"Correct answer: {quiz_data[i]['correct_answer']}: {quiz_data[i]['options'][quiz_data[i]['correct_answer']]}")

                print()


# Function to allow user to choose the amount of questions to answer
def choose():
    limit = int(input("How many questions would you like to answer? "))
    if limit > len(quiz_data):
        print(f"Sorry, there are only {len(quiz_data)} questions available")
        limit = int(input("How many questions would you like to answer? "))
    return limit


# Function to allow user to choose to take the quiz again
def again():
    response = input("Would you like to take the quiz again? (y/n) ")
    if response == "y":
        return True
    elif response == "n":
        print("Thank you for taking the quiz")
    else:
        print("Please enter y or n")
        again()


# code to run the quiz
limit = choose()
score, correct_answers = quiz(limit)
display(score, correct_answers)
while again():
    limit = choose()
    score, correct_answers = quiz(limit)
    display(score, correct_answers)
41