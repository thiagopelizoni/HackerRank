import random

# Constants for the Monopoly board
CC = [2, 17, 33]  # Community Chest positions
CH = [7, 22, 36]  # Chance positions
G2J = 30  # Go to Jail position
JAIL = 10  # Jail position
GO = 0  # GO position
C1 = 11  # C1 position
E3 = 24  # E3 position
H2 = 39  # H2 position
R = [5, 15, 25, 35]  # Railways positions
U = [12, 28]  # Utilities positions
BOARD_SIZE = 40

# Community Chest cards (2/16 cards send player to a new position)
CC_cards = ['GO', 'JAIL'] + [''] * 14

# Chance cards (10/16 cards send player to a new position)
CH_cards = ['GO', 'JAIL', 'C1', 'E3', 'H2', 'R1', 'next R', 'next R', 'next U', 'back 3'] + [''] * 6

# Function to move to the next railway station
def next_r(position):
    while position not in R:
        position = (position + 1) % BOARD_SIZE
    return position

# Function to move to the next utility company
def next_u(position):
    while position not in U:
        position = (position + 1) % BOARD_SIZE
    return position

# Simulate a move on the board
def simulate_move(position, dice):
    position = (position + dice) % BOARD_SIZE
    if position in CC:  # Draw Community Chest card
        card = random.choice(CC_cards)
        if card == 'GO':
            position = GO
        elif card == 'JAIL':
            position = JAIL
    elif position in CH:  # Draw Chance card
        card = random.choice(CH_cards)
        if card == 'GO':
            position = GO
        elif card == 'JAIL':
            position = JAIL
        elif card == 'C1':
            position = C1
        elif card == 'E3':
            position = E3
        elif card == 'H2':
            position = H2
        elif card == 'R1':
            position = R[0]
        elif card == 'next R':
            position = next_r(position)
        elif card == 'next U':
            position = next_u(position)
        elif card == 'back 3':
            position = (position - 3) % BOARD_SIZE
    elif position == G2J:  # Go to Jail
        position = JAIL
    return position

# Initialize variables
position_counts = [0] * BOARD_SIZE
position = GO  # Start at GO
rolls = 1000000  # Number of rolls to simulate
N, K = map(int, input().split())

# Simulate rolls
for _ in range(rolls):
    dice = random.randint(1, N) + random.randint(1, N)
    position = simulate_move(position, dice)
    position_counts[position] += 1

# Calculate the most popular squares
most_popular_squares = sorted(range(BOARD_SIZE), key=lambda x: position_counts[x], reverse=True)[:K]

# Convert the most popular squares to their board representations
square_names = ['GO', 'A1', 'CC1', 'A2', 'T1', 'R1', 'B1', 'CH1', 'B2', 'B3',
                'JAIL', 'C1', 'U1', 'C2', 'C3', 'R2', 'D1', 'CC2', 'D2', 'D3',
                'FP', 'E1', 'CH2', 'E2', 'E3', 'R3', 'F1', 'F2', 'U2', 'F3',
                'G2J', 'G1', 'G2', 'CC3', 'G3', 'R4', 'CH3', 'H1', 'T2', 'H2']
answer = [square_names[i] for i in most_popular_squares]

print(" ".join(answer))
