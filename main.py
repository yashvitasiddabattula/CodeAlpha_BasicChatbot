def chatbot_response(user_input):
    """Generate a response based on the user's message."""

    message = user_input.lower().strip()

    if message in ["hello", "hi", "hey"]:
        return "Hi! Welcome. How can I help you?"

    elif message in ["how are you", "how are you?"]:
        return "I'm fine, thanks! How are you?"

    elif message in ["i am fine", "i am good", "good"]:
        return "That's great to hear!"

    elif message in ["what is your name", "your name"]:
        return "I'm a simple Python chatbot."

    elif message in ["thank you", "thanks"]:
        return "You're welcome!"

    elif message in ["bye", "goodbye", "exit"]:
        return "Goodbye! Have a great day!"

    else:
        return "Sorry, I don't understand that. Please try something else."


def start_chatbot():
    print("====================================")
    print("          PYTHON CHATBOT")
    print("====================================")
    print("Hello! I am your chatbot.")
    print("Type 'bye' to end the conversation.")

    while True:
        user_input = input("\nYou: ")

        response = chatbot_response(user_input)

        print("Chatbot:", response)

        if user_input.lower().strip() in ["bye", "goodbye", "exit"]:
            break


# Start the chatbot
start_chatbot()