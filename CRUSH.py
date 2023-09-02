import os
import shutil
import subprocess
import time

# Helper function to execute a command
def run_command(command, cwd):
    subprocess.run(command, shell=True, cwd=cwd)

# Helper function to process PNG files in folders
def process_image_files_in_folders(command, mode):
    folders = [folder for folder in os.listdir() if os.path.isdir(folder)]
    
    if mode == "2":
        processes = []
    
    for folder in folders:
        exe_path = os.path.join(folder, "rdopng.exe")
        if os.path.exists(exe_path):
            png_files = [file for file in os.listdir(folder) if file.lower().endswith(".png")]
            for png_file in png_files:
                cmd = command.replace("1.png", png_file)
                if mode == "1":
                    run_command(cmd, folder)
                elif mode == "2":
                    process = subprocess.Popen(cmd, shell=True, cwd=folder)
                    processes.append(process)
    
    if mode == "2":
        # Wait for all processes to complete
        for process in processes:
            process.wait()

# Helper function to set up folders and files
def setup_folders_and_files():
    if not os.path.exists("CHECKER.txt"):
        with open("CHECKER.txt", "w") as checker_file:
            checker_file.write("ready absent")
            
setup_folders_and_files()

# Helper functions for user input
def choose_mode():
    return input("Choose mode (1: Iteration, 2: Parallel): ")

# COMPOSITION phase
def composition_phase():
    with open("CHECKER.txt", "r+") as checker_file:
        checker_content = checker_file.read()
        if "ready" in checker_content and "absent" in checker_content:
            folders_to_create = [file.split(".")[0] for file in os.listdir() if file.lower().endswith(".png")]
            for folder_name in folders_to_create:
                os.makedirs(folder_name, exist_ok=True)
                shutil.move(f"{folder_name}.png", folder_name)
                shutil.copy("rdopng.exe", folder_name)
            checker_content = checker_content.replace("absent", "present")
            checker_content = checker_content.replace("ready", "unready")
            checker_file.seek(0)
            checker_file.write(checker_content)

        elif "unready" in checker_content:
            checker_content = checker_content.replace("unready", "ready")
            checker_file.seek(0)
            checker_file.write(checker_content)
            for folder in os.listdir():
                if os.path.isdir(folder):
                    shutil.copy("rdopng.exe", folder)

# PRE-PROCESS phase
user_mode = choose_mode()

# Define presets and their corresponding commands
presets = {
    "1": "-level 3 -two_pass -lambda 300"
}

def choose_preset():
    print("Available presets:")
    for key, value in presets.items():
        print(f"{key}: {value}")
    return input("Choose preset (1: Optimal): ")

# Get the selected preset command
preset = choose_preset()
selected_command = f"rdopng {presets[preset]} 1.png"

# Start the overall timer before PROCESS phase
overall_start_time = time.time()

# COMPOSITION phase
composition_phase()

# PROCESS phase
process_image_files_in_folders(selected_command, user_mode)

# POST-PROCESS phase
overall_elapsed_time = time.time() - overall_start_time

# Convert overall_elapsed_time to integer seconds
elapsed_seconds = int(overall_elapsed_time)

# Handle print format for time elapsed
hours, rem = divmod(elapsed_seconds, 3600)
minutes, seconds = divmod(rem, 60)

time_string = ""
if hours > 0:
    time_string += f"{hours} hour{'s' if hours > 1 else ''} and "
if minutes > 0:
    time_string += f"{minutes} minute{'s' if minutes > 1 else ''} and "
time_string += f"{seconds} second{'s' if seconds > 1 else ''}"

# Display the mode and preset
mode_description = "Iteration" if user_mode == "1" else "Parallel"
preset_description = presets.get(preset, "Custom Preset")

print(f"Used mode: {mode_description}")
print(f"Preset: {preset_description}")

print("\nTime elapsed:", time_string)

# Create or update the TIMER.txt file
with open("TIMER.txt", "w") as timer_file:
    timer_file.write(f"Used mode: {mode_description}\n")
    timer_file.write(f"Preset: {preset_description}\n")
    timer_file.write(f"Time elapsed: {time_string}\n")

try:
    input("\nPress Enter to exit...")
except EOFError:
    pass  # Ignore if Ctrl+D (EOF) is encountered
