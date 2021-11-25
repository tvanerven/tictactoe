# Introduction
This is a tic tac toe game built in Python. Nothing except standard libraries were used. It was built in roughly 6 hours.

# State of work after ~3 hours

- Board + rendering done.
- Storing moves per player in the right squares.
- Welcome mixin for more interactive experience
- Validation of moves and inputs.
- Detection of simple win condition (row)
- Score saving

Still todo:

- Support for more complex win conditions (column and diagonals)
- Replay functionality
- Rewards from file.
- Improvements on code structure
- Cleanup of previous navigation attempt.

# Considerations

- I feel that, first of all, a game should be interactive and fun. This is why I spent more time (and likely prioritized wrongly) on the WelcomeMixin. However, I do feel it adds in terms of value to the player - there is suddenly a reward when playing, and the program handles humanized inputs and outputs as well as various conditions. I do not regret building this.
- Validation (both of win conditions and inputs) is relatively hardcoded. I feel I could've made this more dynamic with more time, but that is not within scope of this assignment.
- I wanted to get out there and showcase familiarity with different libraries in Python rather than stick to one style. As a result, the code style may appear fragmented, but it's more of a showcase than production code.
- Ideally, I wanted to keep it simple in terms of libraries used.

# Pitfalls

- My first consideration was building in directional controls to navigate the board (up, down, left, right, and mark). This turned out to be a false trail - you suddenly have to track the selected square, sanitize direction based from there, and validate different inputs. This wasn't as easy as I expected it to be, but it did yield me the idea of using dictionaries for Squares.
- Second consideration was the validation. I attempted (first) to work with a dynamic sized board, but after noticing that my dynamic navigation didn't go anywhere fast, I passed up this idea. Code-wise, it's doable (and I have some idea on how to approach this), but simply would require more time.
- Last consideration was the inclusion of an extensive easter egg in the form of a text-based game, such as Zork. I know, massive pitfall and not conductive to finishing. I compromised here by simply embedding the Way of Mrs. Cosmopolite from Discword from sir Terry Pratchett's excellent _Thief of Time_. 

# Other thoughts/possible improvements

- Dynamic validation based on board size. It can be done more beautifully.
- Dynamic board size.
- Larger easter egg
- Grouping Square objects into Rows and Columns to handle victory checks more gracefully.
- Keyboard navigation across the board.
- Moving all strings into a mixin and get them from there. This would improve code readability, but would be obstructive when debugging.
