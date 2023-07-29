Title: UTS Blind Help Python Project

Description:
This Python project is designed to provide assistance to visually impaired individuals. It allows users to convert text into Braille and provides a user-friendly interface for interaction.

Code Structure:
The code is structured into several sections:

1. Importing Required Modules:
   - The necessary modules, including `tkinter` for GUI, and `datetime` for time-related operations, are imported.

2. Braille Conversion Function:
   - The `text_to_braille()` function converts text input into Braille representation using a predefined dictionary.

3. Translate Text Function:
   - The `translate_text()` function retrieves the input text from the user interface and calls the `text_to_braille()` function to convert it into Braille. The result is displayed in the output label.

4. GUI Initialization:
   - The main Tkinter window is created with the necessary configurations, such as title, size, and background color.
   - Background and logo images are displayed using `tkinter.Label` widgets.
   - Labels and entry fields are created for input and output.
   - A button is created to trigger the translation process by calling the `translate_text()` function.

5. Time Display:
   - The `update_time()` function updates the time label with the current time every second.
   - A label is created to display the time.
   - The `update_time()` function is initially called to set the time display in motion.

6. From and To Input Fields:
   - Labels and entry fields are created for the "From" and "To" inputs.

7. Additional Details:
   - The project is attributed to "Vedant Singh" through the output label.

Execution:
- Run the script to launch the graphical user interface.
- Enter text in the "UTS NO" field to convert it to Braille using the "Translate" button.
- The Braille translation will be displayed below the "Braille" label.
- The current time will be displayed in the top-left corner of the window.
- The "From" and "To" fields can be used for additional inputs.

Dependencies:
- Ensure that the required image files, such as "back.png" and "1234.png", are located in the specified paths.
- Install the necessary modules, such as `tkinter`, `datetime`, `pyautogui`, and `pdf2image`, before running the code.

Author: Vedant Singh
