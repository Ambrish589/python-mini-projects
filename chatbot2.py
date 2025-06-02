import random

hello = ["Hello","Hii", "Hi", "Hey",  "Namaste"]
bye = ["Goodbye",  "See you later", "Take care", "Bye",]

def chatbot():
    print("hello my name is alex what are you doing")
    print("Welcome to the chatbot! Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye! Have a great day!")
            break
        elif user_input.lower() in ['hello', 'hi','hii', 'hey']:
            response = random.choice(hello)
            print(f"Chatbot: {response} how can i help  you today ")
        elif user_input.lower() in ['bye', 'goodbye', 'see you']:
            response = random.choice(bye)
            print(f"Chatbot: {response} jao maachudao")
        else:
            print("Chatbot: I'm not sure how to respond to that. Can you try something else?")

chatbot()

