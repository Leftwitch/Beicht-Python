hardcoded = [
    [1, 2], [1, 3], [1, 4], [1, 5],
    [2, 3], [2, 4], [2, 5],
    [3, 4], [3, 5],
    [4, 5]
]


def erstelleSpielkonstellationen(player_count):
    result = []
    for player_index in range(1, player_count+1):
        for opponent_index in range(player_index+1, player_count+1):
            result.append([player_index, opponent_index])
    return result


def erstelleSpielkonstellationen2(player_count):
    result = []
    current_player = 1
    current_player_index = 0
    while current_player_index + 1 < player_count:
        opponent_index = current_player % player_count

        # Wenn der Spieler bereits gespielt hat, dann nächsten Spieler, bzw von vorne anfangen
        if opponent_index == 0:
            current_player_index += 1

        # Wenn wir nicht selbst der Spieler sind, dann Spielkonstellation hinzufügen
        if current_player_index != opponent_index and opponent_index > current_player_index:
            result.append([current_player_index+1, opponent_index+1])

        # Zähler für den nächsten Spieler erhöhen
        current_player += 1

    return result


print(erstelleSpielkonstellationen(5))
print(erstelleSpielkonstellationen(5) == hardcoded)


print(erstelleSpielkonstellationen2(5))
print(erstelleSpielkonstellationen2(5) == hardcoded)
