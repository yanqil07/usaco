

def convert_ascii_letter_to_number(character):
    print(f"converting {character} to a number")
    if ( (character >= "A") and (character <= "Z") ):
        return ord(character) - ord("A")

    else:
        return ord(character) - ord("a")


def run_your_ride_sim():
    comet_name = input("Enter the comet's name:")
    group_name = input("Enter the group's name:")

    print(f"Running calculation to see if group {group_name} will be able to go based on comet {comet_name}\n")

    current_character_value_comet = 1
    new_character_value_comet = 1
    current_character_value_group = 1
    new_character_value_group = 1

    for character in comet_name:
        print(f"Character in comet name is {convert_ascii_letter_to_number(character)+1}")
        character_value = convert_ascii_letter_to_number(character)+1
        new_character_value_comet = character_value * current_character_value_comet
        current_character_value_comet = new_character_value_comet
    print("Comet name translated\n")


    for character in group_name:
        print(f"Character in group name is {convert_ascii_letter_to_number(character)+1}")
        character_value = convert_ascii_letter_to_number(character)+1
        new_character_value_group = character_value * current_character_value_group
        current_character_value_group = new_character_value_group
    print("Group name translated\n")

    comet_value = current_character_value_comet % 47
    group_value = current_character_value_group % 47
    print(f"Total comet value is {(current_character_value_comet)}")
    print(f"Comet value moded is {(comet_value)}")
    print(f"Total group value is {(current_character_value_group)}")
    print(f"Group value moded is {(group_value)}")

    if(comet_value==group_value):
        print("Go")
    else:
        print("Stay")


if __name__ == '__main__':
    run_your_ride_sim()

