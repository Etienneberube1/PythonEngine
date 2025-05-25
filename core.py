import pygame
import player

# Define the GameEngine class
class GameEngine:
    def __init__(self):
        
        # All your initialization code for the engine
        print("Initializing the game engine...")
        
        
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))
        self.clock = pygame.time.Clock()
        self.dt = 0
        self.running = True
        
        player.Init_player(self.screen)




    def main(self):
        # Main game loop

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # Fill the screen with a color to wipe away anything from last frame
            self.screen.fill("dimgrey")

            player.Input_Player(self.dt)
            player.Draw_Player(self.screen)

            # Flip the display to update the screen with the new content
            pygame.display.flip()

            # Limit FPS to 60
            self.dt = self.clock.tick(60) / 1000

        pygame.quit()  # Quit pygame when the game ends


# Automatically start the game when the script is executed
if __name__ == "__main__":
    game = GameEngine()  # This automatically calls __init__()
    game.main()  # Then we call the start method for the game loop
