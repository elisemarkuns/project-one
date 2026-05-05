import random

# Function containing the logic for magic eight ball
def magic_eight_ball(question=None,return_answer_as_string=False):
    answer_list = ((("It is certain."),("It is decidedly so."),("Without a doubt."),("Yes, definitely."),("You may rely on it.")),  # Positive answers 1 (5x)
                   (("As I see it, yes."),("Most likely."),("Outlook good."),("Yes"),("Signs point to yes.")),  # Positive answers 2 (5x)
                   (("Reply hazy, try again."),("Ask again later."),("Better not tell you now."),("Cannot predict now."),("Concentrate and ask again.")),   # Non-committal answers (5)
                   (("Don't count on it."),("My reply is no."),("My sources say no."),("Outlook not so good."),("Very doubtful")))   # Negative answers (5)

    if not question:
        question = input("What is your question for magic eight-ball? ")
    
    random.seed()
    answer = answer_list[random.randint(0,3)][random.randint(0,4)]

    if not return_answer_as_string:
        print(f"Magic ball responds: {answer}")
    else:
        return answer
    

# Function that runs eight_ball() function in different ways to make sure it works
def test_magic_eight_ball():
    # Run eight_ball() once without arguments
    print("Running eight_ball() once without arguments:\n")
    magic_eight_ball()


    # Repeatedly run eight_ball() by passing the question as an argument and requesting the answer to be returned as a string
    print("\n\nRunning eight_ball(q,return_answer_as_string=True).\n"
            "q : a question of string type. Passing a question as an argument skips asking user for input and the variable gets discarded.\n"
            "return_answer_as_string=True : indicates to the function to not print the answer and instead return it as a string for user to process.\n")

    for n in range(5):
        q = f"question {n+1}"   # The only purpose of passing the question is to skip asking user for input, the actual string is irrelevant and discarded
        print(f"Question passed to function: {q}")
        print(f"Magic ball responds: {magic_eight_ball(q,return_answer_as_string=True)}")

#--------------------------------------------------#







#--------------------------#
# Main loop of the program #
#--------------------------#
def main():
    test_magic_eight_ball()




if __name__ =="__main__":
    main()
