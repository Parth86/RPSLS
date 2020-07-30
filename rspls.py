import random
score = {
    'player_score': 0,
    'computer_score': 0
}


def name_to_number(name):
    names = ['Rock', 'Spock', 'Paper', 'Lizard', 'Scissors']
    return names.index(name)


def number_to_name(number):
    names = ['Rock', 'Spock', 'Paper', 'Lizard', 'Scissors']
    return names[number]


def player_choice(choice):
    print(f'You chose {choice}!')
    return name_to_number(choice)


def computer_choice():
    number = random.randint(0, 4)
    print(f'Computer chose {number_to_name(number)}!')
    return number

def main():
    names = ['Rock', 'Spock', 'Paper', 'Lizard', 'Scissors']
    player_score = score['player_score']
    computer_score = score['computer_score']
    print()
    print(names)
    print(f'Your Score:{player_score}  Computer Score:{computer_score}')

    choice = input('Enter your choice: ').capitalize() # player choice Name
    if not choice in names:
        print('Invalid Name')
    else:
        player_number = player_choice(choice)
        computer_number = computer_choice()
        diff = (player_number - computer_number) % 5
        if diff in [1, 3]:
            player_score += 1
            score['player_score'] += 1
            print('You Won!')
        elif diff in [2, 4]:
            computer_score += 1
            score['computer_score'] += 1
            print('Computer Won!')
        else:
            print('Tie!')
    main()

if __name__ == "__main__":
    main()





