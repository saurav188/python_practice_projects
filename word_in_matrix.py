def word_search(matrix, word):
    word_size=len(word)
    no_of_rows=len(matrix)
    no_of_columns=len(matrix[0])
    row_no=0
    column_no=0
    while row_no<=no_of_rows-1 and no_of_rows-row_no>=word_size:
        row=matrix[row_no]
        for i in range(no_of_columns):
            if word[0]==row[i]:
                found=True
                word_letter=0
                for j in range(row_no,word_size):
                    if word[word_letter]!=matrix[j][i]:
                        found=False
                    word_letter+=1
                if found:
                    return True
        row_no+=1
    
    while column_no<=no_of_columns and no_of_columns-column_no>=word_size:
        for i in range(no_of_rows):
            if word[0]==matrix[i][column_no]:
                found= True
                word_letter=0
                for j in range(column_no,word_size):
                    if word[word_letter]!=matrix[i][j]:
                        found=False
                    word_letter+=1
                if found:
                    return True
        column_no+=1
    return False

  
matrix = [
  ['F', 'A', 'C', 'I'],
  ['O', 'B', 'Q', 'P'],
  ['A', 'N', 'O', 'B'],
  ['M', 'A', 'S', 'S']]
print(word_search(matrix, 'FOAm'))
# True