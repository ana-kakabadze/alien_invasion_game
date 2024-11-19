import sys

import pygame

class AlienInvasion:
    """Overall class to manage game assets and behavior."""
    
    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))      # This object is called a surface.
        pygame.display.set_caption("Alien Invasion")
    
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            # Make the most recently drawn screen visible.
            pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()


"""
The if __name__ == '__main__': 
statement in Python is a common pattern used to ensure that 
certain code only runs when a script is executed directly, 
rather than when it is imported as a module. 

Every Python module (file) has a special built-in variable called __name__ .
When a Python file is executed directly, Python sets __name__ to the string '__main__'.
When a Python file is imported as a module into another script,
__name__ is set to the name of the module (the filename without the .py extension).

The if statement checks if the current script's __name__ is equal to '__main__'.
If it is, Python runs the indented block of code.
If it isn't (e.g., because the file was imported as a module), Python skips the block.
"""
