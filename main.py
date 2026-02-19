import datetime

name = input("Enter your name: ")
present_hour = datetime.datetime.now().hour

if 5 <= present_hour < 12:
    print("Good Morning", name)
elif 12 <= present_hour < 17:
    print("Good Afternoon", name)
elif 17 <= present_hour < 21:
    print("Good Evening", name)
else:
    print("Good Night", name)

print("\nWelcome to your ChatBot")
print("You can ask me basic questions. Type 'bye' to exit.\n")

responses = {
    "hello": "Hi dear, how can I help you?",
    "how are you": "I'm fine. What about you?",
    "what are you doing": "Currently I'm learning new things. And you?",
    "who are you": "I'm your personal chatbot",
    "happy": "That's great!"
}

def get_bot_response(user_question):
    user_question = user_question.lower()
    for key in responses:
        if key in user_question:
            return responses[key]
    return "I am still learning. I can't answer that yet."

while True:
    user_input = input("You: ").strip()

    if "bye" in user_input.lower():
        print("Bot: Goodbye! Have a nice day ")
        break

    reply = get_bot_response(user_input)
    print("Bot:", reply)
