
def run_gift_sim(input_filename):

    input_file = open(input_filename, "r")

    # first line only contains a number 
    line_from_input_file = input_file.readline()
    num_people = int(line_from_input_file)

    names_of_people = []
    for people_idx in range(num_people):
        names_of_people.append(input_file.readline().strip())

    print(f"{num_people} people are gifting.  Their names are:")
    print(names_of_people)

    # now red until end of file    
    print("\nNow reading remainder of file")
    for line_from_input_file in input_file:
        print(line_from_input_file.strip())

if __name__ == '__main__':
    run_gift_sim("section1_2/gift1.in")
