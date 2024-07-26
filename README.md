# Digital Clock

This is a simple digital clock application built using Python's `tkinter` library. The clock displays the current time in a 12-hour format with seconds and changes the text color randomly every second.

## Features

- Displays the current time in a 12-hour format with AM/PM.
- Randomly changes the text color every second.
- Uses a custom font and size for the clock display.

## Prerequisites

- Python 3.x

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/digital-clock.git
    ```

2. Navigate to the project directory:

    ```bash
    cd digital-clock
    ```

## Usage

Run the script using Python:

```bash
python digital_clock.py
```

## Code Explanation

### Functions

- `update_time()`: Updates the label with the current time and a random color, then schedules itself to run again after 1 second.

- `get_random_color()`: Generates a random color in hexadecimal format.

- `Main Application`: Sets up the tkinter window, font, and label, then starts the update_time function and runs the tkinter main loop.

## Output

Check out the LinkedIn post showcasing the output of this code [here](https://www.linkedin.com/posts/aman-mogal_python-digital-connections-activity-7080837923046137857-_IB9?utm_source=share&utm_medium=member_desktop).
