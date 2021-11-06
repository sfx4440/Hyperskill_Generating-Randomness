import random


def triad_counter(str_variable):
    triad_dict = {'000': [0, 0], '001': [0, 0], '010': [0, 0], '011': [0, 0], '100': [0, 0], '101': [0, 0],
                  '110': [0, 0], '111': [0, 0]}
    for i in range(3, len(str_variable)):
        if str_variable[i] == '0':
            triad_dict[str(str_variable[(i - 3):i])][0] += 1
        elif str_variable[i] == '1':
            triad_dict[str(str_variable[(i - 3):i])][1] += 1
    return triad_dict

def scrubber(str):
    clean_str = ''
    for i in range(len(str)):
        if str[i] in '01':
            clean_str = clean_str + str[i]
    return clean_str


def string_looper():
    str_var = input('Print a random string containing 0 or 1:\n')
    str_var = scrubber(str_var)
    while len(str_var) < 100:
        print(f'Current data length is {len(str_var)}, {100-len(str_var)} symbols left')
        inp_str = input('Print a random string containing 0 or 1:\n')
        new_var = scrubber(inp_str)
        str_var = str_var + new_var
    print(f'Final data string:\n{str_var}\n')
    return triad_counter(str_var)


def string_test(string):
    clean_str = ''
    for i in range(len(string)):
        if string[i] in '01':
            clean_str = clean_str + string[i]
    if string == clean_str:
        return True
    else:
        return False


def gameloop(bank, string, prediction):
    player_bank = bank
    test = string
    a = prediction
    if string == 'enough':
        print('Game over!')
        exit()
    else:
        if string_test(test):
            prediction = ''
            for i in range(3):
                prediction += str(random.randint(0, 1))
            for i in range(len(test))[3:]:
                if a[str(test[(i - 3):i])][0] > a[str(test[(i - 3):i])][1]:
                    prediction = prediction + str(0)
                else:
                    prediction = prediction + str(1)
            print(f'prediction:\n{prediction}')
            count_correct = 0
            count_wrong = 0
            for i in range(3, len(test)):
                if test[i] == prediction[i]:
                    count_correct += 1
                else:
                    count_wrong +=1
            pct_correct = round((count_correct / (len(test) - 3)), 4)
            player_bank += count_wrong
            player_bank -= count_correct
            print(f'Computer guessed right {count_correct} out of {len(test) - 3} symbols ({pct_correct * 100}%)')
            print(f'Your balance is now ${player_bank}')
            test = (input('Print a random string containing 0 or 1:\n'))
            gameloop(player_bank, test, a)
        else:
            gameloop(bank, input('Print a random string containing 0 or 1:\n'), a)


def game():
    player_bank = 1000
    a = string_looper()
    print("""You have $1000. Every time the system successfully predicts your next press, you lose $1. 
Otherwise, you earn $1. Print "enough" to leave the game. Let's go!\n""")
    test = (input('Print a random string containing 0 or 1:\n'))
    gameloop(player_bank, test, a)


game()
