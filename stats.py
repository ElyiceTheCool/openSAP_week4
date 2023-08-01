# Reads player files
with open("openSAP_rps\player1.txt", "r") as file1:
    player1_data = file1.readlines()
    
with open("openSAP_rps\player2.txt", "r") as file2:
    player2_data = file2.readlines()
    
# Compare both inputs and calculate wins
player1_wins = 0
player2_wins = 0
draws = 0

# TODO: Remove \n from each element
for line in range(len(player1_data)):
    if player1_data[line] == player2_data[line]:
        draws += 1
    elif player1_data[line] == '"R"\n' and player2_data[line] == '"S"\n':
        player1_wins += 1
    elif player1_data[line] == '"P"\n' and player2_data[line] == '"R"\n':
        player1_wins += 1
    elif player1_data[line] == '"S"\n' and player2_data[line] == '"P"\n':
        player1_wins += 1
    elif player1_data[line] == '"S"\n' and player2_data[line] == '"R"\n':
        player2_wins += 1
    elif player1_data[line] == '"R"\n' and player2_data[line] == '"P"\n':
        player2_wins += 1
    elif player1_data[line] == '"P"\n' and player2_data[line] == '"S"\n':
        player2_wins += 1
    
    else:
        break

total = draws + player1_wins + player2_wins
# print(total)

# Write results in result.txt file
file_path = "result.txt"
with open(f"openSAP_rps\{file_path}", "w") as file3:
    file3.write(f"Player1 wins: {player1_wins}\n")
    file3.write(f"Player2 wins: {player2_wins}\n")
    file3.write(f"Draws: {draws}")
    