import pyemenu_dev as pyemenu 
from pyemenu_dev import Colors, Title, Text, Menu, Checkboxlist, Form, Entry, Checkbox
from pyemenu_dev import getKeyboard, setCursor, clear_screen
from readchar import key

def main():
    foreground = Colors.green
    background = Colors.white
    name = 'Name'
    surname = Text('Surname', fg=Colors.red, bg=Colors.Navy)
    last_name = Text('Last Name', fg=Colors.Navy)
    age = Entry('Age', validation='int',
                 bg=Colors.yellow, placeholder_bg=Colors.pink)
    credit = Checkbox('Card')
    password = Entry('Password', validation='password',
                 bg=Colors.yellow)    
    options = [name, surname, last_name, age, credit,password]
    title = Title('New User')
    cursor = Text('~>')
    menu1 = Form(options, title=title, cursor=cursor, fg=foreground, bg=background)
    # Initialazing Variables
    pointer = 0
    wrap = 2
    keyboard = ''
    while True:
        clear_screen()
        menu1.print(pointer=pointer, 
                    keyboard=keyboard, 
                    wrap=wrap,
                    highlight=True,
                    fg_hl=Colors.black, 
                    bg_hl=Colors.LimeGreen,
                    title_align='center', 
                    padding_bottom=True,
                    padding_up=True
                    )
        survey = menu1.survey
        print(f"Max len item: {menu1.max_len_item}")
        print(f"Max len Value: {menu1.max_len_values}")
        
        keyboard = getKeyboard()
        pointer = setCursor(keyboard, pointer, menu1.entries, wrap)
        if keyboard in ["q", "Q"]:
            break
    
    print(f"User registered: {survey}")
    

if __name__ == '__main__':
    main()