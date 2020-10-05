import ui
#import artstore
import art
from database import Artist, Artwork

def main():
    while True:
        option = ui.menu_option(ui)
        if option == 'task1':
            art.add_artist()
        elif option == 'task2':
            art.add_artwork()
        elif option == 'task3':
            art.delete_art_work()
        elif option == 'task4':
            art.show_all_artwork_by_one_artist()
        elif option == 'task5':
            pass
        elif option == 'task6':
            pass
        elif option == 'task7':
            pass
        elif option == 'q':
            quit_program()
            break

           



def quit_program():
    ui.message('Thanks and bye!')

if __name__ == '__main__':
    main()    
