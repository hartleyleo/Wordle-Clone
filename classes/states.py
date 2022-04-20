import arcade
from word_list import word_list
from word_list import choosable_word_list
from constants import *
import random
import arcade.gui
import time

class PlayState ( arcade.View ):
    
    def __init__( self, word_list, choosable_word_list ):
        super().__init__()
        
        # Establish variable for use in program
        self.background = None
        
        self.chosen_word = None
        
        # word list imported from file
        self.word_list = word_list
        self.choosable_word_list = choosable_word_list
        
        self.guess = None
        self.guess_count = None
        
        # Below variables used solely for displaying letters on screen, and their accuracy after guessed
        # -------------------------------
        self.line_one = None
        self.line_two = None
        self.line_three = None
        self.line_four = None
        self.line_five = None
        self.line_six = None
        
        self.line_one_accuracy = None
        self.line_two_accuracy = None
        self.line_three_accuracy = None
        self.line_four_accuracy = None
        self.line_five_accuracy = None
        self.line_six_accuracy = None
        # -------------------------------
        
        # UIManager to handle the UI.
        self.manager = arcade.gui.UIManager()
        self.manager.enable()
        
        # Create a vertical BoxGroup to align buttons
        self.v_box = arcade.gui.UIBoxLayout()

        # Create buttons for the menu
        #------------------------------------------------------------------------------
        # Each button is a UITextureButton through the arcade library
        help_button = arcade.gui.UITextureButton(
            texture=arcade.load_texture('resources/buttons/help_button_unpressed.png'), 
            texture_pressed=arcade.load_texture('resources/buttons/help_button_pressed.png'),
            scale=0.8
        )
        
        # Buttons are then added to the v_box to be easily organized
        self.v_box.add(help_button.with_space_around(bottom=20))

        # Create a widget to hold the v_box widget, that will center the buttons
        self.manager.add( arcade.gui.UIAnchorWidget( anchor_x="center_x", anchor_y="center_y", child=self.v_box, align_y=+300, align_x=+230) )

        # Use a decorator to handle on_click events
        @help_button.event("on_click")
        def on_click_start(event):
            self.manager.disable()
            next_state = HelpState( self )
            next_state.setup()
            self.window.show_view( next_state )
        
    def setup( self ):
        # Setup Background
        self.background = arcade.load_texture("resources/background.png")
        
        # Get the word from the imported word list
        self.chosen_word = self.choose_word()
        print(self.chosen_word)
        
        # Used to keep track of current guess for display purposes
        self.guess = ''
        self.guess_count = 1
        
        # Below variables used solely for displaying letters on screen, and their accuracy after guessed
        # --------------------------------------------------------
        self.line_one = ''
        self.line_two = ''
        self.line_three = ''
        self.line_four = ''
        self.line_five = ''
        self.line_six = ''
        
        self.line_one_accuracy = [ 'N', 'N', 'N', 'N', 'N' ]
        self.line_two_accuracy = [ 'N', 'N', 'N', 'N', 'N' ]
        self.line_three_accuracy = [ 'N', 'N', 'N', 'N', 'N' ]
        self.line_four_accuracy = [ 'N', 'N', 'N', 'N', 'N' ]
        self.line_five_accuracy = [ 'N', 'N', 'N', 'N', 'N' ]
        self.line_six_accuracy = [ 'N', 'N', 'N', 'N', 'N' ]
        # --------------------------------------------------------
        
        # Allows mouse to be visible on screen in this menu
        self.window.set_mouse_visible(True)
        
    def on_draw( self ):
        # Clears screen
        self.clear()
        
        # Displays background
        arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        
        # Draws the buttons onto the screen
        self.manager.draw()
        
        # Draws the letters and guesses
        self.draw_letters_to_screen()
    
    def draw_letters_to_screen( self ):
        """
        Function to draw letters to the screen, and shows their accuracy after each guess
        """
        if self.guess_count == 1:
            
            if len(self.guess) == 1:
                arcade.draw_text( self.guess[0], COLUMN_ONE_WIDTH, LINE_ONE_HEIGHT, 
                         arcade.color.WHITE, font_size=25, anchor_x="center" )
                
            if len(self.guess) == 2:
                arcade.draw_text( self.guess[0], COLUMN_ONE_WIDTH, LINE_ONE_HEIGHT, 
                         arcade.color.WHITE, font_size=25, anchor_x="center" )
                arcade.draw_text( self.guess[1], COLUMN_TWO_WIDTH, LINE_ONE_HEIGHT, 
                         arcade.color.WHITE, font_size=25, anchor_x="center" )
                
            if len(self.guess) == 3:
                arcade.draw_text( self.guess[0], COLUMN_ONE_WIDTH, LINE_ONE_HEIGHT, 
                         arcade.color.WHITE, font_size=25, anchor_x="center" )
                arcade.draw_text( self.guess[1], COLUMN_TWO_WIDTH, LINE_ONE_HEIGHT, 
                         arcade.color.WHITE, font_size=25, anchor_x="center" )
                arcade.draw_text( self.guess[2], COLUMN_THREE_WIDTH, LINE_ONE_HEIGHT, 
                         arcade.color.WHITE, font_size=25, anchor_x="center" )
            
            if len(self.guess) == 4:
                arcade.draw_text( self.guess[0], COLUMN_ONE_WIDTH, LINE_ONE_HEIGHT, 
                         arcade.color.WHITE, font_size=25, anchor_x="center" )
                arcade.draw_text( self.guess[1], COLUMN_TWO_WIDTH, LINE_ONE_HEIGHT, 
                         arcade.color.WHITE, font_size=25, anchor_x="center" )
                arcade.draw_text( self.guess[2], COLUMN_THREE_WIDTH, LINE_ONE_HEIGHT, 
                         arcade.color.WHITE, font_size=25, anchor_x="center" )
                arcade.draw_text( self.guess[3], COLUMN_FOUR_WIDTH, LINE_ONE_HEIGHT, 
                         arcade.color.WHITE, font_size=25, anchor_x="center" )
                
            if len(self.guess) == 5:
                arcade.draw_text( self.guess[0], COLUMN_ONE_WIDTH, LINE_ONE_HEIGHT, 
                         arcade.color.WHITE, font_size=25, anchor_x="center" )
                arcade.draw_text( self.guess[1], COLUMN_TWO_WIDTH, LINE_ONE_HEIGHT, 
                         arcade.color.WHITE, font_size=25, anchor_x="center" )
                arcade.draw_text( self.guess[2], COLUMN_THREE_WIDTH, LINE_ONE_HEIGHT, 
                         arcade.color.WHITE, font_size=25, anchor_x="center" )
                arcade.draw_text( self.guess[3], COLUMN_FOUR_WIDTH, LINE_ONE_HEIGHT, 
                         arcade.color.WHITE, font_size=25, anchor_x="center" )
                arcade.draw_text( self.guess[4], COLUMN_FIVE_WIDTH, LINE_ONE_HEIGHT, 
                         arcade.color.WHITE, font_size=25, anchor_x="center" )
        
        if self.guess_count == 2:
            
            """
            Draw the first line
            """
            for i in range( len( self.line_one_accuracy ) ):
                if self.line_one_accuracy[i] == 'N':
                    arcade.draw_text( self.line_one[i], COLUMN_ONE_WIDTH + i*100, LINE_ONE_HEIGHT, 
                            arcade.color.WHITE, font_size=25, anchor_x="center" )
                if self.line_one_accuracy[i] == 'W':
                    arcade.draw_text( self.line_one[i], COLUMN_ONE_WIDTH + i*100, LINE_ONE_HEIGHT, 
                            arcade.color.GOLDEN_POPPY, font_size=25, anchor_x="center" )
                if self.line_one_accuracy[i] == 'C':
                    arcade.draw_text( self.line_one[i], COLUMN_ONE_WIDTH + i*100, LINE_ONE_HEIGHT, 
                            arcade.color.GO_GREEN, font_size=25, anchor_x="center" )
            
            
            if len(self.guess) == 1:
                arcade.draw_text( self.guess[0], COLUMN_ONE_WIDTH, LINE_TWO_HEIGHT, 
                         arcade.color.WHITE, font_size=25, anchor_x="center" )
                
            if len(self.guess) == 2:
                arcade.draw_text( self.guess[0], COLUMN_ONE_WIDTH, LINE_TWO_HEIGHT, 
                         arcade.color.WHITE, font_size=25, anchor_x="center" )
                arcade.draw_text( self.guess[1], COLUMN_TWO_WIDTH, LINE_TWO_HEIGHT, 
                         arcade.color.WHITE, font_size=25, anchor_x="center" )
                
            if len(self.guess) == 3:
                arcade.draw_text( self.guess[0], COLUMN_ONE_WIDTH, LINE_TWO_HEIGHT, 
                         arcade.color.WHITE, font_size=25, anchor_x="center" )
                arcade.draw_text( self.guess[1], COLUMN_TWO_WIDTH, LINE_TWO_HEIGHT, 
                         arcade.color.WHITE, font_size=25, anchor_x="center" )
                arcade.draw_text( self.guess[2], COLUMN_THREE_WIDTH, LINE_TWO_HEIGHT, 
                         arcade.color.WHITE, font_size=25, anchor_x="center" )
            
            if len(self.guess) == 4:
                arcade.draw_text( self.guess[0], COLUMN_ONE_WIDTH, LINE_TWO_HEIGHT, 
                         arcade.color.WHITE, font_size=25, anchor_x="center" )
                arcade.draw_text( self.guess[1], COLUMN_TWO_WIDTH, LINE_TWO_HEIGHT, 
                         arcade.color.WHITE, font_size=25, anchor_x="center" )
                arcade.draw_text( self.guess[2], COLUMN_THREE_WIDTH, LINE_TWO_HEIGHT, 
                         arcade.color.WHITE, font_size=25, anchor_x="center" )
                arcade.draw_text( self.guess[3], COLUMN_FOUR_WIDTH, LINE_TWO_HEIGHT, 
                         arcade.color.WHITE, font_size=25, anchor_x="center" )
                
            if len(self.guess) == 5:
                arcade.draw_text( self.guess[0], COLUMN_ONE_WIDTH, LINE_TWO_HEIGHT, 
                         arcade.color.WHITE, font_size=25, anchor_x="center" )
                arcade.draw_text( self.guess[1], COLUMN_TWO_WIDTH, LINE_TWO_HEIGHT, 
                         arcade.color.WHITE, font_size=25, anchor_x="center" )
                arcade.draw_text( self.guess[2], COLUMN_THREE_WIDTH, LINE_TWO_HEIGHT, 
                         arcade.color.WHITE, font_size=25, anchor_x="center" )
                arcade.draw_text( self.guess[3], COLUMN_FOUR_WIDTH, LINE_TWO_HEIGHT, 
                         arcade.color.WHITE, font_size=25, anchor_x="center" )
                arcade.draw_text( self.guess[4], COLUMN_FIVE_WIDTH, LINE_TWO_HEIGHT, 
                         arcade.color.WHITE, font_size=25, anchor_x="center" )
                
        if self.guess_count == 3:
            
            """
            Draw the first line
            """
            for i in range( len( self.line_one_accuracy ) ):
                
                if self.line_one_accuracy[i] == 'N':
                    arcade.draw_text( self.line_one[i], COLUMN_ONE_WIDTH + i*100, LINE_ONE_HEIGHT, 
                            arcade.color.WHITE, font_size=25, anchor_x="center" )
                if self.line_one_accuracy[i] == 'W':
                    arcade.draw_text( self.line_one[i], COLUMN_ONE_WIDTH + i*100, LINE_ONE_HEIGHT, 
                            arcade.color.GOLDEN_POPPY, font_size=25, anchor_x="center" )
                if self.line_one_accuracy[i] == 'C':
                    arcade.draw_text( self.line_one[i], COLUMN_ONE_WIDTH + i*100, LINE_ONE_HEIGHT, 
                            arcade.color.GO_GREEN, font_size=25, anchor_x="center" )
            
            """
            Draw the second line
            """
            for i in range( len( self.line_two_accuracy ) ):
                
                if self.line_two_accuracy[i] == 'N':
                    arcade.draw_text( self.line_two[i], COLUMN_ONE_WIDTH + i*100, LINE_TWO_HEIGHT, 
                            arcade.color.WHITE, font_size=25, anchor_x="center" )
                if self.line_two_accuracy[i] == 'W':
                    arcade.draw_text( self.line_two[i], COLUMN_ONE_WIDTH + i*100, LINE_TWO_HEIGHT, 
                            arcade.color.GOLDEN_POPPY, font_size=25, anchor_x="center" )
                if self.line_two_accuracy[i] == 'C':
                    arcade.draw_text( self.line_two[i], COLUMN_ONE_WIDTH + i*100, LINE_TWO_HEIGHT, 
                            arcade.color.GO_GREEN, font_size=25, anchor_x="center" )
            
            
            if len(self.guess) == 1:
                arcade.draw_text( self.guess[0], COLUMN_ONE_WIDTH, LINE_THREE_HEIGHT, 
                         arcade.color.WHITE, font_size=25, anchor_x="center" )
                
            if len(self.guess) == 2:
                arcade.draw_text( self.guess[0], COLUMN_ONE_WIDTH, LINE_THREE_HEIGHT, 
                         arcade.color.WHITE, font_size=25, anchor_x="center" )
                arcade.draw_text( self.guess[1], COLUMN_TWO_WIDTH, LINE_THREE_HEIGHT, 
                         arcade.color.WHITE, font_size=25, anchor_x="center" )
                
            if len(self.guess) == 3:
                arcade.draw_text( self.guess[0], COLUMN_ONE_WIDTH, LINE_THREE_HEIGHT, 
                         arcade.color.WHITE, font_size=25, anchor_x="center" )
                arcade.draw_text( self.guess[1], COLUMN_TWO_WIDTH, LINE_THREE_HEIGHT, 
                         arcade.color.WHITE, font_size=25, anchor_x="center" )
                arcade.draw_text( self.guess[2], COLUMN_THREE_WIDTH, LINE_THREE_HEIGHT, 
                         arcade.color.WHITE, font_size=25, anchor_x="center" )
            
            if len(self.guess) == 4:
                arcade.draw_text( self.guess[0], COLUMN_ONE_WIDTH, LINE_THREE_HEIGHT, 
                         arcade.color.WHITE, font_size=25, anchor_x="center" )
                arcade.draw_text( self.guess[1], COLUMN_TWO_WIDTH, LINE_THREE_HEIGHT, 
                         arcade.color.WHITE, font_size=25, anchor_x="center" )
                arcade.draw_text( self.guess[2], COLUMN_THREE_WIDTH, LINE_THREE_HEIGHT, 
                         arcade.color.WHITE, font_size=25, anchor_x="center" )
                arcade.draw_text( self.guess[3], COLUMN_FOUR_WIDTH, LINE_THREE_HEIGHT, 
                         arcade.color.WHITE, font_size=25, anchor_x="center" )
                
            if len(self.guess) == 5:
                arcade.draw_text( self.guess[0], COLUMN_ONE_WIDTH, LINE_THREE_HEIGHT, 
                         arcade.color.WHITE, font_size=25, anchor_x="center" )
                arcade.draw_text( self.guess[1], COLUMN_TWO_WIDTH, LINE_THREE_HEIGHT, 
                         arcade.color.WHITE, font_size=25, anchor_x="center" )
                arcade.draw_text( self.guess[2], COLUMN_THREE_WIDTH, LINE_THREE_HEIGHT, 
                         arcade.color.WHITE, font_size=25, anchor_x="center" )
                arcade.draw_text( self.guess[3], COLUMN_FOUR_WIDTH, LINE_THREE_HEIGHT, 
                         arcade.color.WHITE, font_size=25, anchor_x="center" )
                arcade.draw_text( self.guess[4], COLUMN_FIVE_WIDTH, LINE_THREE_HEIGHT, 
                         arcade.color.WHITE, font_size=25, anchor_x="center" )
                
        if self.guess_count == 4:
            
            """
            Draw the first line
            """
            for i in range( len( self.line_one_accuracy ) ):
                
                if self.line_one_accuracy[i] == 'N':
                    arcade.draw_text( self.line_one[i], COLUMN_ONE_WIDTH + i*100, LINE_ONE_HEIGHT, 
                            arcade.color.WHITE, font_size=25, anchor_x="center" )
                if self.line_one_accuracy[i] == 'W':
                    arcade.draw_text( self.line_one[i], COLUMN_ONE_WIDTH + i*100, LINE_ONE_HEIGHT, 
                            arcade.color.GOLDEN_POPPY, font_size=25, anchor_x="center" )
                if self.line_one_accuracy[i] == 'C':
                    arcade.draw_text( self.line_one[i], COLUMN_ONE_WIDTH + i*100, LINE_ONE_HEIGHT, 
                            arcade.color.GO_GREEN, font_size=25, anchor_x="center" )
            
            """
            Draw the second line
            """
            for i in range( len( self.line_two_accuracy ) ):
                
                if self.line_two_accuracy[i] == 'N':
                    arcade.draw_text( self.line_two[i], COLUMN_ONE_WIDTH + i*100, LINE_TWO_HEIGHT, 
                            arcade.color.WHITE, font_size=25, anchor_x="center" )
                if self.line_two_accuracy[i] == 'W':
                    arcade.draw_text( self.line_two[i], COLUMN_ONE_WIDTH + i*100, LINE_TWO_HEIGHT, 
                            arcade.color.GOLDEN_POPPY, font_size=25, anchor_x="center" )
                if self.line_two_accuracy[i] == 'C':
                    arcade.draw_text( self.line_two[i], COLUMN_ONE_WIDTH + i*100, LINE_TWO_HEIGHT, 
                            arcade.color.GO_GREEN, font_size=25, anchor_x="center" )
            
            """
            Draw the third line
            """
            for i in range( len( self.line_three_accuracy ) ):
                
                if self.line_three_accuracy[i] == 'N':
                    arcade.draw_text( self.line_three[i], COLUMN_ONE_WIDTH + i*100, LINE_THREE_HEIGHT, 
                            arcade.color.WHITE, font_size=25, anchor_x="center" )
                if self.line_three_accuracy[i] == 'W':
                    arcade.draw_text( self.line_three[i], COLUMN_ONE_WIDTH + i*100, LINE_THREE_HEIGHT, 
                            arcade.color.GOLDEN_POPPY, font_size=25, anchor_x="center" )
                if self.line_three_accuracy[i] == 'C':
                    arcade.draw_text( self.line_three[i], COLUMN_ONE_WIDTH + i*100, LINE_THREE_HEIGHT, 
                            arcade.color.GO_GREEN, font_size=25, anchor_x="center" )            
            
            if len(self.guess) == 1:
                arcade.draw_text( self.guess[0], COLUMN_ONE_WIDTH, LINE_FOUR_HEIGHT, 
                         arcade.color.WHITE, font_size=25, anchor_x="center" )
                
            if len(self.guess) == 2:
                arcade.draw_text( self.guess[0], COLUMN_ONE_WIDTH, LINE_FOUR_HEIGHT, 
                         arcade.color.WHITE, font_size=25, anchor_x="center" )
                arcade.draw_text( self.guess[1], COLUMN_TWO_WIDTH, LINE_FOUR_HEIGHT, 
                         arcade.color.WHITE, font_size=25, anchor_x="center" )
                
            if len(self.guess) == 3:
                arcade.draw_text( self.guess[0], COLUMN_ONE_WIDTH, LINE_FOUR_HEIGHT, 
                         arcade.color.WHITE, font_size=25, anchor_x="center" )
                arcade.draw_text( self.guess[1], COLUMN_TWO_WIDTH, LINE_FOUR_HEIGHT, 
                         arcade.color.WHITE, font_size=25, anchor_x="center" )
                arcade.draw_text( self.guess[2], COLUMN_THREE_WIDTH, LINE_FOUR_HEIGHT, 
                         arcade.color.WHITE, font_size=25, anchor_x="center" )
            
            if len(self.guess) == 4:
                arcade.draw_text( self.guess[0], COLUMN_ONE_WIDTH, LINE_FOUR_HEIGHT, 
                         arcade.color.WHITE, font_size=25, anchor_x="center" )
                arcade.draw_text( self.guess[1], COLUMN_TWO_WIDTH, LINE_FOUR_HEIGHT, 
                         arcade.color.WHITE, font_size=25, anchor_x="center" )
                arcade.draw_text( self.guess[2], COLUMN_THREE_WIDTH, LINE_FOUR_HEIGHT, 
                         arcade.color.WHITE, font_size=25, anchor_x="center" )
                arcade.draw_text( self.guess[3], COLUMN_FOUR_WIDTH, LINE_FOUR_HEIGHT, 
                         arcade.color.WHITE, font_size=25, anchor_x="center" )
                
            if len(self.guess) == 5:
                arcade.draw_text( self.guess[0], COLUMN_ONE_WIDTH, LINE_FOUR_HEIGHT, 
                         arcade.color.WHITE, font_size=25, anchor_x="center" )
                arcade.draw_text( self.guess[1], COLUMN_TWO_WIDTH, LINE_FOUR_HEIGHT, 
                         arcade.color.WHITE, font_size=25, anchor_x="center" )
                arcade.draw_text( self.guess[2], COLUMN_THREE_WIDTH, LINE_FOUR_HEIGHT, 
                         arcade.color.WHITE, font_size=25, anchor_x="center" )
                arcade.draw_text( self.guess[3], COLUMN_FOUR_WIDTH, LINE_FOUR_HEIGHT, 
                         arcade.color.WHITE, font_size=25, anchor_x="center" )
                arcade.draw_text( self.guess[4], COLUMN_FIVE_WIDTH, LINE_FOUR_HEIGHT, 
                         arcade.color.WHITE, font_size=25, anchor_x="center" )
        
        if self.guess_count == 5:
            
            """
            Draw the first line
            """
            for i in range( len( self.line_one_accuracy ) ):
                
                if self.line_one_accuracy[i] == 'N':
                    arcade.draw_text( self.line_one[i], COLUMN_ONE_WIDTH + i*100, LINE_ONE_HEIGHT, 
                            arcade.color.WHITE, font_size=25, anchor_x="center" )
                if self.line_one_accuracy[i] == 'W':
                    arcade.draw_text( self.line_one[i], COLUMN_ONE_WIDTH + i*100, LINE_ONE_HEIGHT, 
                            arcade.color.GOLDEN_POPPY, font_size=25, anchor_x="center" )
                if self.line_one_accuracy[i] == 'C':
                    arcade.draw_text( self.line_one[i], COLUMN_ONE_WIDTH + i*100, LINE_ONE_HEIGHT, 
                            arcade.color.GO_GREEN, font_size=25, anchor_x="center" )
            
            """
            Draw the second line
            """
            for i in range( len( self.line_two_accuracy ) ):
                
                if self.line_two_accuracy[i] == 'N':
                    arcade.draw_text( self.line_two[i], COLUMN_ONE_WIDTH + i*100, LINE_TWO_HEIGHT, 
                            arcade.color.WHITE, font_size=25, anchor_x="center" )
                if self.line_two_accuracy[i] == 'W':
                    arcade.draw_text( self.line_two[i], COLUMN_ONE_WIDTH + i*100, LINE_TWO_HEIGHT, 
                            arcade.color.GOLDEN_POPPY, font_size=25, anchor_x="center" )
                if self.line_two_accuracy[i] == 'C':
                    arcade.draw_text( self.line_two[i], COLUMN_ONE_WIDTH + i*100, LINE_TWO_HEIGHT, 
                            arcade.color.GO_GREEN, font_size=25, anchor_x="center" )
            
            """
            Draw the third line
            """
            for i in range( len( self.line_three_accuracy ) ):
                
                if self.line_three_accuracy[i] == 'N':
                    arcade.draw_text( self.line_three[i], COLUMN_ONE_WIDTH + i*100, LINE_THREE_HEIGHT, 
                            arcade.color.WHITE, font_size=25, anchor_x="center" )
                if self.line_three_accuracy[i] == 'W':
                    arcade.draw_text( self.line_three[i], COLUMN_ONE_WIDTH + i*100, LINE_THREE_HEIGHT, 
                            arcade.color.GOLDEN_POPPY, font_size=25, anchor_x="center" )
                if self.line_three_accuracy[i] == 'C':
                    arcade.draw_text( self.line_three[i], COLUMN_ONE_WIDTH + i*100, LINE_THREE_HEIGHT, 
                            arcade.color.GO_GREEN, font_size=25, anchor_x="center" )
            
            """
            Draw the fourth line
            """
            for i in range( len( self.line_four_accuracy ) ):
                
                if self.line_four_accuracy[i] == 'N':
                    arcade.draw_text( self.line_four[i], COLUMN_ONE_WIDTH + i*100, LINE_FOUR_HEIGHT, 
                            arcade.color.WHITE, font_size=25, anchor_x="center" )
                if self.line_four_accuracy[i] == 'W':
                    arcade.draw_text( self.line_four[i], COLUMN_ONE_WIDTH + i*100, LINE_FOUR_HEIGHT, 
                            arcade.color.GOLDEN_POPPY, font_size=25, anchor_x="center" )
                if self.line_four_accuracy[i] == 'C':
                    arcade.draw_text( self.line_four[i], COLUMN_ONE_WIDTH + i*100, LINE_FOUR_HEIGHT, 
                            arcade.color.GO_GREEN, font_size=25, anchor_x="center" )
            
            
            if len(self.guess) == 1:
                arcade.draw_text( self.guess[0], COLUMN_ONE_WIDTH, LINE_FIVE_HEIGHT, 
                         arcade.color.WHITE, font_size=25, anchor_x="center" )
                
            if len(self.guess) == 2:
                arcade.draw_text( self.guess[0], COLUMN_ONE_WIDTH, LINE_FIVE_HEIGHT, 
                         arcade.color.WHITE, font_size=25, anchor_x="center" )
                arcade.draw_text( self.guess[1], COLUMN_TWO_WIDTH, LINE_FIVE_HEIGHT, 
                         arcade.color.WHITE, font_size=25, anchor_x="center" )
                
            if len(self.guess) == 3:
                arcade.draw_text( self.guess[0], COLUMN_ONE_WIDTH, LINE_FIVE_HEIGHT, 
                         arcade.color.WHITE, font_size=25, anchor_x="center" )
                arcade.draw_text( self.guess[1], COLUMN_TWO_WIDTH, LINE_FIVE_HEIGHT, 
                         arcade.color.WHITE, font_size=25, anchor_x="center" )
                arcade.draw_text( self.guess[2], COLUMN_THREE_WIDTH, LINE_FIVE_HEIGHT, 
                         arcade.color.WHITE, font_size=25, anchor_x="center" )
            
            if len(self.guess) == 4:
                arcade.draw_text( self.guess[0], COLUMN_ONE_WIDTH, LINE_FIVE_HEIGHT, 
                         arcade.color.WHITE, font_size=25, anchor_x="center" )
                arcade.draw_text( self.guess[1], COLUMN_TWO_WIDTH, LINE_FIVE_HEIGHT, 
                         arcade.color.WHITE, font_size=25, anchor_x="center" )
                arcade.draw_text( self.guess[2], COLUMN_THREE_WIDTH, LINE_FIVE_HEIGHT, 
                         arcade.color.WHITE, font_size=25, anchor_x="center" )
                arcade.draw_text( self.guess[3], COLUMN_FOUR_WIDTH, LINE_FIVE_HEIGHT, 
                         arcade.color.WHITE, font_size=25, anchor_x="center" )
                
            if len(self.guess) == 5:
                arcade.draw_text( self.guess[0], COLUMN_ONE_WIDTH, LINE_FIVE_HEIGHT, 
                         arcade.color.WHITE, font_size=25, anchor_x="center" )
                arcade.draw_text( self.guess[1], COLUMN_TWO_WIDTH, LINE_FIVE_HEIGHT, 
                         arcade.color.WHITE, font_size=25, anchor_x="center" )
                arcade.draw_text( self.guess[2], COLUMN_THREE_WIDTH, LINE_FIVE_HEIGHT, 
                         arcade.color.WHITE, font_size=25, anchor_x="center" )
                arcade.draw_text( self.guess[3], COLUMN_FOUR_WIDTH, LINE_FIVE_HEIGHT, 
                         arcade.color.WHITE, font_size=25, anchor_x="center" )
                arcade.draw_text( self.guess[4], COLUMN_FIVE_WIDTH, LINE_FIVE_HEIGHT, 
                         arcade.color.WHITE, font_size=25, anchor_x="center" )
        
        if self.guess_count == 6:
            
            """
            Draw the first line
            """
            for i in range( len( self.line_one_accuracy ) ):
                
                if self.line_one_accuracy[i] == 'N':
                    arcade.draw_text( self.line_one[i], COLUMN_ONE_WIDTH + i*100, LINE_ONE_HEIGHT, 
                            arcade.color.WHITE, font_size=25, anchor_x="center" )
                if self.line_one_accuracy[i] == 'W':
                    arcade.draw_text( self.line_one[i], COLUMN_ONE_WIDTH + i*100, LINE_ONE_HEIGHT, 
                            arcade.color.GOLDEN_POPPY, font_size=25, anchor_x="center" )
                if self.line_one_accuracy[i] == 'C':
                    arcade.draw_text( self.line_one[i], COLUMN_ONE_WIDTH + i*100, LINE_ONE_HEIGHT, 
                            arcade.color.GO_GREEN, font_size=25, anchor_x="center" )
            
            """
            Draw the second line
            """
            for i in range( len( self.line_two_accuracy ) ):
                
                if self.line_two_accuracy[i] == 'N':
                    arcade.draw_text( self.line_two[i], COLUMN_ONE_WIDTH + i*100, LINE_TWO_HEIGHT, 
                            arcade.color.WHITE, font_size=25, anchor_x="center" )
                if self.line_two_accuracy[i] == 'W':
                    arcade.draw_text( self.line_two[i], COLUMN_ONE_WIDTH + i*100, LINE_TWO_HEIGHT, 
                            arcade.color.GOLDEN_POPPY, font_size=25, anchor_x="center" )
                if self.line_two_accuracy[i] == 'C':
                    arcade.draw_text( self.line_two[i], COLUMN_ONE_WIDTH + i*100, LINE_TWO_HEIGHT, 
                            arcade.color.GO_GREEN, font_size=25, anchor_x="center" )
            
            """
            Draw the third line
            """
            for i in range( len( self.line_three_accuracy ) ):
                
                if self.line_three_accuracy[i] == 'N':
                    arcade.draw_text( self.line_three[i], COLUMN_ONE_WIDTH + i*100, LINE_THREE_HEIGHT, 
                            arcade.color.WHITE, font_size=25, anchor_x="center" )
                if self.line_three_accuracy[i] == 'W':
                    arcade.draw_text( self.line_three[i], COLUMN_ONE_WIDTH + i*100, LINE_THREE_HEIGHT, 
                            arcade.color.GOLDEN_POPPY, font_size=25, anchor_x="center" )
                if self.line_three_accuracy[i] == 'C':
                    arcade.draw_text( self.line_three[i], COLUMN_ONE_WIDTH + i*100, LINE_THREE_HEIGHT, 
                            arcade.color.GO_GREEN, font_size=25, anchor_x="center" )
            
            """
            Draw the fourth line
            """
            for i in range( len( self.line_four_accuracy ) ):
                
                if self.line_four_accuracy[i] == 'N':
                    arcade.draw_text( self.line_four[i], COLUMN_ONE_WIDTH + i*100, LINE_FOUR_HEIGHT, 
                            arcade.color.WHITE, font_size=25, anchor_x="center" )
                if self.line_four_accuracy[i] == 'W':
                    arcade.draw_text( self.line_four[i], COLUMN_ONE_WIDTH + i*100, LINE_FOUR_HEIGHT, 
                            arcade.color.GOLDEN_POPPY, font_size=25, anchor_x="center" )
                if self.line_four_accuracy[i] == 'C':
                    arcade.draw_text( self.line_four[i], COLUMN_ONE_WIDTH + i*100, LINE_FOUR_HEIGHT, 
                            arcade.color.GO_GREEN, font_size=25, anchor_x="center" )
            
            """
            Draw the fifth line
            """
            for i in range( len( self.line_five_accuracy ) ):
                
                if self.line_five_accuracy[i] == 'N':
                    arcade.draw_text( self.line_five[i], COLUMN_ONE_WIDTH + i*100, LINE_FIVE_HEIGHT, 
                            arcade.color.WHITE, font_size=25, anchor_x="center" )
                if self.line_five_accuracy[i] == 'W':
                    arcade.draw_text( self.line_five[i], COLUMN_ONE_WIDTH + i*100, LINE_FIVE_HEIGHT, 
                            arcade.color.GOLDEN_POPPY, font_size=25, anchor_x="center" )
                if self.line_five_accuracy[i] == 'C':
                    arcade.draw_text( self.line_five[i], COLUMN_ONE_WIDTH + i*100, LINE_FIVE_HEIGHT, 
                            arcade.color.GO_GREEN, font_size=25, anchor_x="center" )
            
            if len(self.guess) == 1:
                arcade.draw_text( self.guess[0], COLUMN_ONE_WIDTH, LINE_SIX_HEIGHT, 
                         arcade.color.WHITE, font_size=25, anchor_x="center" )
                
            if len(self.guess) == 2:
                arcade.draw_text( self.guess[0], COLUMN_ONE_WIDTH, LINE_SIX_HEIGHT, 
                         arcade.color.WHITE, font_size=25, anchor_x="center" )
                arcade.draw_text( self.guess[1], COLUMN_TWO_WIDTH, LINE_SIX_HEIGHT, 
                         arcade.color.WHITE, font_size=25, anchor_x="center" )
                
            if len(self.guess) == 3:
                arcade.draw_text( self.guess[0], COLUMN_ONE_WIDTH, LINE_SIX_HEIGHT, 
                         arcade.color.WHITE, font_size=25, anchor_x="center" )
                arcade.draw_text( self.guess[1], COLUMN_TWO_WIDTH, LINE_SIX_HEIGHT, 
                         arcade.color.WHITE, font_size=25, anchor_x="center" )
                arcade.draw_text( self.guess[2], COLUMN_THREE_WIDTH, LINE_SIX_HEIGHT, 
                         arcade.color.WHITE, font_size=25, anchor_x="center" )
            
            if len(self.guess) == 4:
                arcade.draw_text( self.guess[0], COLUMN_ONE_WIDTH, LINE_SIX_HEIGHT, 
                         arcade.color.WHITE, font_size=25, anchor_x="center" )
                arcade.draw_text( self.guess[1], COLUMN_TWO_WIDTH, LINE_SIX_HEIGHT, 
                         arcade.color.WHITE, font_size=25, anchor_x="center" )
                arcade.draw_text( self.guess[2], COLUMN_THREE_WIDTH, LINE_SIX_HEIGHT, 
                         arcade.color.WHITE, font_size=25, anchor_x="center" )
                arcade.draw_text( self.guess[3], COLUMN_FOUR_WIDTH, LINE_SIX_HEIGHT, 
                         arcade.color.WHITE, font_size=25, anchor_x="center" )
                
            if len(self.guess) == 5:
                arcade.draw_text( self.guess[0], COLUMN_ONE_WIDTH, LINE_SIX_HEIGHT, 
                         arcade.color.WHITE, font_size=25, anchor_x="center" )
                arcade.draw_text( self.guess[1], COLUMN_TWO_WIDTH, LINE_SIX_HEIGHT, 
                         arcade.color.WHITE, font_size=25, anchor_x="center" )
                arcade.draw_text( self.guess[2], COLUMN_THREE_WIDTH, LINE_SIX_HEIGHT, 
                         arcade.color.WHITE, font_size=25, anchor_x="center" )
                arcade.draw_text( self.guess[3], COLUMN_FOUR_WIDTH, LINE_SIX_HEIGHT, 
                         arcade.color.WHITE, font_size=25, anchor_x="center" )
                arcade.draw_text( self.guess[4], COLUMN_FIVE_WIDTH, LINE_SIX_HEIGHT, 
                         arcade.color.WHITE, font_size=25, anchor_x="center" )
        
        if self.guess_count > 6:
            
            """
            Draw the first line
            """
            for i in range( len( self.line_one_accuracy ) ):
                
                if self.line_one_accuracy[i] == 'N':
                    arcade.draw_text( self.line_one[i], COLUMN_ONE_WIDTH + i*100, LINE_ONE_HEIGHT, 
                            arcade.color.WHITE, font_size=25, anchor_x="center" )
                if self.line_one_accuracy[i] == 'W':
                    arcade.draw_text( self.line_one[i], COLUMN_ONE_WIDTH + i*100, LINE_ONE_HEIGHT, 
                            arcade.color.GOLDEN_POPPY, font_size=25, anchor_x="center" )
                if self.line_one_accuracy[i] == 'C':
                    arcade.draw_text( self.line_one[i], COLUMN_ONE_WIDTH + i*100, LINE_ONE_HEIGHT, 
                            arcade.color.GO_GREEN, font_size=25, anchor_x="center" )
            
            """
            Draw the second line
            """
            for i in range( len( self.line_two_accuracy ) ):
                
                if self.line_two_accuracy[i] == 'N':
                    arcade.draw_text( self.line_two[i], COLUMN_ONE_WIDTH + i*100, LINE_TWO_HEIGHT, 
                            arcade.color.WHITE, font_size=25, anchor_x="center" )
                if self.line_two_accuracy[i] == 'W':
                    arcade.draw_text( self.line_two[i], COLUMN_ONE_WIDTH + i*100, LINE_TWO_HEIGHT, 
                            arcade.color.GOLDEN_POPPY, font_size=25, anchor_x="center" )
                if self.line_two_accuracy[i] == 'C':
                    arcade.draw_text( self.line_two[i], COLUMN_ONE_WIDTH + i*100, LINE_TWO_HEIGHT, 
                            arcade.color.GO_GREEN, font_size=25, anchor_x="center" )
            
            """
            Draw the third line
            """
            for i in range( len( self.line_three_accuracy ) ):
                
                if self.line_three_accuracy[i] == 'N':
                    arcade.draw_text( self.line_three[i], COLUMN_ONE_WIDTH + i*100, LINE_THREE_HEIGHT, 
                            arcade.color.WHITE, font_size=25, anchor_x="center" )
                if self.line_three_accuracy[i] == 'W':
                    arcade.draw_text( self.line_three[i], COLUMN_ONE_WIDTH + i*100, LINE_THREE_HEIGHT, 
                            arcade.color.GOLDEN_POPPY, font_size=25, anchor_x="center" )
                if self.line_three_accuracy[i] == 'C':
                    arcade.draw_text( self.line_three[i], COLUMN_ONE_WIDTH + i*100, LINE_THREE_HEIGHT, 
                            arcade.color.GO_GREEN, font_size=25, anchor_x="center" )
            
            """
            Draw the fourth line
            """
            for i in range( len( self.line_four_accuracy ) ):
                
                if self.line_four_accuracy[i] == 'N':
                    arcade.draw_text( self.line_four[i], COLUMN_ONE_WIDTH + i*100, LINE_FOUR_HEIGHT, 
                            arcade.color.WHITE, font_size=25, anchor_x="center" )
                if self.line_four_accuracy[i] == 'W':
                    arcade.draw_text( self.line_four[i], COLUMN_ONE_WIDTH + i*100, LINE_FOUR_HEIGHT, 
                            arcade.color.GOLDEN_POPPY, font_size=25, anchor_x="center" )
                if self.line_four_accuracy[i] == 'C':
                    arcade.draw_text( self.line_four[i], COLUMN_ONE_WIDTH + i*100, LINE_FOUR_HEIGHT, 
                            arcade.color.GO_GREEN, font_size=25, anchor_x="center" )
            
            """
            Draw the fifth line
            """
            for i in range( len( self.line_five_accuracy ) ):
                
                if self.line_five_accuracy[i] == 'N':
                    arcade.draw_text( self.line_five[i], COLUMN_ONE_WIDTH + i*100, LINE_FIVE_HEIGHT, 
                            arcade.color.WHITE, font_size=25, anchor_x="center" )
                if self.line_five_accuracy[i] == 'W':
                    arcade.draw_text( self.line_five[i], COLUMN_ONE_WIDTH + i*100, LINE_FIVE_HEIGHT, 
                            arcade.color.GOLDEN_POPPY, font_size=25, anchor_x="center" )
                if self.line_five_accuracy[i] == 'C':
                    arcade.draw_text( self.line_five[i], COLUMN_ONE_WIDTH + i*100, LINE_FIVE_HEIGHT, 
                            arcade.color.GO_GREEN, font_size=25, anchor_x="center" )
            
            """
            Draw the sixth line
            """
            for i in range( len( self.line_six_accuracy ) ):
                
                if self.line_six_accuracy[i] == 'N':
                    arcade.draw_text( self.line_five[i], COLUMN_ONE_WIDTH + i*100, LINE_FIVE_HEIGHT, 
                            arcade.color.WHITE, font_size=25, anchor_x="center" )
                if self.line_six_accuracy[i] == 'W':
                    arcade.draw_text( self.line_five[i], COLUMN_ONE_WIDTH + i*100, LINE_SIX_HEIGHT, 
                            arcade.color.GOLDEN_POPPY, font_size=25, anchor_x="center" )
                if self.line_six_accuracy[i] == 'C':
                    arcade.draw_text( self.line_five[i], COLUMN_ONE_WIDTH + i*100, LINE_SIX_HEIGHT, 
                            arcade.color.GO_GREEN, font_size=25, anchor_x="center" )
        
    def on_update( self, delta_time ):
        
        if self.guess_count == 1:
            self.line_one = self.guess
            
        if self.guess_count == 2:
            self.line_two = self.guess
            
        if self.guess_count == 3:
            self.line_three = self.guess
            
        if self.guess_count == 4:
            self.line_four = self.guess
            
        if self.guess_count == 5:
            self.line_five = self.guess
            
        if self.guess_count == 6:
            self.line_six = self.guess
        
    def choose_word( self ):
        """
        Function randomly chooses a word from the imported word list to be used
        """
        index = random.randint( 0, len( self.choosable_word_list ) - 1 )
        return self.choosable_word_list[index]
        
    def check_word( self ):
        """
        Function to determine if the word is correct or not, and handle them appropriately
        """
        
        # If the guess is correct
        if self.guess == self.chosen_word: 
                
             # Loads the end state and displays it
            new_state = GameOverState( self.guess_count, self.chosen_word )
            new_state.setup()
            self.window.show_view( new_state )
                
        # If the guess is a word but not the right one
        else:
                
            if self.guess_count == 6:
                """
                END THE GAME, OUT OF GUESSES
                """
                new_state = GameOverState( self.guess_count, self.chosen_word )
                new_state.setup()
                self.window.show_view( new_state )
                
            # Gets the accuracy of the guessed word
            word_accuracy = self.get_guess_index_accuracy()
                
            # Set the word accuracy for drawing purposes
            if self.guess_count == 1:
                self.line_one_accuracy = word_accuracy
            elif self.guess_count == 2:
                self.line_two_accuracy = word_accuracy
            elif self.guess_count == 3:
                self.line_three_accuracy = word_accuracy
            elif self.guess_count == 4:
                self.line_four_accuracy = word_accuracy
            elif self.guess_count == 5:
                self.line_five_accuracy = word_accuracy
            elif self.guess_count == 6:
                self.line_six_accuracy = word_accuracy
                           
    def get_guess_index_accuracy( self ):
        """
        Function creates a list with all letters either correct, in the wrong spot, or not in the word
        """
        
        correct_spot_indexes = self.letter_is_in_correct_spot()
        incorrect_spot_indexes = self.letter_is_in_word()
        
        # Creates a list for the draw function to check and determine the color of each letter 
        # N(ot in) = not in the word
        # W(rong spot) = in the wrong spot
        # C(orrect spot) = in the right spot
        word_accuracy = [ 'N', 'N', 'N', 'N', 'N' ]
        
        for i in range( len( incorrect_spot_indexes ) ):
            word_accuracy[incorrect_spot_indexes[i]] = 'W'
            
        for i in range( len( correct_spot_indexes ) ):
            word_accuracy[correct_spot_indexes[i]] = 'C'
        
        return word_accuracy
        
    def letter_is_in_correct_spot( self ):
        """
        Function to find if a letter is in the word at the right spot
        """
        correct_spot_indexes = []
        
        for i in range( len( self.chosen_word ) ):
            if self.guess[i] == self.chosen_word[i]:
                correct_spot_indexes.append( i )
        
        return correct_spot_indexes
    
    def letter_is_in_word( self ):
        """
        Function to find if a letter is in the word, but in the wrong spot
        """
        incorrect_spot_indexes = []
        
        for i in range( len( self.chosen_word ) ):
            for j in range( len( self.chosen_word ) ):
                if self.guess[i] == self.chosen_word[j]:
                    incorrect_spot_indexes.append( i )
        
        return incorrect_spot_indexes
        
    def word_is_valid( self ):
        """"
        Function checks to see if the word is valid to be checked: in the word list
        """
        if self.guess in self.word_list or self.guess in self.choosable_word_list:
            return True
    
    def guess_length_full( self, guess ):
        """
        Function to check if the length of thee current guess is at length 5
        """
        if len( guess ) == 5:
            return True
       
    def on_key_press( self, key, modifiers ):
        """Called whenever a key is pressed. """

        if key == arcade.key.BACKSPACE:
            self.guess = self.guess[:-1]
            
        if key == arcade.key.ENTER:
            if self.guess_length_full( self.guess ):
                
                # Checks if the word is a valid guess ( length is 5, and in the word list )
                if self.word_is_valid():
                    self.check_word()
                    self.guess = ''
                    self.guess_count += 1
                    
            else:
                pass

        elif key == arcade.key.A:
            if not self.guess_length_full( self.guess ):
                self.guess += 'A'
                
        elif key == arcade.key.B:
            if not self.guess_length_full( self.guess ):
                self.guess += 'B'
                
        elif key == arcade.key.C:
            if not self.guess_length_full( self.guess ):
                self.guess += 'C'
                
        elif key == arcade.key.D:
            if not self.guess_length_full( self.guess ):
                self.guess += 'D'
                
        elif key == arcade.key.E:
            if not self.guess_length_full( self.guess ):
                self.guess += 'E'
                
        elif key == arcade.key.F:
            if not self.guess_length_full( self.guess ):
                self.guess += 'F'
                
        elif key == arcade.key.G:
            if not self.guess_length_full( self.guess ):
                self.guess += 'G'
                
        elif key == arcade.key.H:
            if not self.guess_length_full( self.guess ):
                self.guess += 'H'
                
        elif key == arcade.key.I:
            if not self.guess_length_full( self.guess ):
                self.guess += 'I'
                
        elif key == arcade.key.J:
            if not self.guess_length_full( self.guess ):
                self.guess += 'J'
                
        elif key == arcade.key.K:
            if not self.guess_length_full( self.guess ):
                self.guess += 'K'
                
        elif key == arcade.key.L:
            if not self.guess_length_full( self.guess ):
                self.guess += 'L'
                
        elif key == arcade.key.M:
            if not self.guess_length_full( self.guess ):
                self.guess += 'M'
        
        elif key == arcade.key.N:
            if not self.guess_length_full( self.guess ):
                self.guess += 'N'
                
        elif key == arcade.key.O:
            if not self.guess_length_full( self.guess ):
                self.guess += 'O'
                
        elif key == arcade.key.P:
            if not self.guess_length_full( self.guess ):
                self.guess += 'P'
                
        elif key == arcade.key.Q:
            if not self.guess_length_full( self.guess ):
                self.guess += 'Q'
                
        elif key == arcade.key.R:
            if not self.guess_length_full( self.guess ):
                self.guess += 'R'
                
        elif key == arcade.key.S:
            if not self.guess_length_full( self.guess ):
                self.guess += 'S'
                
        elif key == arcade.key.T:
            if not self.guess_length_full( self.guess ):
                self.guess += 'T'
                
        elif key == arcade.key.U:
            if not self.guess_length_full( self.guess ):
                self.guess += 'U'
                
        elif key == arcade.key.V:
            if not self.guess_length_full( self.guess ):
                self.guess += 'V'
                
        elif key == arcade.key.W:
            if not self.guess_length_full( self.guess ):
                self.guess += 'W'
        
        elif key == arcade.key.X:
            if not self.guess_length_full( self.guess ):
                self.guess += 'X'
        
        elif key == arcade.key.Y:
            if not self.guess_length_full( self.guess ):
                self.guess += 'Y'
        
        elif key == arcade.key.Z:
            if not self.guess_length_full( self.guess ):
                self.guess += 'Z'    
                          
class GameOverState ( arcade.View ):
    
    def __init__( self, guess_count, word ):
        super().__init__()
        
        # Get info from previous state to display on the end game state
        self.word = word
        self.guess_count = guess_count
        
        # UIManager to handle the UI.
        self.manager = arcade.gui.UIManager()
        self.manager.enable()
        
        # Establish background variable
        self.background = None
        
        # Create a vertical BoxGroup to align buttons
        self.v_box = arcade.gui.UIBoxLayout()

        # Create buttons for the menu
        #------------------------------------------------------------------------------
        # Each button is a UITextureButton through the arcade library
        start_button = arcade.gui.UITextureButton(
            texture=arcade.load_texture('resources/buttons/start_button_unpressed.png'), 
            texture_pressed=arcade.load_texture('resources/buttons/start_button_pressed.png'),
            scale=1
        )
        
        quit_button = arcade.gui.UITextureButton(
            texture=arcade.load_texture('resources/buttons/quit_button_unpressed.png'), 
            texture_pressed=arcade.load_texture('resources/buttons/quit_button_pressed.png'), 
            scale=1
        )
        
        # Buttons are then added to the v_box to be easily organized
        self.v_box.add(start_button.with_space_around(bottom=20))
        self.v_box.add(quit_button)

        # Create a widget to hold the v_box widget, that will center the buttons
        self.manager.add( arcade.gui.UIAnchorWidget( anchor_x="center_x", anchor_y="center_y", child=self.v_box, align_y=-100) )

        # Use a decorator to handle on_click events
        @start_button.event("on_click")
        def on_click_start(event):
            
            # Creates state, sets it up, and then shows it to the screen, also disables the buttons
            new_state = PlayState( word_list, choosable_word_list )
            new_state.setup()
            self.manager.disable()
            self.window.show_view( new_state )
            
        # Button exits the game
        @quit_button.event("on_click")
        def on_click_quit(event):
            arcade.exit()
    
    def setup( self ):
        
        # Allows mouse to be visible on screen
        self.window.set_mouse_visible(True)
        
        # Assigns the background png
        self.background = arcade.load_texture("resources/end_screen.png")
        
    def on_draw( self ):
                
        # Draws the background to the screen
        arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        
        # Draws the word to the screen
        arcade.draw_text( self.word, 300, 573, arcade.color.WHITE, font_size=50, anchor_x="center" )
        
        #Draws the guess count to the screen
        arcade.draw_text( str(self.guess_count), 300, 450, arcade.color.WHITE, font_size=25, anchor_x="center" )
        
        #Draws the buttons onto the screen
        self.manager.draw()
        
class HelpState ( arcade.View ):
    
    def __init__( self, play_state ):
        super().__init__()
        
        self.play_state = play_state
        
        # UIManager to handle the UI.
        self.manager = arcade.gui.UIManager()
        self.manager.enable()
        
        self.background = None
        
        # Create a vertical BoxGroup to align buttons
        self.v_box = arcade.gui.UIBoxLayout()

        # Create buttons for the menu
        #------------------------------------------------------------------------------
        # Each button is a UITextureButton through the arcade library
        back_button = arcade.gui.UITextureButton(
            texture=arcade.load_texture('resources/buttons/back_button_unpressed.png'), 
            texture_pressed=arcade.load_texture('resources/buttons/back_button_pressed.png'),
            scale=0.8
        )
        
        # Buttons are then added to the v_box to be easily organized
        self.v_box.add(back_button.with_space_around(bottom=20))

        # Create a widget to hold the v_box widget, that will center the buttons
        self.manager.add( arcade.gui.UIAnchorWidget( anchor_x="center_x", anchor_y="center_y", child=self.v_box, align_y=-200) )

        # Use a decorator to handle on_click events
        @back_button.event("on_click")
        def on_click_start(event):
            self.manager.disable()
            self.window.show_view( self.play_state )
    
    def setup( self ):
        
        # Allows mouse to be visible on screen
        self.window.set_mouse_visible(True)
        
        # Assigns the background png
        self.background = arcade.load_texture("resources/help_screen.png")
        
    def on_draw( self ):
                
        # Draws the background to the screen
        arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
                
        #Draws the buttons onto the screen
        self.manager.draw()