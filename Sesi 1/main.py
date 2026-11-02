from top import welcome_message,exit_program
from Games import lord
from Games import warung_mini

def menu():
    user_option = int(input(f'Menu Program:\n1. Games Lord\n2. Warung Mini\n3. Keluar progam\n\nsilahkan pilih: '))

    if user_option == 1:
        lord.start()
    elif user_option == 2:
        warung_mini.start()
    elif user_option == 3:
        exit_program ()
    else:
        print('hanya boleh pilih yang tersedia di menu!')
       
def main():
    welcome_message()
    menu() 
    
if __name__ == "__main__":
    main()