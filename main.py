def main():
    import pygame
    from asteroidfield import AsteroidField
    from constants import SCREEN_WIDTH, SCREEN_HEIGHT
    from logger import log_state
    from player import Player
    from circleshape import CircleShape
    from asteroid import Asteroid

    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    
    
    pygame.init()

    # restricting FPS to 60
    clock = pygame.time.Clock()
    dt = 0.0

    # setting screen size 
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # creating groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    
    # Give player class group memberships
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    
    player = Player(x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()

    # main gameplay loop
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        dt = clock.tick(60)/1000
        
        screen.fill("black")
        for thing in drawable:
            thing.draw(screen)
    
        updatable.update(dt)
        pygame.display.flip()


if __name__ == "__main__":
    main()
