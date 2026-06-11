print("Hi i am LEO,your AI chatbot ")
print("what can i do for u ")
print("Type 'bye' to exit")

while True:
    user_input = input("You: ").lower()

    if user_input == "hello" or user_input == "hi":
        print("Bot: Hello! How can I help you?")

    elif "name" in user_input:
        print("Bot: My name is LEO.")

    elif "how are you" in user_input:
        print("Bot: I am fine. Thank you for asking!")

    elif "college" in user_input:
        print("Bot: College is a great place to learn and grow and develop skills for your future.")

    elif "time" in user_input:
        print("Bot: Sorry, I cannot tell the current time,some error has occured.")

    elif user_input == "bye":
        print("Bot: Goodbye! Have a nice day.")
        break

    else:
        print("Bot: Sorry, I don't understand that.")