import random

#--------------------------#
# Magic Eight Ball section #
#--------------------------#

# Function containing the logic for magic eight ball
def magic_eight_ball(question=None,print_answer=True):
                    # Positive answers 1 (5x)
    answers_tuple = ((("It is certain."),("It is decidedly so."),("Without a doubt."),("Yes, definitely."),("You may rely on it.")),
                    # Positive answers 2 (5x)
                   (("As I see it, yes."),("Most likely."),("Outlook good."),("Yes"),("Signs point to yes.")),
                    # Non-committal answers (5x)
                   (("Reply hazy, try again."),("Ask again later."),("Better not tell you now."),("Cannot predict now."),("Concentrate and ask again.")),
                    # Negative answers (5x)
                   (("Don't count on it."),("My reply is no."),("My sources say no."),("Outlook not so good."),("Very doubtful")))

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
# Fortune cookie section #
#------------------------#
def fortune_cookie(print_answer=True):
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
    fortune = f"{fortunes_tuple[random.randint(0,9)]}"
    numbers = f"{random.randint(1,99)} {random.randint(1,99)} {random.randint(1,99)} {random.randint(1,99)}"
    # Check if function call passed a True argument
    # if yes, print the fortune, otherwise skip
    if print_answer:
        print(f"{fortune}\n{numbers}")

    return fortune, numbers


def test_fortune_cookie():
    # By running the function with the argument True, we are telling the function 
    # to print the output and we don't have to print or format it ourselves.
    print("Run fortune_cookie function 5 times with 'True' argument and let the function print the raw output:\n")
    for n in range(5):
        fortune_cookie(True)

    # Run fortune_cookie function 5 times with "False" argument telling the function to not print the output. 
    # We handle printing the fortune ourselves.
    print("\n\nRun fortune_cookie function 5 times with 'False' argument and format the output ourselves:\n")
    for n in range(5):
        fortune, numbers = fortune_cookie(False)
        print(f"You crack open the fortune cookie and see a rolled up piece of paper inside.\n"
              f"You carefully unroll it and see that there is text on it.\n"
              f"It says: \"{fortune}\"\n"
              f"You notice there are numbers beneath the text: {numbers}\n"
              f"You wonder what all of this means...\n")


#-------------------#
# Fizz Buzz section #
#-------------------#
def fizz_buzz(print_answer=True):
    # We could just print the output, but we're gonna save it to a list for more modularity
    output = []
    for n in range(1,101):
        # Here we append a new item to the list every time we increment our loop
        output.append(n)

        # We check if n is divisible by 3 without a remainder
        # If it does, we replace the list item associated
        # with our place in the loop with 'Fizz'
        if n % 3 == 0:
            output[n-1] = 'Fizz'
        
        # Check if n is divisible by 5 without a remainder
        if n % 5 == 0:
            # Check if the list item associated with the place
            # in the loop has already been changed to 'Fizz'
            # (which would only be possible if it passed the check for division by 3)
            if output[n-1] == 'Fizz':
                # Add 'Buzz' to the output list item (which should already be 'Fizz')
                output[n-1] = output[n-1] + 'Buzz'
            else:
                # If the item does not match 'Fizz' (not divisible by 3)
                # Instead of adding to, we replace the value with 'Buzz'
                output[n-1] = 'Buzz'
        # Check if the function was called with a print_answer=True argument
        # and if it is, print the current list item in the loop                
        if print_answer:
            print(output[n-1])
    
    # Return the full list so the user can choose to format the output different 
    # or do anything else with the output
    return output

#--------------------------#
# Main loop of the program #
#--------------------------#
def main():
    #test_magic_eight_ball()
    #test_fortune_cookie()
    fizz_buzz()
    pass



if __name__ =="__main__":
    main()
