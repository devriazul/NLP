import doctest

# --- Conditional Statements ---

# 1. Categorize temperature based on input value.
def check_temperature(temp: float) -> str:
    """Categorizes temperature as Cold, Warm, or Hot.

    >>> check_temperature(10)
    'Cold'
    >>> check_temperature(25)
    'Warm'
    >>> check_temperature(30)
    'Hot'
    """
    if temp < 15:
        return "Cold"
    elif 15 <= temp < 30:
        return "Warm"
    else:
        return "Hot"


# 2. Evaluate a model's performance based on its accuracy score.
def evaluate_model_accuracy(accuracy: int) -> str:
    """Evaluates a model based on its accuracy percentage.

    >>> evaluate_model_accuracy(95)
    'Excellent Model'
    >>> evaluate_model_accuracy(80)
    'Good Model'
    >>> evaluate_model_accuracy(60)
    'Average Model'
    >>> evaluate_model_accuracy(49)
    'Poor Model'
    """
    if accuracy >= 90:
        return "Excellent Model"
    elif 70 <= accuracy <= 89:
        return "Good Model"
    elif 50 <= accuracy <= 69:
        return "Average Model"
    else:
        return "Poor Model"


# 3. Determine if a given integer is even or odd.
def check_even_or_odd(dataset_size: int) -> str:
    """Determines if a number is Even or Odd.

    >>> check_even_or_odd(1000)
    'Even'
    >>> check_even_or_odd(751)
    'Odd'
    """
    if dataset_size % 2 == 0:
        return "Even"
    else:
        return "Odd"


# 4. Compare two model loss values to determine the better model.
def compare_model_loss(model_1_loss: float, model_2_loss: float) -> str:
    """Compares two models based on their loss values. Lower is better.

    >>> compare_model_loss(0.1, 0.2)
    'Model 1 is better.'
    >>> compare_model_loss(0.5, 0.3)
    'Model 2 is better.'
    >>> compare_model_loss(0.1, 0.1)
    'Both models have the same performance.'
    """
    if model_1_loss < model_2_loss:
        return "Model 1 is better."
    elif model_2_loss < model_1_loss:
        return "Model 2 is better."
    else:
        return "Both models have the same performance."


# 5. Check if a message is spam based on keywords.
def check_for_spam(message: str) -> str:
    """Checks if a message contains spam keywords.

    >>> check_for_spam("Congratulations! You won a free prize.")
    'Spam Message'
    >>> check_for_spam("This is a special offer just for you.")
    'Spam Message'
    >>> check_for_spam("Hello, how are you?")
    'Not Spam'
    """
    if "offer" in message.lower() or "free" in message.lower():
        return "Spam Message"
    else:
        return "Not Spam"

# --- Nested If-Else ---


# 6. Determine event eligibility based on age and number of published papers.
def check_eligibility_for_talk(age: int, papers: int) -> str:
    """Checks eligibility for a talk based on age and published papers.

    >>> check_eligibility_for_talk(25, 3)
    'Eligible for Talk'
    >>> check_eligibility_for_talk(20, 1)
    'Eligible for Attendee only'
    >>> check_eligibility_for_talk(17, 5)
    'Not Eligible'
    """
    if age >= 18:
        if papers >= 2:
            return "Eligible for Talk"
        else:
            return "Eligible for Attendee only"
    else:
        return "Not Eligible"


# 7. Check if a model is ready for deployment based on accuracy and latency.
def check_deployment_readiness(accuracy: float, latency: int) -> str:
    """Checks if a model is ready for production based on accuracy and latency.

    >>> check_deployment_readiness(90, 80)
    'Ready for Production'
    >>> check_deployment_readiness(88, 120)
    'Needs Optimization'
    >>> check_deployment_readiness(80, 90)
    'Not Suitable for Deployment'
    """
    if accuracy >= 85:
        if latency <= 100:
            return "Ready for Production"
        else:
            return "Needs Optimization"
    else:
        return "Not Suitable for Deployment"


# 8. Assess dataset quality based on the number of samples and missing value percentage.
def assess_dataset_quality(samples: int, missing_percentage: float) -> str:
    """Assesses dataset quality based on samples and missing values.

    >>> assess_dataset_quality(2000, 5)
    'Good Dataset'
    >>> assess_dataset_quality(1500, 15)
    'Needs Cleaning'
    >>> assess_dataset_quality(900, 5)
    'Insufficient Data'
    """
    if samples >= 1000:
        if missing_percentage <= 10:
            return "Good Dataset"
        else:
            return "Needs Cleaning"
    else:
        return "Insufficient Data"


# 9. Check data usability based on its source and user consent.
def check_data_usability(data_source: str, consent: str) -> str:
    """Checks data usability based on source and consent.

    >>> check_data_usability("public", "no")
    'Usable Data'
    >>> check_data_usability("private", "yes")
    'Usable Data'
    >>> check_data_usability("private", "no")
    'Ethical Issue'
    """
    if data_source.lower() == "public":
        return "Usable Data"
    else:
        if consent.lower() == "yes":
            return "Usable Data"
        else:
            return "Ethical Issue"


# 10. Suggest a machine learning model based on problem type and dataset size.
def select_model(problem_type: str, dataset_size: int) -> str:
    """Selects a model based on problem type and dataset size.

    >>> select_model("classification", 4000)
    'Logistic Regression'
    >>> select_model("classification", 6000)
    'Neural Network'
    >>> select_model("regression", 8000)
    'Linear Regression'
    >>> select_model("regression", 12000)
    'XGBoost'
    """
    if problem_type.lower() == "classification":
        if dataset_size <= 5000:
            return "Logistic Regression"
        else:
            return "Neural Network"
    elif problem_type.lower() == "regression":
        if dataset_size <= 10000:
            return "Linear Regression"
        else:
            return "XGBoost"

# --- While Loops ---


# 11. Simulate model training by reducing loss in a while loop.
def simulate_loss_reduction(initial_loss: float) -> list:
    """Simulates loss reduction until it's <= 0.1.

    >>> simulate_loss_reduction(0.25)
    [0.2, 0.15, 0.09999999999999998]
    """
    loss = initial_loss
    loss_history = []
    while loss > 0.1:
        loss -= 0.05
        loss_history.append(loss)
    return loss_history


# 12. Create a simple interactive chatbot that runs in a loop.
def chatbot():
    """A simple chatbot that responds until the user types 'exit'.
    This function is interactive and not tested with doctest.
    """
    user_input = ""
    while user_input.lower() != "exit":
        user_input = input("You: ")
        if user_input.lower() != "exit":
            print("Bot: I am learning...")
    print("Bot: Goodbye!")


# 13. Use a while loop to count from 1 up to a specified number.
def count_up_to(dataset_size: int) -> int:
    """Counts from 1 up to a given number using a while loop.

    >>> count_up_to(5)
    5
    >>> count_up_to(1)
    1
    """
    count = 0
    i = 0
    while i < dataset_size:
        i += 1
        count = i
    return count


# 14. Simulate and log training epochs using a while loop.
def train_epochs(total_epochs: int) -> list:
    """Simulates training epochs and returns the log.

    >>> train_epochs(3)
    ['Training epoch 1', 'Training epoch 2', 'Training epoch 3']
    """
    current_epoch = 1
    log = []
    while current_epoch <= total_epochs:
        message = f"Training epoch {current_epoch}"
        log.append(message)
        current_epoch += 1
    return log


# 15. Repeatedly divide a number by 2 in a loop until it is <= 1.
def divide_by_two_until_one(number: float) -> list:
    """Keeps dividing a number by 2 until it's <= 1.

    >>> divide_by_two_until_one(16)
    [8.0, 4.0, 2.0, 1.0]
    >>> divide_by_two_until_one(10)
    [5.0, 2.5, 1.25, 0.625]
    """
    steps = []
    while number > 1:
        number /= 2
        steps.append(number)
    return steps

# --- Combine Questions ---


# 16. Check password strength using nested conditional logic.
def check_password_strength(password: str) -> str:
    """Checks password strength based on length and content.

    >>> check_password_strength("MyStrongAIPass")
    'Strong Password'
    >>> check_password_strength("MyPassword123")
    'Weak Password'
    >>> check_password_strength("short")
    'Invalid Password'
    """
    if len(password) >= 8:
        if "AI" in password:
            return "Strong Password"
        else:
            return "Weak Password"
    else:
        return "Invalid Password"


# 17. Simulate learning rate decay using a while loop.
def adjust_learning_rate(learning_rate: float = 0.1) -> list:
    """Adjusts learning rate by dividing by 2 until it's <= 0.001.

    >>> adjust_learning_rate(0.01)
    [0.005, 0.0025, 0.00125, 0.000625]
    """
    history = []
    while learning_rate > 0.001:
        learning_rate /= 2
        history.append(learning_rate)
    return history


# 18. Use a while loop and conditional to count even numbers up to a limit.
def count_even_labels(dataset_labels: int) -> int:
    """Counts the number of even labels from 1 to dataset_labels.

    >>> count_even_labels(10)
    5
    >>> count_even_labels(7)
    3
    """
    count = 0
    i = 1
    while i <= dataset_labels:
        if i % 2 == 0:
            count += 1
        i += 1
    return count


# 19. Simulate accuracy improvement in a while loop.
def simulate_accuracy_increase(accuracy: int = 50) -> list:
    """Simulates accuracy increasing by 5 until it reaches 95.

    >>> simulate_accuracy_increase(80)
    ['Current Accuracy: 85%', 'Current Accuracy: 90%', 'Current Accuracy: 95%']
    """
    log = []
    while accuracy < 95:
        accuracy += 5
        log.append(f"Current Accuracy: {accuracy}%")
    return log


# 20. Evaluate a score using a chain of if/elif/else conditions.
def evaluate_marks(marks: int) -> str:
    """Evaluates a student's level based on marks.

    >>> evaluate_marks(90)
    'AI Expert'
    >>> evaluate_marks(75)
    'AI Learner'
    >>> evaluate_marks(50)
    'Needs Improvement'
    """
    if marks >= 80:
        return "AI Expert"
    elif marks >= 60:
        return "AI Learner"
    else:
        return "Needs Improvement"


# --- Doctest Runner ---
if __name__ == "__main__":
    print("--- Running Assignment 03 Doctests ---")
    results = doctest.testmod(verbose=False)
    if results.failed == 0:
        print(f"All {results.attempted} tests passed successfully!")
    else:
        print(f"Doctest results: {results.failed} failures / {results.attempted} tests.")
    print("--- End of Assignment 03 Solutions ---")