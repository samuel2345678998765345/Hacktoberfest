import random

def hangman():
    words = ['python', 'java', 'ruby', 'javascript', 'php', 'html', 'css', 'swift']
    word = random.choice(words)
    guessed = '_' * len(word)
    tries = 6
    letters_tried = ''

    print('Welcome to Hangman!')
    print('Try to guess the word in fewer than 6 attempts.')

    while tries > 0 and guessed != word:
        print(f'You have {tries} tries left.')
        print(f'Word to guess: {guessed}')
        print(f'Letters tried: {letters_tried}')

        guess = input('Enter a letter or the full word: ').lower()

        if len(guess) == 1 and guess.isalpha():
            if guess in letters_tried:
                print(f'You already tried {guess}')
            elif guess not in word:
                print(f'{guess} is not in the word.')
                tries -= 1
                letters_tried += guess
            else:
                print(f'Good job, {guess} is in the word!')
                letters_tried += guess
                word_list = list(guessed)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_list[index] = guess
                guessed = ''.join(word_list)
        elif len(guess) == len(word) and guess.isalpha():
            if guess == word:
                guessed = word
            else:
                print(f'{guess} is not the word.')
                tries -= 1
        else:
            print('Not a valid guess.')

        print()

    if guessed == word:
        print(f'Congratulations! You guessed the word {word}!')
    else:
        print(f'Sorry, you ran out of tries. The word was {word}.')

if __name__ == '__main__':
    hangman()
