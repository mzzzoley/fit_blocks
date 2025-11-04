## Intro

Fit blocks with different shapes on a board. Default setup is the wooden calendar which can be solved for each 
day of the year. The month and day squares will be the only ones not covered in output.
The pieces or blocks will be checked in every rotated and mirrored forms.

https://img-1.kwcdn.com/product/Fancyalgo/VirtualModelMatting/f71b2cd74e036fa628c83b2749f08d0d.jpg?imageView2/2/w/800/q/70/format/webp


## Installation

Download repository and use `poetry install`.

## Usage

Tool is not a packaged finished product. Get your hands dirty and check __main__.py to run default calendar game for a specific date.
To get every possible solution, run stats.py.

No proper testing was done, but the tool should be able to handle custom board and shapes with some limitations.
Limitations:
 - every row of custom board should have the same row length (e.g. [[0,0,0],[0,0]] is not allowed, should be defined as [[0,0,0],[0,0,1]])
 - place 1-s on the board where no piece should be placed
 - pieces should be defined in the smallest dimensions possible (e.g. [1,1,1] not [[1,1,1][0,0,0]])

To run custom setup check custom_example.py


## License

Completely free to use!