"""
This file contains the functions to convert 
from dice rolls to base 10 or hex or coin flips.

Author: Ronik
"""

DATE = "090322"

def check_dice(dice_rolls):
    """
    check_dice - confirms that all dice rolls are indeed 1-6
    Returns: None
    """

    if any((roll not in "123456" for roll in dice_rolls)):
        raise ValueError("invalid dice rolls")

def dice_to_heximal(dice_rolls):
    """
    dice_to_heximal - converts dice rolls to base 6

    dice_rolls : str - string of dice rolls 1-6

    Returns: str
    """

    # throw error if invalid dice rolls
    check_dice(dice_rolls)

    return "".join((str(int(roll) - 1) for roll in dice_rolls))

def dice_to_int(dice_rolls):
    """
    dice_to_int - converts dice rolls to base 6, then to int

    dice_rolls : str - string of dice rolls 1-6

    Returns: int
    """

    base_6 = dice_to_heximal(dice_rolls)
    
    return int(base_6, 6)

def dice_to_dec(dice_rolls):
    """
    dice_to_dec - converts dice rolls to base 6, then to base 10
        must remove the first digit of the string because it is
        impossible for the first digit to be zero with this method

    dice_rolls : str - string of dice rolls 1-6

    Returns: str
    """

    dice_as_int = dice_to_int(dice_rolls)

    return str(dice_as_int)[1:]

def dice_to_hex(dice_rolls):
    """
    dice_to_hex - converts dice rolls to base 6, then to base 16
        must remove the first digit of the string because it is
        impossible for the first digit to be zero with this method

    dice_rolls : str - string of dice rolls 1-6

    Returns: str
    """

    dice_as_int = dice_to_int(dice_rolls)

    return hex(dice_as_int)[3:]

def dice_to_coin_flips(dice_rolls):
    """
    dice_to_coin_flips - converts dice rolls to base 6, then bin, then flips
        must remove the first flip of the string because it is
        impossible for the first flip to be tails with this method

    dice_rolls : str - string of dice rolls 1-6

    Returns: str
    """

    dice_as_int = dice_to_int(dice_rolls)

    base_2 = bin(dice_as_int)[3:]

    return "".join(("H" if int(bit) else "T" for bit in base_2))

def main():
    with open(f"../dice-rolls/{DATE}.txt", "r") as f:
        dice_rolls = f.read()
    
    with open(f"../dice-rolls/{DATE}-dec.txt", "w") as f:
        f.write(dice_to_dec(dice_rolls))

    with open(f"../dice-rolls/{DATE}-hex.txt", "w") as f:
        f.write(dice_to_hex(dice_rolls))

    with open(f"../dice-rolls/{DATE}-flips.txt", "w") as f:
        f.write(dice_to_coin_flips(dice_rolls))

if __name__ == "__main__":
    main()