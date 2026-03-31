def detect_sentiment(message):
    message = message.lower()

    if any(word in message for word in ["urgent", "asap", "immediately"]):
        return "Urgent ⚠️"
    elif any(word in message for word in ["happy", "great", "good", "nice"]):
        return "Positive 😊"
    elif any(word in message for word in ["sad", "angry", "bad", "upset"]):
        return "Negative 😠"
    else:
        return "Neutral 😐"


def generate_reply(message):
    message = message.lower()

    if "where are you" in message:
        return "I’m on my way!"
    elif "hello" in message or "hi" in message:
        return "Hey! How can I help you?"
    elif "urgent" in message:
        return "I’ll get back to you ASAP."
    elif "thank" in message:
        return "You're welcome!"
    else:
        return "Got it!"
def suggest_replies(message):
    message = message.lower()

    if "hello" in message:
        return ["Hi!", "Hello there!", "Hey!"]
    elif "how are you" in message:
        return ["I'm good!", "Doing great!", "All good here!"]
    elif "where" in message:
        return ["On my way!", "Almost there!", "Give me 5 mins"]
    else:
        return ["Okay", "Got it", "Sure"]