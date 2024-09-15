# aimentorapp/main.py
from aimentorapp.ai_interactions import AIInteraction

def main():
    ai = AIInteraction()
    print("Welcome to AIMentorApp!")
    
    while True:
        user_input = input("Enter a command (hello, bye, thanks, or exit): ").strip()
        if user_input.lower() == "exit":
            print("Exiting AIMentorApp. Goodbye!")
            break
        response = ai.provide_response(user_input)
        print(response)

if __name__ == "__main__":
    main()