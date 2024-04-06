from textblob import TextBlob
from textblob.np_extractors import ConllExtractor
import re

extractor = ConllExtractor()

def main():   
    print("Hello, I am Marvin, the friendly robot.")
    print("You can end this conversation at any time by typing 'bye'")    
    print("After typing each answer, press 'enter'")
    print("How are you today?")

    while True:
        user_input = input("> ")

        if user_input.lower() == "bye":            
            break
        else:
            # Check for specific keywords in the user input
            if re.search(r'\bwhy\b', user_input.lower()):
                print("I'm not sure, why do you ask?")
            elif re.search(r'\bhow\b', user_input.lower()):
                print("I'm not sure, how do you think?")
            else:
                user_input_blob = TextBlob(user_input, np_extractor=extractor)                        
                np = user_input_blob.noun_phrases                                    
                response = ""
                if user_input_blob.polarity <= -0.5:
                    response = "Oh dear, that sounds bad. "
                elif user_input_blob.polarity <= 0:
                    response = "Hmm, that's not great. "
                elif user_input_blob.polarity <= 0.5:
                    response = "Well, that sounds positive. "
                elif user_input_blob.polarity <= 1:
                    response = "Wow, that sounds great. "

                if len(np) != 0:
                    response = response + "Can you tell me more about " + np[0].pluralize() + "?"
                else:
                    response = response + "Can you tell me more?"
                print(response)
    
    print("It was nice talking to you, goodbye!")

# Start the program
main()