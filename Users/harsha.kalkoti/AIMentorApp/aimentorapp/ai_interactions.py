# aimentorapp/ai_interactions.py
class AIInteraction:
    def interact(self, user):
        print(f"Interacting with {user}.")

    def ask_question(self, question):
        print(f"AI asks: {question}")
        response = input("Your answer: ")
        return response

    def provide_response(self, user_input):
        responses = {
            "hello": "Hi there! How can I assist you today?",
            "bye": "Goodbye! Have a great day!",
            "thanks": "You're welcome!"
        }
        return responses.get(user_input.lower(), "I'm not sure how to respond to that.")