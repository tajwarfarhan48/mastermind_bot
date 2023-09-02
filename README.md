# Introduction

This is a game bot written in Python for beating Mastermind, a code-cracking game, using 6 moves or less using Donald Knuth's 5-Guess Algorithm.

# Rules of Mastermind

Mastermind is a two-player code-breaking game. One of the players is the code-maker. Their job is to create a code using 4 pegs, each of which can be one of 8 possible colors (the number of pegs and possible colors can vary based on the version of the game). The second player is the code-breaker. Their job is to crack the code in 10 moves or less wihtout seeing it. 

As mentioned before, the code-breaker has at most 10 guesses to crack the code. The game starts with the code-breaker making a guess about what the code might be. The code-maker must then give feedback about how accurate the breaker's guess is using pins. For each peg in the breaker's guess that matches the position AND the color of one of the maker's code pegs, the maker gives a BLACK pin to the breaker. For each peg in the guess that matches the color but NOT the position of one of the maker's code pegs, the maker gives a WHITE peg. 

Using the feedback from the maker, the breaker must deduce the maker's code. The breaker wins the game if they are able to make a guess which receives 4 BLACK pins from the maker (i.e., all the pegs in the guess are in the right position and have the right color) within 10 moves or less. Otherwise, the maker wins. 

# The Bot

The bot attempts to crack the code present in the variable 'solution' using an algorithm known as the Five-Guess algorithm by Donald Knuth. The algorithm follows the following steps:

1. Create a set S which contains all possible solutions (e.g., for the 4-peg version of the game, the scores are S = { 1111, 1112, ... 8887, 8888 } )
2. Start with a random guess from set S 
3. Get the score for the current guess. The score is defined as the number of black and white pins received for a particular guess.
4. If a perfect score is received (maximum number of black pins), the game is won, and the algorithm ends.
5. Remove all solutions from S that do not give the same score for the current guess as the current score (these scores are impossible). 
6. Now, we will choose the next guess using the minmax technique - i.e., the we will pick the guess whose worst-case scenario performance is the best. We will pick each possible valid guess from S. For that guess, we will scan all possible scores that a guess can receive, and select the worst-case score, which is the score that gives us the least information, or eliminates the least number of options. The number of options eliminated in the worst-case score for a guess is its worst-case kill count. We will pick the guess with the highest worst-case kill count to be our next guess.
7. Repeat Step 3.

# The Code

The code for the bot is in the file 'five_guesses.py'. The code can be modified to change the number of pegs from the default (4), but the number of possible colors cannot be changed. If you modify the number of pegs in the game, keep in mind that raising the number of pegs past 4 will significantly slow down the performance of the program. You can also change the maximum number of tries the bot has to crack your code

The first section of the files gives you instructions on how to safely change the solution that the bot has to crack. 

# Instructions

To use this program, follow these steps (for Unix users or Windows users with a Git Bash shell; for Powershell or CMD users, the command to move into the project directory might be different): 

```
git clone https://github.com/tajwarfarhan48/mastermind_bot.git 
cd mastermind_bot 
python3 five_guesses.py
```