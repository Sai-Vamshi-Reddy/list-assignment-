#user interface to the main menu
import data
import functions
def show_main_menu():
  while True:
    print("Solomon diner") #edit to show your name
    print("__________")
    print('N for a new order')
    print('C to change an order')
    print('X for close orders and print the check')
    print('P for to print the check')
    print('Q for quit')
    user_menu_choice = input('Your choice: ')
    if user_menu_choice in 'Qq':
      print("Exiting... Thank you for visiting!")
      break
    elif user_menu_choice in 'Xx':
      print('This option prints the list of items ordered, extended price, total, Taxes, and Grand total ')
      print('Closing orders and printing the check:')
      functions.print_check(order)
      order = functions.reset_order() 
      break
    elif user_menu_choice in 'Nn':
      print('New order')
      make_order(user_menu_choice.upper(),order)  #calls a function for adding to the orders
     elif user_menu_choice in 'Cc':
      print('Modify your current order:')
      order = modify_order(user_menu_choice.upper(),order)  # Modify the existing order
    elif user_menu_choice in 'Pp':
      if order == []:
          print("No Items, Please order first")
      else:
        functions.print_check(order)
    else:
      print("Invalid input. Please try again.")
def make_order(menu_choice):
  print('Functionality for menu choice ', menu_choice)
  user_selection = functions.get_item_number()
  item_code, quantity = user_selection.split()
  print(functions.get_item_information(item_code))

def close_order(menu_choice):
  print('Functionality for menu choice ', menu_choice)



if __name__ == '__main__':
    #initialize the lists
    drinks = []
    appetizers = []
    salads = []
    entrees = []
    dessert= []
    #print(functions.get_item_information('D1'))
    show_main_menu()


