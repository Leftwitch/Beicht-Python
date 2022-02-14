hardcoded = [[1, 2], [1, 3], [1, 4], [1, 5], [
    2, 3], [2, 4], [2, 5], [3, 4], [3, 5], [4, 5]]


def erstelleSpielkonstellationen(player_count):
    result = []
    for player_index in range(1, player_count+1):
        for opponent_index in range(player_index, player_count+1):
            if player_index != opponent_index:
                result.append([player_index, opponent_index])
    return result


def erstelleSpielkonstellationen2(player_count):
    result = []
    for player_index in range(1, player_count+1):
       # Calculate all possible opponents and append them to result
        result.extend([[player_index, opponent_index]
                      for opponent_index in range(player_index, player_count+1) if player_index != opponent_index])

    return result


print(erstelleSpielkonstellationen(5))
print(erstelleSpielkonstellationen(5) == hardcoded)


print(erstelleSpielkonstellationen2(5))
print(erstelleSpielkonstellationen2(5) == hardcoded)
