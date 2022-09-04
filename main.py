# Author    : Hammam Mahfuzh Sujudi
# Occasion  : Monotaro Indonesia - Python Test - 2022/09/03


def four_up(num_of_pages, total_pages=1):
    remainder = num_of_pages % 4
    # Check if input is an int greater than 4 and is not a multiple of 4
    if num_of_pages > 4 and remainder > 0:
        # Using integer division
        total_pages += num_of_pages // 4
    elif num_of_pages > 4:
        total_pages += (num_of_pages // 4) - 1
    return total_pages


this_input = int(input())
if this_input > 1000 or this_input < 1:
    print(f"Invalid input.\nPlease rerun the file.")
else:
    print(four_up(this_input))
