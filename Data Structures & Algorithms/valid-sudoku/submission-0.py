class Solution:
    @staticmethod
    def has_duplicates(cells: List[str]) -> bool:
        filled = [x for x in cells if x != '.']
        return len(filled) != len(set(filled))
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            if self.has_duplicates(row):
                return False 
            
        for col_idx in range(9):
            column = [board[row_idx][col_idx] for row_idx in range(9)]
            if self.has_duplicates(column):
                return False 
            
        for br in range(0, 9, 3):
            for bc in range(0, 9, 3):
                square = [board[br + dr][bc + dc] for dr in range(3) for dc in range(3)]
                if self.has_duplicates(square):
                    return False

        return True 

        
        


