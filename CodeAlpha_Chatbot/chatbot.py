# Simple Rule-Based Chatbot — CodeAlpha Task 4

def get_response(user_input):
    user_input = user_input.lower().strip()

    # Greetings
    if user_input in ["hello", "hi", "hey", "hii", "helo"]:
        return "👋 Hi there! How can I help you today?"

    elif user_input in ["how are you", "how are you?", "how r u", "hows you"]:
        return "😊 I'm doing great, thanks for asking! What about you?"

    elif user_input in ["i am fine", "i'm fine", "good", "fine", "i am good"]:
        return "That's wonderful to hear! 😄 Is there anything I can help you with?"

    # About the bot
    elif user_input in ["what is your name", "what's your name", "who are you"]:
        return "🤖 I'm ChatBot, your simple AI assistant built for CodeAlpha!"

    elif user_input in ["what can you do", "help", "what do you do"]:
        return "💡 I can chat with you! Try saying: hello, how are you, tell me a joke, time, or bye."

    # Fun
    elif "joke" in user_input:
        return "😂 Why do programmers prefer dark mode? Because light attracts bugs! 🐛"

    elif "your favourite" in user_input or "your favorite" in user_input:
        return "🎯 My favourite thing is chatting with awesome people like you!"

    # Time
    elif "time" in user_input:
        from datetime import datetime
        now = datetime.now().strftime("%I:%M %p")
        return f"🕐 The current time is {now}."

    elif "date" in user_input:
        from datetime import datetime
        today = datetime.now().strftime("%d %B %Y")
        return f"📅 Today's date is {today}."

    # Farewells
    elif user_input in ["bye", "goodbye", "see you", "exit", "quit", "tata"]:
        return "QUIT"

    elif "thank" in user_input:
        return "😊 You're welcome! Happy to help anytime."

    # Default
    else:
        return "🤔 Hmm, I didn't understand that. Try: hello, how are you, tell me a joke, or bye."


def main():
    print("=" * 45)
    print("   🤖 Welcome to ChatBot — CodeAlpha Task 4")
    print("=" * 45)
    print("   Type 'bye' anytime to exit.\n")

    while True:
        user_input = input("You: ").strip()

        if not user_input:
            print("Bot: Please type something!\n")
            continue

        response = get_response(user_input)

        if response == "QUIT":
            print("Bot: 👋 Goodbye! Have a great day!")
            break

        print(f"Bot: {response}\n")


if __name__ == "__main__":
    main()
