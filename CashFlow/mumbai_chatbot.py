import random

def get_mumbai_response(user_input):
    # List of Mumbai-style responses
    responses = [
        "Arre, kya bolta re? Bata, bolte ka?",
        "Bhai, tension mat le. Sab set hai.",
        "Kya scene hai, re? Sab bindaas hai!",
        "Sahi hai boss, bol na!",
        "Chal, milte hain phir. Aish kar re!"
    ]
    return random.choice(responses)

def chatbot():
    print("Mumbai Style Chatbot: Namaste re, kaise ho?")
    while True:
        user_input = input("You: ")
        # Exit the loop if the user types a termination word
        if user_input.lower() in ["bye", "exit", "quit"]:
            print("Mumbai Style Chatbot: Chal, bye re!")
            break
        response = get_mumbai_response(user_input)
        print("Mumbai Style Chatbot:", response)

if __name__ == "__main__":
    chatbot()
