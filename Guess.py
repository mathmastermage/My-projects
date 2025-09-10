import random

word_bank = ['rizz', 'ohio', 'sigma', 'tiktok', 'skibidi', 'paper', 'book']
word = random.choice(word_bank)

guessWord = ['_'] * len(word)
attempts = 10

while attempts > 0:
    print('\nCurrent word: ' + ' '.join(guessWord))
    guess = input('Guess a letter: ').lower()

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessWord[i] = guess
        print('Great guess!')
    else:
        attempts -= 1
        print('Wrong guess! Attempts left: ' + str(attempts))

    if '_' not in guessWord:
        print('\nCongratulations!! You guessed the word: ' + word)
        break
if attempts == 0 and '_' in guessWord:
    print('\nYou\'ve run out of attempts! The word was: ' + word)
