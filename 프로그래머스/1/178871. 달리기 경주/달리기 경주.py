def solution(players, callings):
    
    player2rank = {player:i for i,player in enumerate(players)}
    rank2player = {i:player for player,i in player2rank.items()}
    
    for call in callings:
        rank = player2rank[call]
        before_player = rank2player[rank-1]
        rank2player[rank-1] = call
        rank2player[rank] = before_player
        player2rank[call] = rank-1
        player2rank[before_player] = rank
        
    answer= [player for player in rank2player.values()]
    
    return answer