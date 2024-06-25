
# list of actions
ACTION_READ_GIFTER = 1
ACTION_READ_AMOUNT = 2
ACTION_READ_RECIPIENT = 3


def run_gift_sim(input_filename):

    input_file = open(input_filename, "r")

    # first line only contains a number 
    line_from_input_file = input_file.readline()
    num_people = int(line_from_input_file)

    names_of_people = []
    balances = []
    for people_idx in range(num_people):
        entry = {"name" : "", "balance" : 0}
        entry["name"] = input_file.readline().strip()
        balances.append(entry)

    print(f"{num_people} people are gifting.  Their starting balances are:")
    print(balances)

    next_action = ACTION_READ_GIFTER

    # now red until end of file    
    print("\nNow reading remainder of file")
    for line_from_input_file in input_file:
        print(line_from_input_file.strip())
        if(next_action == ACTION_READ_GIFTER):
            # read the giver
            giver = line_from_input_file.strip()
            next_action = ACTION_READ_AMOUNT
        elif(next_action == ACTION_READ_AMOUNT):
            # read the amount of money and number of people
            values = line_from_input_file.strip().split(" ")
            #print(values[0])
            gross_gift_amount = int(values[0])
            num_of_recipients = int(values[1])
            remainder = gross_gift_amount%num_of_recipients
            gift_to_recipients = int(gross_gift_amount/num_of_recipients)
            print(gift_to_recipients)
            next_action = ACTION_READ_RECIPIENT
        elif(next_action == ACTION_READ_RECIPIENT):
            # read the recipients 
            recipients = line_from_input_file.strip().split("")
            next_action = ACTION_READ_GIFTER

if __name__ == '__main__':
    run_gift_sim("section1_2/gift1.in")
