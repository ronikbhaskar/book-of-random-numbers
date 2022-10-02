"""
This file is used to format strings of random digits/characters.

Author: Ronik
"""

COL_WIDTH = 10
NUM_COLS = 6
ROW_HEIGHT = 2
FILE = "book-of-random-numbers/dice-rolls/090322.txt"

def get_block_size(col_width: int, num_cols: int, row_height:int) -> int:
    """
    col_width : int - number of chars left-to-right per columns
    num_cols : int - number of columns
    row_height : int - number of chars top-to-bottom per row

    Returns the size of the blocks of random numbers
     in terms of number of characters
    """

    assert col_width > 0 and num_cols > 0 and row_height > 0

    return col_width * num_cols * row_height

def padded_string(string, block_size):
    """
    string - string of random characters
    block_size : int - product of col width, num cols, and row height
    Returns: string padded with sufficient spaces to fill blocks evenly
    """

    pad_char = " "
    string_len = len(string)
    remainder = string_len % block_size
    padding = (block_size - remainder) * pad_char
    return string + padding

def format_random(title, string, col_width, num_cols, row_height):
    """
    string - string of random characters
    col_width : int - number of chars left-to-right per columns
    num_cols : int - number of columns
    row_height : int - number of chars top-to-bottom per row

    Returns: text for markdown table of these characters
    """

    block_size = get_block_size(col_width, num_cols, row_height)
    string = padded_string(string, block_size)
    res = "| " + title + " |\n|---|\n"

    while string != "":
        section = string[:block_size]
        res += "|"

        for line in range(row_height):
            res += "` " + section[:col_width]
            section = section[col_width:]

            for col in range(num_cols - 1):
                res += " " + section[:col_width]
                section = section[col_width:]

            res += " `<br>"
        res += "|\n"

        string = string[block_size:]

    return res

def main():
    with open(FILE, "r") as f:
        string = f.read()
    print(format_random("TITLE", string, COL_WIDTH, NUM_COLS, ROW_HEIGHT))

if __name__ == "__main__":
    main()





