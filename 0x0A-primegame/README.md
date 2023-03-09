Prime Number Game
In this game, two players, Maria and Ben, take turns choosing prime numbers from a set of consecutive integers starting from 1 up to and including n. The chosen prime and its multiples are then removed from the set. The player who cannot make a move loses the game.

Given x rounds of the game, where n may be different for each round, determine who the winner of each game is. Assuming Maria always goes first and both players play optimally.

Approach
To solve this problem, we can use the Sieve of Eratosthenes algorithm to generate a list of all primes up to the given value of n. Then, we can simulate the game by removing the chosen prime and its multiples from the list until there are no more primes left. We can keep track of whose turn it is by using a boolean variable, where True represents Maria's turn and False represents Ben's turn. We can also keep track of the number of remaining primes in the list.

To determine the optimal move, we can start with the largest remaining prime and work backwards until we find a prime that leaves no more primes in the list after it is removed. If no such prime exists, we can choose the largest remaining prime.

We can repeat this process until there are no more primes left in the list or until one of the players cannot make a move. If Maria cannot make a move, then Ben wins. If Ben cannot make a move, then Maria wins.

Functionality
The function isWinner(x, nums) takes two parameters:

x: an integer that represents the number of rounds to play
nums: a list of integers n that represents the value of n for each round
The function returns the name of the player that won the most rounds. If the winner cannot be determined, it returns None.

Code
Dive in to the code section and have a look.
