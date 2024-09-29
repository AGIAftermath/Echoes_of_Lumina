# main.py
import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Echoes of Lumina")

# Clock for controlling frame rate
clock = pygame.time.Clock()
FPS = 60

# Load assets
player_img = pygame.image.load('assets/lumina.png').convert_alpha()
light_img = pygame.image.load('assets/light.png').convert_alpha()

# Player settings
player_pos = pygame.Vector2(WIDTH // 2, HEIGHT // 2)
player_speed = 5

def draw_player(pos):
    screen.blit(player_img, pos)

def main():
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Handle movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            player_pos.x -= player_speed
        if keys[pygame.K_d]:
            player_pos.x += player_speed
        if keys[pygame.K_w]:
            player_pos.y -= player_speed
        if keys[pygame.K_s]:
            player_pos.y += player_speed

        # Render
        screen.fill((10, 10, 30))  # Dark background to emphasize light

        # Draw light around the player
        light_rect = light_img.get_rect(center=player_pos)
        screen.blit(light_img, light_rect)

        # Draw player
        draw_player(player_pos)

        pygame.display.flip()

    pygame.quit()
    sys.exit()
if __name__ == "__main__":
    main()
# Add to main.py

def create_light_surface(radius, color=(255, 255, 200, 180)):
    light_surface = pygame.Surface((radius*2, radius*2), pygame.SRCALPHA)
    pygame.draw.circle(light_surface, color, (radius, radius), radius)
    return light_surface

# In the main loop, replace the light rendering section with:

# Create and blit light
light_radius = 150
light_surface = create_light_surface(light_radius)
light_rect = light_surface.get_rect(center=player_pos)
screen.blit(light_surface, light_rect, special_flags=pygame.BLEND_RGBA_ADD)

# Add obstacle class
class Obstacle:
    def __init__(self, rect):
        self.rect = pygame.Rect(rect)

    def draw(self, surface):
        pygame.draw.rect(surface, (50, 50, 50), self.rect)

# Initialize obstacles
obstacles = [
    Obstacle((300, 200, 200, 20)),
    Obstacle((150, 400, 500, 20)),
    Obstacle((100, 150, 20, 300)),
    Obstacle((680, 100, 20, 400)),
]

def draw_shadows(surface, light_pos, obstacles):
    for obstacle in obstacles:
        # Calculate shadow points (simplified)
        shadow_offset = pygame.Vector2(50, 50)
        shadow_rect = obstacle.rect.copy()
        shadow_rect.topleft += shadow_offset
        pygame.draw.rect(surface, (30, 30, 30, 150), shadow_rect)

def main():
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Handle movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            player_pos.x -= player_speed
        if keys[pygame.K_d]:
            player_pos.x += player_speed
        if keys[pygame.K_w]:
            player_pos.y -= player_speed
        if keys[pygame.K_s]:
            player_pos.y += player_speed

        # Render
        screen.fill((10, 10, 30))  # Dark background to emphasize light

        # Draw obstacles
        for obstacle in obstacles:
            obstacle.draw(screen)

        # Draw shadows
        draw_shadows(screen, player_pos, obstacles)

        # Create and blit light
        light_radius = 150
        light_surface = create_light_surface(light_radius)
        light_rect = light_surface.get_rect(center=player_pos)
        screen.blit(light_surface, light_rect, special_flags=pygame.BLEND_RGBA_ADD)

        # Draw player
        draw_player(player_pos)

        pygame.display.flip()

    pygame.quit()
    sys.exit()
