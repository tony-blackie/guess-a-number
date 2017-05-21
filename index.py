def fruit(reels, spins):
    reel0 = reels[0]
    reel1 = reels[1]
    reel2 = reels[2]
    
    twoOfAKind = False
    twoAndAWild = False
    threeOfAKind = False
    
    if (reel0[spins[0]] == reel1[spins[1]] == reel2[spins[2]]):
        threeOfAKind = True
    elif (((reel0[spins[0]] == reel1[spins[1]]) and reel2[spins[2]] == 'Wild') or ((reel1[spins[1]] == reel2[spins[2]]) and reel0[spins[0]] == 'Wild') or ((reel0[spins[0]] == reel2[spins[2]]) and reel1[spins[1]]  == 'Wild')):
        twoAndAWild = True
    elif (((reel0[spins[0]] == reel1[spins[1]]) and reel2[spins[2]] != 'Wild') or ((reel1[spins[1]] == reel2[spins[2]]) and reel0[spins[0]] != 'Wild') or ((reel0[spins[0]] == reel2[spins[2]]) and reel1[spins[1]]  != 'Wild')):
        twoOfAKind = True    
    
    winnerComboOf = ''
    
    if twoOfAKind or twoAndAWild:
        if reel0[spins[0]] == reel1[spins[1]]:
            winnerComboOf = reel0[spins[0]]
        if reel1[spins[1]] == reel2[spins[2]]:
            winnerComboOf = reel1[spins[1]]
        if reel2[spins[2]] == reel0[spins[0]]:
            winnerComboOf = reel0[spins[0]]
    elif threeOfAKind:
        winnerComboOf = reel0[spins[0]]
        
    result = 0
    
    if threeOfAKind:
        if winnerComboOf == 'Jack':
            result = 10
        elif winnerComboOf == 'Queen':
            result = 20
        elif winnerComboOf == 'King':
            result = 30
        elif winnerComboOf == 'Bar':
            result = 40
        elif winnerComboOf == 'Cherry':
            result = 50
        elif winnerComboOf == 'Seven':
            result = 60
        elif winnerComboOf == 'Shell':
            result = 70
        elif winnerComboOf == 'Bell':
            result = 80
        elif winnerComboOf == 'Star':
            result = 90
        elif winnerComboOf == 'Wild':
            result = 100
    
    if twoOfAKind:
        if winnerComboOf == 'Jack':
            result = 1
        elif winnerComboOf == 'Queen':
            result = 2
        elif winnerComboOf == 'King':
            result = 3
        elif winnerComboOf == 'Bar':
            result = 4
        elif winnerComboOf == 'Cherry':
            result = 5
        elif winnerComboOf == 'Seven':
            result = 6
        elif winnerComboOf == 'Shell':
            result = 7
        elif winnerComboOf == 'Bell':
            result = 8
        elif winnerComboOf == 'Star':
            result = 9
        elif winnerComboOf == 'Wild':
            result = 10
            
    if twoAndAWild:
        if winnerComboOf == 'Jack':
            result = 2
        elif winnerComboOf == 'Queen':
            result = 4
        elif winnerComboOf == 'King':
            result = 6
        elif winnerComboOf == 'Bar':
            result = 8
        elif winnerComboOf == 'Cherry':
            result = 10
        elif winnerComboOf == 'Seven':
            result = 12
        elif winnerComboOf == 'Shell':
            result = 14
        elif winnerComboOf == 'Bell':
            result = 16
        elif winnerComboOf == 'Star':
            result = 18
        elif winnerComboOf == 'Wild':
            result = None
            
    return result


    