#!/usr/bin/env python

import sys
import os

main_donors = [("Luke Skywalker", [100.25, 200.55, 50]),
          ("Han Solo", [100.80, 50.99, 600]),
          ("Yoda", [1000.01, 50, 600.55, 200.47]),
          ("Ben Kenobe", [101.32, 500, 60.34]),
          ]

def clear_screen():
    """
    clears the command screen
    """
    os.system("cls" if os.name == "nt" else "clear")


def show_list():
    """
    shows the donors in the list without donation amounts
    \n"""
    print("#" * 9, "The Current Donor List", "#" * 9)
    index = 1
    for donor in main_donors:
        print("{}:{} ~ {}".format(index, donor[0], str(donor[1]).replace("[","").replace("]","")))
        index += 1
    print("#" * 43 + "\n")
    return show_list

def main_menu():
    """
    Main menu options
    """
    prompt = input("\n".join(("\nWelcome to the Mailroom!",
"Please choose from one of the options below:\n",
"1: Send a Thank You",
"2: Create a Report",
"3: Quit",
">>> ")))
    return prompt

def menu_thank_you():
    """
    Menu to user to enter options for thank you
    """
    print("""\nTo whom would you like to send a Thank You?
Please enter full name""")
    thanks_answer = input("""
Enter 'LIST' to see Donor list or 'MENU' to return to Main Menu.
>>> """)
    return thanks_answer


def send_email(name, amount):
    print("""\n
    Dear {n},
       Thank you for your generous donation of ${a}! This will help our cause
       immensely in our battle against the darkside.  You, {n} , have made a big 
       difference in our efforts and we greatly appreciate you!!!  Your ${a} will be 
       put to great use to our forces against evil!  

       Thank you,

       The FORCE
    
    \n""".format(n = name, a = amount))

def send_thank_you():
    """
    Either adds to list or adds a new donor to the list and  a 
    new donation amount 
    """
    clear_screen()
    while True:
        thanks_answer = menu_thank_you().strip()
        if thanks_answer.upper() == "LIST":
            clear_screen()
            show_list()
        elif thanks_answer.upper() == "MENU":
            clear_screen()
            break
        else:
            idx = len(main_donors)-1
            in_main_donors = False
            for x in range(len(main_donors)-1, -1, -1):
                if main_donors[x][0].lower() == thanks_answer.lower():
                    in_main_donors = True
                    print("\nThe Donor you have selected is {}".format(thanks_answer))
                    donation_amount = float(input("\nPlease enter the amount that {} kindly donated: ".format(thanks_answer)))
                    main_donors[idx][1].append(donation_amount)
                    print("{}: ${:.2f}".format(thanks_answer, donation_amount))
                idx -= 1
            
            if in_main_donors == False:
                donation_amount = float(input("\nPlease enter {}'s donated amount: ".format(thanks_answer)))
                add_new_donors = (thanks_answer,[donation_amount])
                main_donors.append(add_new_donors)
                print("{} was added with a donation of ${:.2f}".format(thanks_answer,float(donation_amount)))
            
            send_email(thanks_answer, donation_amount)



def report_menu():
    """
    Menu for Create a Report and to give the user an option to exit
    """
    report_menu_answer = input(""" 
    Welcome to the 'Create a Report option'!
Enter 'MENU' to exit and return to the Main Menu
Press Enter to continue
 >>> \n""")

    return report_menu_answer


def gen_stats(main_donors):
    donor_stats = []
    lst = main_donors
    for donor in lst:
        donations = donor[1]
        total = sum(donations)
        num = len(donations)
        avg = round(total / num, 2)
        stats = [donor[0], total, num, avg]
        donor_stats.append(stats)

    return donor_stats

def create_report():
    """
    Generates the report of donors by donation amount from greatest to least
    """
    while True:
        response = report_menu().strip()
        if response.upper() == "MENU":
            break
        else:
            stats_list = gen_stats(main_donors)
            stats_list.sort(key=lambda stats_list: stats_list[1],reverse=True)
            
            print("{:<20}|{:^15}|{:^15}|{:>15}".format("Donor Name", "Total Given", "Num Gifts", "Average Gifts"))
            print("-" * 68)
            for donor in stats_list:
                print("{:<20}${:>15} {:>15} ${:>15}".format(donor[0], donor[1], donor[2], donor[3]))
            print("\nEnd of Report\n")    
       

def quit():
    print("You are leaving the Mailroom!")
    sys.exit()

def mailroom_main():
    """
    Main mailroom script
    """
    while True:
        answer = main_menu().strip()
        if answer == "1":
            send_thank_you()
        elif answer == "2":
            create_report()
        elif answer == "3":
            quit()
        else:
            print("Please choose a number 1-3")


if __name__ == "__main__": mailroom_main()
