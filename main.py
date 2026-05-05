import random
from os import system   # needed to clear console screen


#--------------------------#
# Program selection screen #
#--------------------------#
class Menu():
    
    def __init__(self):
        self.exit = False
        self.show_menu()

    def receive_user_input(self, question=""):
        user_input = input(question)
        return user_input

    def show_header(self):
        # Clear console
        system('clear')
        # Print the menu header
        print(  f"________________________________________\n"
                f"___________Python Project One___________\n"
                f"__________________by____________________\n"
                f"_____________Elise_Markuns______________\n"
                f"________________________________________\n")

    def show_menu(self):
        # Keep looping until it's time to exit the application
        while not self.exit:
            
            self.show_header()
            print(  f"1. Magic Eight Ball\n"
                    f"2. Fortune Cookie generator\n"
                    f"3. Print Fizz Buzz\n"
                    f"\n"
                    f"Type a number (1-3) to select which program to run (or \"q\" to exit): ")
        
            # Keep looping until it's time exit the application
            while True or not self.exit:
                selection = self.receive_user_input()
                if selection.lower().find("q") == 0:
                    self.exit_program()

                match selection:
                    case "1":
                        self.show_magic_eight_ball()
                        break
                    case "2":
                        self.show_fortune_cookie()
                        break
                    case "3":
                        self.show_fizz_buzz()
                        break                        
                    case _:
                        print("Input has to be a number 1-3 (1 or 2 or 3) or \"q\" to quit.")
            
        self.exit_program()
                    
    def exit_program(self):
        self.exit = True
        print("Thank you for checking this project out. Now exiting...")
        exit()         
        

    

    #--------------------------#
    # Magic Eight Ball section #
    #--------------------------#
    def show_magic_eight_ball(self):
        while True:
            self.show_header()
            if self.magic_eight_ball()=="exit":
                return
            
            while True:
                print("Would you like to ask again? (Y/n)")
                selection = self.receive_user_input()

                if selection.lower().find("n")==0:
                    return
                elif selection.lower().find("y")==0 or selection=="":
                    break
                elif selection.lower().find("y")!=0:
                    print("Input has to be Y or N")

    # Function containing the logic for magic eight ball
    def magic_eight_ball(self,question=None,print_answer=True):
                        # Positive answers 1 (5x)
        answers_tuple = ((("It is certain."),("It is decidedly so."),("Without a doubt."),("Yes, definitely."),("You may rely on it.")),
                        # Positive answers 2 (5x)
                        (("As I see it, yes."),("Most likely."),("Outlook good."),("Yes"),("Signs point to yes.")),
                        # Non-committal answers (5x)
                        (("Reply hazy, try again."),("Ask again later."),("Better not tell you now."),("Cannot predict now."),("Concentrate and ask again.")),
                        # Negative answers (5x)
                        (("Don't count on it."),("My reply is no."),("My sources say no."),("Outlook not so good."),("Very doubtful")))
        
        # If no question is passed to function, ask user to type in their question
        while not question:
            question = self.receive_user_input("What is your question for magic eight-ball? ")
            # Check if user input "q" and the length of the input is less than or equal to 4 characters (i.e if they typed in "quit")
            # Exit if the check passes
            if question.lower().find("q") == 0 and len(question)<= 4:
                print("Exiting Magic Eight Ball. Press Enter to continue:")
                self.receive_user_input()
                return "exit"
            # If no question was typed in, ask user to type it again
            if question == "" or question == None:
                print("Please type in your question or type Quit to exit the program:")
        
        # Update the rng seed and generate the answer
        random.seed()
        answer = answers_tuple[random.randint(0,3)][random.randint(0,4)]

        if print_answer:
            print(f"Magic ball responds: {answer}")
        
        return answer
    

    #------------------------#
    # Fortune cookie section #
    #------------------------#
    def show_fortune_cookie(self):
        while True:
            self.show_header()
            self.fortune_cookie()
            
            while True:
                print("Would you like to generate another fortune? (Y/n)")
                selection = self.receive_user_input()

                if selection.lower().find("n")==0:
                    return
                elif selection.lower().find("y")==0 or selection=="":
                    break
                elif selection.lower().find("y")!=0:
                    print("Input has to be Y or N")
        
    # Function generating the fortune cookie fortune
    def fortune_cookie(self,print_answer=True):
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

    
    #-------------------#
    # Fizz Buzz section #
    #-------------------#
    def show_fizz_buzz(self):
        self.show_header()
        
        fizz_list = self.fizz_buzz(False)

        for i in range(len(fizz_list)):
            # print without newline
            # align string to right, add padding to 8 total characters (same length as FizzBuzz)
            print(f"{fizz_list[i]:>9}",end=' ')
            # every 10 items, print a newline
            if (i+1)%10==0:
                print()
            
        print()
        # Wait for user input before we continue and clear the console
        print("Press Enter key to continue: ")
        selection = self.receive_user_input()
        
            
    def fizz_buzz(self,print_answer=True):
        # We could just print the output without saving it to a list, 
        # but we're gonna save it for more customizability
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
    #fizz_buzz()
    menu = Menu()



if __name__ =="__main__":
    main()
