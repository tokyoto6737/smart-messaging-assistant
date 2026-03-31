import tkinter as tk
from ai_module import detect_sentiment, generate_reply
from spam_filter import is_spam
from ai_module import suggest_replies

class ChatUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Vaibhs Chatbot")
        self.root.geometry("400x500")

        # Chat display area
        self.chat_area = tk.Text(root, state='disabled', wrap='word')
        self.chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        self.chat_area.tag_config("user", foreground="blue")
        self.chat_area.tag_config("bot", foreground="green")
        self.chat_area.tag_config("system", foreground="red")

        # Input field
        self.entry = tk.Entry(root)
        self.entry.pack(padx=10, pady=5, fill=tk.X)
        self.entry.bind("<Return>", self.send_message)

        # Send button
        self.send_button = tk.Button(root, text="Send", command=self.send_message)
        self.send_button.pack(pady=5)
        self.suggestion_frame = tk.Frame(root)
        self.suggestion_frame.pack(pady=5)

    def display_message(self, sender, message):
        self.chat_area.config(state='normal')

        if sender == "You":
            self.chat_area.insert(tk.END, f"You: {message}\n", "user")
        elif sender == "Assistant":
            self.chat_area.insert(tk.END, f"Assistant: {message}\n", "bot")
        else:
            self.chat_area.insert(tk.END, f"{sender}: {message}\n", "system")

        self.chat_area.config(state='disabled')
        self.chat_area.see(tk.END)
    def send_message(self, event=None):
        message = self.entry.get()
        if message.strip() != "":
            self.display_message("You", message)

            if is_spam(message):
                self.display_message("System", "🚫 Spam detected!")
            else:
                sentiment = detect_sentiment(message)
                reply = generate_reply(message)
                suggestions = suggest_replies(message)

                self.display_message("System", f"Sentiment: {sentiment}")
                self.display_message("Assistant", reply)

                self.show_suggestions(suggestions)

            self.entry.delete(0, tk.END)
    def show_suggestions(self, suggestions):
        # Clear old buttons
        for widget in self.suggestion_frame.winfo_children():
            widget.destroy()

        for text in suggestions:
            btn = tk.Button(self.suggestion_frame, text=text,
                            command=lambda t=text: self.use_suggestion(t))
            btn.pack(side=tk.LEFT, padx=5)
    def use_suggestion(self, text):
        self.entry.delete(0, tk.END)
        self.entry.insert(0, text)