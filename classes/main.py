import arcade
from constants import *
from word_list import word_list
from states import PlayState

class MyWindow(arcade.Window):
    """
    MyWindow Class creates a window class based off the parent window class provided by Python Arcade
    as a base to display our states onto
    """
    
    def __init__(self):
        super().__init__( SCREEN_WIDTH, SCREEN_HEIGHT, 'Wordle' )
             
def main():
    window = MyWindow()
    window.center_window()
    
    play_state = PlayState( word_list )
    play_state.setup()
    window.show_view( play_state )
    
    arcade.run()
    
if __name__ == "__main__":
    main()