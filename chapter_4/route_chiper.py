"""Decrypt a path through a Union Route Cipher.

Designed for whole-word transposition ciphers with variable rows and columns.
Assumes encryption began at either top or bottom of a column.
Key indicates the order to read columns and the direction to traverse.
Negative column numbers mean start at bottom and read up.
Positive column numbers mean start at top and read down.

Example below is for 4x4 matrix with key -1 2 -3 4.
Note "0" is not allowed.
Arrows show encryption route; for negative key values read UP.

  1   2   3   4
_________________
| ^ | | | ^ | | |
|_|_|_v_|_|_|_v_|
| ^ | | | ^ | | |
|_|_|_v_|_|_|_v_|
| ^ | | | ^ | | |
|_|_|_v_|_|_|_v_|
| ^ | | | ^ | | |
|_|_|_v_|_|_|_v_|
START        END

Required inputs - a text message, # of columns, # of rows, key string

Prints translated plaintext
"""
#===============================================================================
# USER INPUT:

# the string to be decrypted (type or paste between triple-quotes):
ciphertext = """16 12 8 4 0 1 5 9 13 17 18 14 10 6 2 3 7 11 15 19"""

# number of columns in the transposition matrix:
COLS = 4

# number of rows in the transposition matrix:
ROWS = 5

# key with spaces between numbers; negative to read UP column (ex = -1 2 -3 4)
key = """ -1 2 -3 4 """

# END OF USER INPUT - DO NOT EDIT BELOW THIS LINE!
#===============================================================================

# split elements into words, not letters
cipherlist = list(ciphertext.split())

translation_matrix = [None] * COLS
plaintext = ""
start = 0
stop = ROWS

# turn key_int into list of integers.
key_int = [int(i) for i in key.split()]

#turn columns into items in list of lists:
for k in key_int:
    if k < 0: # reading bottom-to-top of column
        col_items = cipherlist[start:stop]
    elif k > 0: # reading top-to-bottom of column
        col_items = list((reversed(cipherlist[start:stop])))
    translation_matrix[abs(k) - 1] = col_items
    start += ROWS
    stop += ROWS

print(f"\nciphertext = {ciphertext}")
print(f"\ntranslation matrix = {translation_matrix}")
print(f"\nkey length = {len(key_int)}")

# loop through nested lists popping off last item to new list:
for i in range(ROWS):
    for col_items in translation_matrix:
        word = str(col_items.pop())
        plaintext += word + " "





print(f"\nplaintext = {plaintext}")
