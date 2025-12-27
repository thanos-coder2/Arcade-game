IEK Pygame Arcade Project
Game Description (written in first person)

I created a 2D arcade game with a Pac-Man style using Python and the Pygame library.
In the game, the player moves inside a simple maze using the arrow keys and tries to avoid an enemy that chases them.
If the enemy touches the player, a GAME OVER message appears, and I can press SPACE to restart the game.

Technical Features I Used

Map Design:
I created the map as a list of strings and draw it using for loops so that the walls are displayed on the screen.

Object-Oriented Programming:
I implemented the Pacman and Enemy classes to manage the player and the enemy.
Each class stores the position, movement, and drawing of the character.

Movement and Collision:
The player moves with the arrow keys, and the enemy tries to reach the player.
When they occupy the same cell, the Game Over state is triggered.

User Input Handling:
I detect key presses for player movement and for restarting the game (SPACE).

Graphics and Sound:
The map and characters are drawn using simple shapes (# for walls, circles for the player, squares for the enemy) and background music plays throughout the game.

Game Over with Restart:
When the game ends, a message is displayed on the screen, and I can restart by pressing SPACE.

What I Learned

I learned how to organize code with classes, handle collisions, manage user input, and combine graphics and sound in a Python game.