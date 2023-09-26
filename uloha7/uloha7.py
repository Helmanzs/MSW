import random


def roll_3d6():
    return sum(random.randint(1, 6) for _ in range(3))


def monte_carlo_probability(num_simulations) -> tuple[int, int]:
    player1_wins = 0
    tie = 0

    for _ in range(num_simulations):
        player1_sum = roll_3d6()
        other_player_sum = roll_3d6()

        if player1_sum > other_player_sum:
            player1_wins += 1
        if player1_sum == other_player_sum:
            tie += 1

    probability = player1_wins / num_simulations
    tie_probability = tie / num_simulations
    return probability, tie_probability


num_simulations = 10000

probability = monte_carlo_probability(num_simulations)
print(f"Probability of Player 1 having a higher 3d6 throw: {probability[0]*100:.4f}%")
print(f"Probability of tie: {probability[1]*100:.4f}%\n")
