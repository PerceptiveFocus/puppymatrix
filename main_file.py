import curses
import time
import random

# Define ASCII art frames for the dog animation
frames = [
    """
 / \\__
 (    @\___
 /         O
/   (_____/
/_____/   U\033[0m
""",
    """
 / \\__
 (    @\___
 /         O
/   (_____/
/_____/    U\033[0m
""",
    """
 / \\__
 (    @\___
 /         O
/   (_____/
/_____/   \\\033[0m
""",
    """
 / \\__
 (    @\___
 /         O
/   (_____/
/_____/   /\033[0m
""",
    """
 / \\__
 (    @\___
 /         O
/   (_____/
/_____/    \\\033[0m
""",
    """
 / \\__
 (    @\___
 /         O
/   (_____/
/_____/   /\033[0m
""",
    """
 / \\__
 (    @\___
 /         O
/   (_____/
/_____/    \\\033[0m
""",
    """
 / \\__
 (    @\___
 /         O
/   (_____/
/_____/   \\\033[0m
""",
    """
 / \\__
 (    @\___
 /         O
/   (_____/
/_____/    \\\033[0m
""",
    """
 / \\__
 (    @\___
 /         O
/   (_____/
/_____/   U\033[0m
"""
]

# Define barking frames
barking_frames = ["Woof!", "Bark!", "Arf!", "Ruff!"]

def display_frame(stdscr, frame, bark_frame, color_pair):
    height, width = stdscr.getmaxyx()
    
    # Display dog ASCII art
    for j, line in enumerate(frame.split('\n')):
        stdscr.addstr(j, (width - len(line)) // 2, line)
    
    # Display barking frame with alternating colors
    bark_x = (width - len(bark_frame)) // 2
    bark_y = height - 2
    stdscr.addstr(bark_y, bark_x, bark_frame, curses.color_pair(color_pair))
    
    stdscr.refresh()

def main(stdscr):
    curses.curs_set(0)  # Hide cursor
    
    # Set colors for the barking frames
    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_CYAN, curses.COLOR_BLACK)
    
    stdscr.clear()
    stdscr.refresh()
    
   # Display dog animation with barking frames
    while True:
        for i in range(len(frames)):
            bark_index = i % len(barking_frames)
            bark_frame = barking_frames[bark_index]
            color_pair = (bark_index % 4) + 1
            
            display_frame(stdscr, frames[i], bark_frame, color_pair)
            time.sleep(0.2)  # Adjust sleep time for animation speed
            stdscr.clear()
        
        # Randomly display a special frame
        if random.random() < 0.6:
            special_frame = """
ACCELERATE!!
"""
            display_frame(stdscr, special_frame, "Woof Woof!", 7)
            time.sleep(0.5)
            stdscr.clear()

if __name__ == "__main__":
    curses.wrapper(main)
