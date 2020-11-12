# Frontend for the chargen explorer. From here we call backend functions and make the user interface #

import CharGen
import os

CHARS_LIST = []


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def character_details(index):

    for i, char in enumerate(CHARS_LIST):
        if i == index:
            print("{0}, {1}\n\n{2}\n{3}".format(CHARS_LIST[index].get_name(),
                                              CHARS_LIST[index].get_gender(),
                                              CHARS_LIST[index].describe_appearance(),
                                              CHARS_LIST[index].describe_appearance_detail()))

def select_menu():
    view_chars_running = True
    while view_chars_running:

        clear_terminal()
        for i, item in enumerate(CHARS_LIST):
            print("({0}) {1}, {2}".format(i + 1, item.get_name(), item.gender))

        view_chars_menu = input("\nSelect a character, or enter 0 to exit.\n")
        if view_chars_menu == "0":
            view_chars_running = False
            clear_terminal()
            main_menu()

        try:
            clear_terminal()
            character_details(int(view_chars_menu) - 1)
        except Exception:
            print("Please enter a valid index.\n")

        print("(0) Go back.\n")
        view_chars_submenu = input()
        if view_chars_submenu == "0":
            clear_terminal()
            select_menu()
        else:
            pass

def main_menu():
    #clear_terminal()
    print("(1) Generate a list of random characters with user-defined parameters.\n"
          "(2) Generate a single character with user-defined parameters.\n"
          "(3) View generated characters.\n"
          "(4) Exit.")

    running = True
    while running:
        menu = input()

        # generate N random chars
        if menu == "1":
            clear_terminal()
            n = input("Please enter your desired number of characters to generate.\n")

            clear_terminal()
            m_ratio = input("Please enter your desired ratio of males to females from 0 to 1.\n"
                            "For example, 0.7 indicates about 70% males.\n")

            clear_terminal()
            vm_ratio = input("Please enter your desired ratio of veiled males from 0 to 1.\n")

            clear_terminal()
            vf_ratio = input("Please enter your desired ratio of veiled females from 0 to 1.\n")

            clear_terminal()
            chars_temp = CharGen.generate_characters(int(n), float(m_ratio), float(vm_ratio), float(vf_ratio))
            for char in chars_temp:
                print("{0}, {1}".format(char.get_name(), char.get_gender()))

            print("\n(1) Re-generate.\n"
                  "(2) Done.")

            regen_running = True
            while regen_running:
                regen_menu = input()

                if regen_menu == "1":
                    clear_terminal()
                    chars_temp = CharGen.generate_characters(int(n), float(m_ratio), float(vm_ratio), float(vf_ratio))
                    for char in chars_temp:
                        print("{0}, {1}".format(char.get_name(), char.get_gender()))

                    print("\n(1) Re-generate.\n"
                          "(2) Done.")

                elif regen_menu == "2":
                    regen_running = False
                    clear_terminal()
                    for char in chars_temp:
                        CHARS_LIST.append(char)
                    main_menu()

        # generate 1 random char with specified attributes
        elif menu == "2":
            clear_terminal()
            gen = input("Please enter the gender of the desired character. male/female\n")

            clear_terminal()
            veil_temp = input("Please specify if the character is veiled or not. True/False\n")
            if veil_temp == "true" or veil_temp == "True":
                veil = True
            elif veil_temp == "false" or veil_temp == "False":
                veil = False

            clear_terminal()
            chars_temp = [CharGen.generate_single_character(gen, veil)]
            for char in chars_temp:
                print("{0}, {1}".format(char.get_name(), char.get_gender()))

            print("\n(1) Re-generate.\n"
                  "(2) Done.")

            regen_running = True
            while regen_running:
                regen_menu = input()

                if regen_menu == "1":
                    clear_terminal()
                    chars_temp = [CharGen.generate_single_character(gen, veil)]
                    for char in chars_temp:
                        print("{0}, {1}".format(char.get_name(), char.get_gender()))

                    print("\n(1) Re-generate.\n"
                          "(2) Done.")

                elif regen_menu == "2":
                    regen_running = False
                    clear_terminal()
                    for char in chars_temp:
                        CHARS_LIST.append(char)
                    main_menu()

        # view the list of characters
        elif menu == "3":
            clear_terminal()
            select_menu()


        # exit
        elif menu == "4":
            running = False
            clear_terminal()
            quit(0)

        # handle invalid command
        else:
            clear_terminal()
            print("Please enter a valid command.\n\n")
            print("(1) Generate a list of random characters with user-defined parameters.\n"
                  "(2) Generate a single character with user-defined parameters.\n"
                  "(3) View generated characters."
                  "(4) Exit.\n")


clear_terminal()

print("Welcome to CharGenExplorer.\nThis is a demo for an early iteration of the Nebhos character generator.\n"
      "Type one of the numbers corresponding to the options below to get started.\n")

main_menu()
