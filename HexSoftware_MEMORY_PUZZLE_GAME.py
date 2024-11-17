import pygame
import random
import time
import os

# Suppress the output from pygame
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "1"
pygame.init()

# Game constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
CARD_WIDTH = 80
CARD_HEIGHT = 80
GRID_SIZE = 4  # 4x4 grid
FPS = 30

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Setup the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Memory Puzzle Game")

# Load font
font = pygame.font.SysFont('Arial', 24)

# Create the card deck
def generate_deck():
    """Generate a shuffled deck of pairs."""
    cards = list(range(1, (GRID_SIZE * GRID_SIZE) // 2 + 1)) * 2
    random.shuffle(cards)
    return cards

# Card class
class Card:
    def __init__(self, value, x, y):
        self.value = value
        self.x = x
        self.y = y
        self.is_flipped = False
        self.is_matched = False

    def draw(self, screen):
        """Draw the card to the screen."""
        if self.is_flipped or self.is_matched:
            pygame.draw.rect(screen, WHITE, (self.x, self.y, CARD_WIDTH, CARD_HEIGHT))
            pygame.draw.rect(screen, BLACK, (self.x, self.y, CARD_WIDTH, CARD_HEIGHT), 2)
            text = font.render(str(self.value), True, BLACK)
            text_rect = text.get_rect(center=(self.x + CARD_WIDTH // 2, self.y + CARD_HEIGHT // 2))
            screen.blit(text, text_rect)
        else:
            pygame.draw.rect(screen, BLUE, (self.x, self.y, CARD_WIDTH, CARD_HEIGHT))
            pygame.draw.rect(screen, BLACK, (self.x, self.y, CARD_WIDTH, CARD_HEIGHT), 2)

    def flip(self):
        """Flip the card."""
        self.is_flipped = True

    def unflip(self):
        """Unflip the card."""
        self.is_flipped = False

    def match(self):
        """Mark the card as matched."""
        self.is_matched = True


# Main game function
def game():
    clock = pygame.time.Clock()
    cards = []
    flipped_cards = []
    matched_pairs = 0

    # Generate cards and place them on the screen
    card_values = generate_deck()
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            x = col * (CARD_WIDTH + 10) + 50
            y = row * (CARD_HEIGHT + 10) + 50
            value = card_values.pop()
            card = Card(value, x, y)
            cards.append(card)

    game_over = False
    while not game_over:
        screen.fill(BLACK)

        # Check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.MOUSEBUTTONDOWN and len(flipped_cards) < 2:
                mx, my = event.pos
                for card in cards:
                    if card.x < mx < card.x + CARD_WIDTH and card.y < my < card.y + CARD_HEIGHT:
                        if not card.is_flipped and not card.is_matched:
                            card.flip()
                            flipped_cards.append(card)

        # Check for a match
        if len(flipped_cards) == 2:
            if flipped_cards[0].value == flipped_cards[1].value:
                flipped_cards[0].match()
                flipped_cards[1].match()
                matched_pairs += 1
            else:
                # If no match, unflip the cards
                pygame.time.wait(500)  # wait for a short time to show the cards
                flipped_cards[0].unflip()
                flipped_cards[1].unflip()
            flipped_cards = []

        # Draw the cards
        for card in cards:
            card.draw(screen)

        # Check for win
        if matched_pairs == (GRID_SIZE * GRID_SIZE) // 2:
            game_over_text = font.render("You Win!", True, GREEN)
            screen.blit(game_over_text, (SCREEN_WIDTH // 2 - 70, SCREEN_HEIGHT // 2))
            pygame.display.update()
            time.sleep(2)
            game_over = True

        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()


