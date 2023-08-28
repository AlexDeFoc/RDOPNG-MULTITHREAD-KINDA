# Image Processing Script Guide

## Prerequisites

Before you begin, ensure you have Python installed on your system.

## Getting Started

1. **Install Python:**
   Make sure you have Python installed on your system. You can download it from the official [Python website](https://www.python.org/downloads/).

2. **Place All PNGs:**
   Put all your PNG files into the "main directory" (the directory where the script is located).

3. **Ensure `rdopng.exe`:**
   Make sure that the `rdopng.exe` file is located in the same directory.

## What Happens?

When you follow these steps:

- Separate folders will be created for each PNG file.
- A copy of `rdopng.exe` will be placed in each of these folders.
- The effect of the `.exe` will be applied individually to every file within their respective folders (Recommended: Parallel Mode).

## How Modes Work

1. **Iteration Mode:**
   In this mode, the chosen preset command will be applied to each PNG found in its matching folder, using the `.exe` located in the same folder. This happens in a sequential manner, one by one.

2. **Parallel Mode:**
   Similar to Iteration Mode, but in Parallel Mode, the actions are performed simultaneously for all PNGs. Be cautious: this mode creates a separate process for each `.exe`, potentially using 100% of your CPU. This approach could speed up processing but might lead to increased CPU usage and temperature. (I prefer Parallel Mode.)

**Note:** Ensure that the PNG file names do not contain symbols such as dots or other special characters, as these might cause issues. While I tested with dots and it broke the process, you can experiment at your own risk.

## Time Reduction using Parallel Mode

Using Parallel Mode offers significant time reductions:

- For 2 photos: approximately 55.56% reduction in processing time (18 seconds in Iteration Mode vs. 8 seconds in Parallel Mode, tested on the fast preset).
- For over 10 photos: approximately 82.25% reduction in processing time (1 minute 17 seconds in Iteration Mode vs. 17 seconds in Parallel Mode, tested on the fast preset).

## How the Script Works

The script operates in phases:

1. **Composition Phase:**
   - The script scans the main directory for PNG files.
   - If PNG files are found, the script creates separate folders for each PNG and copies the `rdopng.exe` to each folder.
   - The script then proceeds to the Pre-Process Phase.

2. **Pre-Process Phase:**
   - In this phase, the script prompts the user to choose the processing mode (Iteration or Parallel) and set the desired preset/command.

3. **Process Phase:**
   - The script applies the chosen preset commands to each PNG in their respective folders using the `.exe` files.
   - The script performs this action either sequentially (Iteration Mode) or simultaneously (Parallel Mode).

4. **Post-Process Phase:**
   - After processing, the script creates a `TIMER.txt` file that contains information about the chosen mode, preset/command, and time elapsed.

## Reruns and Further Processing

To process more photos or redo the processing:

1. Delete CHECKER (optionally timer or leave it as it will be rewritten).
2. Move out the PNGs from their respective folders (if you want to redo the same PNGs) and then delete the folders.
   - If you want to process other PNGs while keeping the processed ones, move these folders out of the main directory and run the script again.

**Note:** The output files generated by the `.exe` are inside the original PNG's folder and have names in the format: `<original_name>_rdo.png`. For example, if the original file is `1.png`, the output file will be `1_rdo.png`.

## Suggestions and Contributions

I welcome any suggestions, feedback, or contributions! If you have ideas for new commands, features, fixes, or improvements, feel free to reach out. The script is designed to be easy to modify, add, or remove commands due to its readable structure.

For suggestions that could become part of the default release, you can provide them via pull requests on the script's GitHub repository or by contacting me directly.

---

## A Personal Note

I'd like to share that I embarked on this project with minimal prior knowledge of Python; I was truly starting from scratch. Over the course of more than 16 hours, I worked diligently, learning as I went along. A huge shoutout goes to ChatGPT 3.5 for being an invaluable companion in guiding me through this process.

Throughout this journey, I was reminded of the phrase that encapsulates the spirit of many programmers: **"PLS FIX MY ENTIRE CODE, CHAT GPT!!!"** While I didn't ask for complete fixes, the guidance and insights I received from ChatGPT were immensely helpful in achieving my goals.

---

## Workaround and Limitations

This script provides a workaround for the limitations of having to apply changes to only one photo at a time and being restricted to single-thread processing. It leverages the power of parallel and iteration modes to enable efficient handling of tasks involving multiple images.

The script utilizes `rdopng.exe` developed by [Rich Geldreich](https://github.com/richgel999). You can find the original repository at [https://github.com/richgel999/rdopng](https://github.com/richgel999/rdopng).

If you encounter any issues or have questions, feel free to ask!

---

## Future Update Plans

In the near future, I have plans to introduce a significant enhancement to the script. I'm actively working on integrating oxipng optimization for the processed PNGs. This addition aims to further compress the PNG files while maintaining their quality. Keep an eye out for updates!

---

## Overview

In essence, I've developed a Python script that empowers you with the flexibility to utilize commands (presets) and modes, enabling you to efficiently perform a multitude of tasks simultaneously or one after another. 

This can be particularly helpful when handling a large number of photos, offering the choice between parallel processing for faster execution and iteration for a more controlled approach. 

Feel free to incorporate these functionalities into your workflow and make the most of your tasks!
