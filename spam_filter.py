def is_spam(message):
    message = message.lower()

    spam_keywords = [
        "win money", "free cash", "click this", "subscribe now",
        "buy now", "limited offer", "earn fast"
    ]

    return any(keyword in message for keyword in spam_keywords)