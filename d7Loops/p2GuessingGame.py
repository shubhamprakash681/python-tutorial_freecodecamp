secret_word = 'Shubham'
guess = ''

guess_count = 0
limit = 3

while (guess != secret_word) and (guess_count < limit):
    guess = input('Enter Guess Word: ')
    guess_count += 1
    if guess == secret_word:
        break
    print('Wrong Guess,' + ' Guesses Left= ' + str(limit-guess_count))

if guess_count == limit:
    print('Correct Guess')
    print('You Loose!')
else:
    print('You Won!')
