import random

#--------------------------#
# Magic Eight Ball section #
#--------------------------#

# Function containing the logic for magic eight ball
def magic_eight_ball(question=None,print_answer=True):
    answers_tuple = ((("It is certain."),("It is decidedly so."),("Without a doubt."),("Yes, definitely."),("You may rely on it.")),  # Positive answers 1 (5x)
                   (("As I see it, yes."),("Most likely."),("Outlook good."),("Yes"),("Signs point to yes.")),  # Positive answers 2 (5x)
                   (("Reply hazy, try again."),("Ask again later."),("Better not tell you now."),("Cannot predict now."),("Concentrate and ask again.")),   # Non-committal answers (5)
                   (("Don't count on it."),("My reply is no."),("My sources say no."),("Outlook not so good."),("Very doubtful")))   # Negative answers (5)

    if not question:
        question = input("What is your question for magic eight-ball? ")
    
    random.seed()
    answer = answers_tuple[random.randint(0,3)][random.randint(0,4)]

    if print_answer:
        print(f"Magic ball responds: {answer}")
    
    return answer
    

# Function that runs eight_ball() function in different ways to make sure it works
def test_magic_eight_ball():
    # Run eight_ball() once without arguments
    print("Running eight_ball() once without arguments:\n")
    magic_eight_ball()


    # Repeatedly run eight_ball() by passing the question as an argument and requesting the answer to be returned as a string
    print("\n\nRunning eight_ball(q,return_answer_as_string=True).\n"
            "q : a question of string type. Passing a question as an argument skips asking user for input and the variable gets discarded.\n"
            "print_answer=True : indicates to the function to not print the answer and only return it as a string for user to process.\n")

    for n in range(5):
        q = f"question {n+1}"   # The value of the question string is irrelevant and discarded
        print(f"Question passed to function: {q}")
        print(f"Magic ball responds: {magic_eight_ball(q,print_answer=False)}")



#------------------------#
#-Fortune cookie section-#
#------------------------#
def fortune_cookie(print_answer=False):
    # A tuple of 10 fortunes to pull from (generated with Gemma4)
    fortunes_tuple = (  "You will encounter an unexpected delight today. Keep your mind open and enjoy the surprise.",
                        "Patience is a profound asset. What you are waiting for is worth the wait.",
                        "A simple change in perspective will lead you to a rewarding breakthrough. Look at things differently.",
                        "Fortune favors the curious mind. Your next great adventure begins with a question.",
                        "Kindness is a language that the world understands. Share your warmth generously.",
                        "The perfect opportunity will present itself when you least expect it. Be observant and ready.",
                        "Growth comes after comfort. Be brave enough to step outside your familiar routine.",
                        "Harmony awaits where disagreement once stood. Seek peace and understanding today.",
                        "Unexpected connections will enrich your life. Talk to someone you rarely speak with.",
                        "Today's greatest reward is the knowledge you gain. Keep learning, keep moving forward.")
    # Set seed for random number generator
    # running seed() without an argument uses system time as the seed
    random.seed()
    
    # Generate a random fortune
    fortune = f"{fortunes_tuple[random.range(0,9)]}\n{random.range(1,99)} {random.range(1,99)} {random.range(1,99)} {random.range(1,99)}"
    
    # Check if function call passed a True argument
    # if yes, print the fortune, otherwise skip
    if print_answer:
        print(fortune)

    return fortune





#--------------------------#
# Main loop of the program #
#--------------------------#
def main():
    #test_magic_eight_ball()




if __name__ =="__main__":
    main()
