import arcade
from constants import *
from word_list import word_list
from word_list import choosable_word_list
from states import PlayState

class MyWindow(arcade.Window):
    """
    MyWindow Class creates a window class based off the parent window class provided by Python Arcade
    as a base to display our states onto
    """
    
    def __init__(self):
        super().__init__( SCREEN_WIDTH, SCREEN_HEIGHT, 'Wordle Clone' )
             
def main():
    # Creates a window object to display states onto
    window = MyWindow()
    window.center_window()
    
    # Creates our playstate object and displays it onto the window
    play_state = PlayState( word_list, choosable_word_list )
    play_state.setup()
    window.show_view( play_state )
    
    arcade.run()
    
if __name__ == "__main__":
    main()
