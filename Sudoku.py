"""Runtime: 233 ms, faster than 5.28% of Python3 online submissions for Valid Sudoku.
Memory Usage: 13.8 MB, less than 99.18% of Python3 online submissions for Valid Sudoku."""
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:

        box_numbers = [[],[],[],[],[],[],[],[],[]]
        col_numbers = []
        is_soduku = True

        for index, row_list in enumerate(board):
            is_soduku = self.checkIfNotDuplicate(self,row_list)
            if not is_soduku:
                return False
            for index_list, value_box in enumerate(row_list):
                col_numbers.append(board[index_list][index])
                if len(col_numbers) == 9:
                        is_soduku = self.checkIfNotDuplicate(self,col_numbers)
                        if not is_soduku:
                            return False
                        col_numbers = []

                if index < 3:
                    if index_list < 3:
                        box_numbers[0].append(value_box)
                    elif index_list < 6:
                        box_numbers[1].append(value_box)
                    elif index_list < 9:
                        box_numbers[2].append(value_box)
                elif index < 6:
                    if index_list < 3:
                        box_numbers[3].append(value_box)
                    elif index_list < 6:
                        box_numbers[4].append(value_box)
                    elif index_list < 9:
                        box_numbers[5].append(value_box)
                elif index < 9:
                    if index_list < 3:
                        box_numbers[6].append(value_box)
                    elif index_list < 6:
                        box_numbers[7].append(value_box)
                    elif index_list < 9:
                        box_numbers[8].append(value_box)
                
        for each_box in box_numbers:
            is_soduku = self.checkIfNotDuplicate(self,each_box)
            if not is_soduku:
                return False
        return True



    def checkIfNotDuplicate(self, list_numbers: list[str]):
        list_numbers = [x for x in list_numbers if "." not in x]
        remove_list = list(Counter(list_numbers).values())
        
        while len(remove_list) > 0:
            if remove_list[0] == 1:
                remove_list.pop(0)
            else:
                return False
        
        return True


su_board =  [
[".",".",".",".","5",".",".","1","."],
[".","4",".","3",".",".",".",".","."],
[".",".",".",".",".","3",".",".","1"],
["8",".",".",".",".",".",".","2","."],
[".",".","2",".","7",".",".",".","."],
[".","1","5",".",".",".",".",".","."],
[".",".",".",".",".","2",".",".","."],
[".","2",".","9",".",".",".",".","."],
[".",".","4",".",".",".",".",".","."]]

print(Solution.isValidSudoku(Solution,su_board))