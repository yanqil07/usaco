

def convert_ascii_letter_to_number(character):
    print(f"converting {character} to a number")
    if ( (character >= "A") and (character <= "Z") ):
        return ord(character) - ord("A")

    else:
        return ord(character) - ord("a")

def run_your_ride_sim():
    # comet_name = input("Enter the comet's name:")
    # group_name = input("Enter the group's name:")
    comet_name = "TEST"
    group_name = "BACON"
    print(f"Running calculation to see if group {group_name} will be able to go based on comet {comet_name}\n")

    for character in comet_name:
        print(f"Character is {convert_ascii_letter_to_number(character)}")
        

if __name__ == '__main__':
    run_your_ride_sim()
