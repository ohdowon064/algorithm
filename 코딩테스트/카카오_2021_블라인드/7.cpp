#include <string>
#include <vector>
#include <cstring>

using namespace std;

int cache[5][5][5][5][2];

int dp(vector<vector<int>> board, int x1, int y1, int x2, int y2, int turn){

    int xSize = board[0].size(), ySize = board.size();
    if(x1 > xSize || x2 > xSize || y1 > ySize || y2 > ySize)
        return 1;

    int ret = cache[x1][y1][x2][y2][turn];
    if(ret != -1)   return ret;

    if(turn == 0){ // A turn
        if(x1 < xSize) // right
            ret += dp(board, x1+1, y1, x2, y2, 0);
        if(x1 > 1) // left
            ret += dp(board, x1-1, y1, x2, y2, 0);
        if(y1 > 1) // down
            ret += dp(board, x1, y1+1, x2, y2, 0);
        if(y1 < ySize)  // up
            ret += dp(board, x1, y1-1, x2, y2, 0);
    }
    else if(turn == 0){ // B turn
        if(x2 < xSize) // right
            ret += dp(board, x1, y1, x2+1, y2, 1);
        if(x2 > 1) // left
            ret += dp(board, x1, y1, x2-1, y2, 1);
        if(y2 > 1) // down
            ret += dp(board, x1, y1, x2, y2+1, 1);
        if(y2 < ySize)  // up
            ret += dp(board, x1, y1, x2, y2-1, 1);
    }
    return ret;
}

int solution(vector<vector<int>> board, vector<int> aloc, vector<int> bloc) {
    memset(cache, -1 , sizeof(cache));
    return dp(board, aloc[0], aloc[1], bloc[0], bloc[1], 0);
}