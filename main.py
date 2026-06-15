def main():
    import pygame
    from constants import SCREEN_WIDTH, SCREEN_HEIGHT
    from logger import log_state
    from player import Player
    from circleshape import CircleShape
    

    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    
    
    pygame.init()

    # restricting FPS to 60
    clock = pygame.time.Clock()
    dt = 0.0

    # setting screen size 
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # create player object
    player = Player(x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2)
    # main gameplay loop
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        dt = clock.tick(60)/1000
        
        screen.fill("black")
        player.draw(screen)
        player.update(dt)
        pygame.display.flip()


if __name__ == "__main__":
    main()
