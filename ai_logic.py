def ai_logic(cells, player, enemy):
    if cells[5] == " ":
        return 5

    combinations = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
    for combo in combinations:
        # Atack
        if cells[combo[0]] == player and cells[combo[1]] == player and cells[combo[2]] == " ":
            return combo[2]
        if cells[combo[0]] == player and cells[combo[1]] == " " and cells[combo[2]] == player:
            return combo[1]
        if cells[combo[0]] == " " and cells[combo[1]] == player and cells[combo[2]] == player:
            return combo[0]

        # Defense
        if cells[combo[0]] == enemy and cells[combo[1]] == enemy and cells[combo[2]] == " ":
            return combo[2]
        if cells[combo[0]] == enemy and cells[combo[1]] == " " and cells[combo[2]] == enemy:
            return combo[1]
        if cells[combo[0]] == " " and cells[combo[1]] == enemy and cells[combo[2]] == enemy:
            return combo[0]

    for i in range(1,10):
        if cells[i] == " ":
            return i
