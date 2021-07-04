def solution(places):
    answer = []
    def is_safe(x, y, place):
        if (not (x-1 < 0)) and place[x-1][y] == 'P' : return False
        if (not (y-1 < 0)) and place[x][y-1] == 'P' : return False
        if (not (x+1 > 4)) and place[x+1][y] == 'P' : return False
        if (not (y+1 > 4)) and place[x][y+1] == 'P' : return False

        if ((not (x-1 < 0 or y+1 > 4)) and place[x-1][y+1] == 'P') and (place[x-1][y] == 'O' or place[x][y+1] == 'O'):
            return False
        if ((not (x-1 < 0 or y-1 < 0)) and place[x-1][y-1] == 'P') and (place[x-1][y] == 'O' or place[x][y-1] == 'O'):
            return False
        if ((not (x+1 > 4 or y-1 < 0)) and place[x+1][y-1] == 'P') and (place[x][y-1] == 'O' or place[x+1][y] == 'O'):
            return False
        if ((not (x+1 > 0 or y+1 > 4)) and place[x+1][y+1] == 'P') and (place[x+1][y] == 'O' or place[x][y+1] == 'O'):
            return False

        if (not y-2 < 0 and place[x][y-2] == 'P') and (not y-1 < 0 and place[x][y-1] == 'O') : 
            return False
        if (not x-2 < 0 and place[x-2][y] == 'P') and (not x-1 < 0 and place[x-1][y] == 'O') : 
            return False
        if (not x+2 > 4 and place[x+2][y] == 'P') and (not x+1 > 4 and place[x+1][y] == 'O') : 
            return False
        if (not y+2 > 4 and place[x][y+2] == 'P') and (not y+1 > 4 and place[x][y+1] == 'O') : 
            return False
        
        return True

    for place in places:
        is_ok = True
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    if not is_safe(i, j, place):
                        is_ok = False
        if is_ok:
            answer.append(1)
        else:
            answer.append(0)

    return answer