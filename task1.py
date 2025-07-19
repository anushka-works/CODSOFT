def chatbot():
    print("Hi! I'm a chatbot. To end the chat, type 'bye'.")
    while True:
        user_input = input("You: ").lower()

        if user_input in ["hello", "hi"]:
            print("Bot: Hi! How may I assist you?")

        elif "what's your name" in user_input:
            print("Bot: I am a basic rule-based chatbot built with Python.")

        elif "how are you" in user_input:
            print("Bot: I'm doing fantastic! 😊Thanks for asking.")

        elif "what can you do" in user_input:
            print("Bot: I can talk to you and respond to some of your simple questions.")

        elif "bye" in user_input:
            print("Bot: ok bye! Enjoy your day!")
            break  # Exit the loop when user says bye

        elif "help" in user_input:
            print("Bot: You can just say hello or ask me my name and how I'm doing!")

        else:
            print("Bot: I don't know how to react to that. Try to ask a different query.")

# Launch the chatbot
chatbot()
