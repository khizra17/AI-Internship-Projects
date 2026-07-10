Greetings = {
    "hello" : "Hi there!",
    "hi"    : "Hello!",
    "hey"   : "Hello there!",
    "thanks": "You're Welcome!",
    "thank you": "You're Welcome!",
    "how are you?": "I am doing great. Thank You!"   
}

def process(input):
    clean_input = input.lower().strip()
    return clean_input

print("Welcome back!")  
print()

while True:
    user_input = input("You: ")
    processed_input = process(user_input)
    if processed_input == 'exit' or processed_input == 'bye':
        print("Goodbye!")
        break
    reply = Greetings.get(processed_input,'I donot understand!')
    print(reply)
    print()
        
    
    
    
    

