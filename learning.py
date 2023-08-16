import nltk
from nltk.chat.util import Chat, reflections

# Define chatbot responses using pattern-response pairs
responses = [
    (r"hi|hello|hey", ["Hello!", "Hi there!", "Hey!"]),
    (r"how are you|how's it going", ["I'm just a chatbot, but I'm here to help!"]),
    (r"what is your name", ["You can call me ChatBot."]),
    (r"bye|goodbye", ["Goodbye!", "Take care!"]),
    # You can add more patterns and responses here
]


def main():
    print("Hello! I'm your chatbot. Type 'exit' to end the conversation.")
    chatbot = Chat(responses, reflections)

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("ChatBot: Goodbye!")
            break
        response = chatbot.respond(user_input)
        print("ChatBot:", response)


if __name__ == "__main__":
    main()