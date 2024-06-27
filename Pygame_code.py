import pygame
# Initializes all the Pygame modules
pygame.init()     

# Define the dimensions of the window

width = 500
height = 500
# Creates a window of size 500x500 pixels.
win = pygame.display.set_mode((width, height)) 
pygame.display.set_caption("Client")

class Player():
    # The constructor initializes the player's position, size, color, and speed (val).
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x, y, width, height)
        self.val = 3
        
    def draw(self, win):
        # Draws the player (a rectangle) on the window.
        pygame.draw.rect(win, self.color, self.rect)
        
    def move(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_LEFT]:
            self.x -= self.val
            
        if keys[pygame.K_RIGHT]:
            self.x += self.val
            
        if keys[pygame.K_UP]:
            self.y -= self.val
            
        if keys[pygame.K_DOWN]:
            self.y += self.val
        
        self.rect = (self.x, self.y, self.width, self.height)

# Fills the window with a white background and then draws the player. Finally, it updates the display.
def redrawWindow(win, player):
    win.fill((255, 255, 255))
    player.draw(win)
    pygame.display.update()


def main():
    run = True
    p = Player(50, 50, 100, 100, (0, 255, 0))
    # Creates a clock object to control the frame rate.
    clock = pygame.time.Clock()
    
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
    
        p.move()            
        redrawWindow(win, p)
        
main()
# If the QUIT event is detected (e.g., the user closes the window), run is set to False and pygame.quit() is called to exit the program.
