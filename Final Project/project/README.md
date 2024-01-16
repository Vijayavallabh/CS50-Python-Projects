# Mind Reading Machine
#### Video Demo: https://youtu.be/GMokftSWUjE
#### Description:

The Mind Reader game algorithm is built around the machine invented by Claude Shannon in 1953. He named it "A Mind Reading Machine". It predicts a player's next move based on his/her previous inputs.

You can read about the machine by clicking on the following link provided in the Activities section under the title A Mind Reader Machine - Claude E. Shannon

Note: The algorithm is quite complicated to understand and to create. For all practical purposes, you just need to know how to apply the algorithm. It is completely all right if you do not understand how to create this algorithm.

In this algorithm, the computer looks for certain patterns in the player inputs (Heads or Tails) and tries to remember them. Furthermore, it assumes that the player will follow these patterns the next time if the same situation arises.

The computer also contains an element of randomness. If an assumed pattern is not repeated at least twice by the player, the machine predicts Heads or Tails randomly.

The types of patterns remembered, involve the outcome of two successive plays, i.e., whether or not the player won on those plays and whether the player changed their choice between the plays and after the plays.

There are 8 possible situations and, for each situation, a player can do two things

Each situation corresponds to a different cell in the memory of a machine. Within a cell, two events are registered:

Whether the last time this situation arose, the player played the same or different.

Whether or not the behaviour indicated in the first point, was a repeat of the same behaviour in the preceding situation.

Consider the situation win, same and lose, i.e., the second situation out of the 8 possible situations.

Suppose that the last time the second situation occurred, the player played differently. So differently is recorded in the first part of the memory cell. If at the preceding juncture, the second situation arose and the player again played differently, the second part of the memory cell registers this as a repeat.

If this situation arises again, the machine will assume that this is a definite pattern in the player's behaviour and will play accordingly. If the player does not repeat, the machine makes prediction randomly. The memory cells are always kept up to date.


