# Image Processing Script Guide

## Getting Started

1. **Place All PNGs:**
   Put all your PNG files into the "main directory" (the directory where the script is located).
   
2. **Ensure `rdopng.exe`:**
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

---

## Workaround and Limitations

This script provides a workaround for the limitations of having to apply changes to only one photo at a time and being restricted to single-thread processing. It leverages the power of parallel and iteration modes to enable efficient handling of tasks involving multiple images.

The script utilizes `rdopng.exe` developed by [Rich Geldreich](https://github.com/richgel999). You can find the original repository at [https://github.com/richgel999/rdopng](https://github.com/richgel999/rdopng).

---

## Overview

In essence, I've developed a Python script that empowers you with the flexibility to utilize commands (presets) and modes, enabling you to efficiently perform a multitude of tasks simultaneously or one after another. 

This can be particularly helpful when handling a large number of photos, offering the choice between parallel processing for faster execution and iteration for a more controlled approach. 

Feel free to incorporate these functionalities into your workflow and make the most of your tasks!
