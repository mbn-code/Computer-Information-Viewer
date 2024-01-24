# Computer Information Viewer

This Python script, "computer_information.py," is a system information viewer that provides details about your computer's CPU, memory, disk, and network. It utilizes various Python modules such as `platform`, `subprocess`, `tkinter`, `cpuinfo`, and `psutil` to gather and display relevant information.

## Features

- **CPU Information:** Displays information about the CPU, including brand, architecture, number of cores (logical and physical), and frequency.

- **Memory Information:** Provides details about the system's memory, including total, available, used, and the percentage of used memory.

- **Disk Information:** Displays information about each disk partition, including mount point, total space, used space, free space, and the percentage of used space.

- **Network Information:** Shows the hostname and IP address of the computer.

## Setup

Before running the script, ensure that the required modules are installed. The script will attempt to install them if they are missing. You can also manually install the modules using the following command:

```bash
pip install psutil py-cpuinfo GPUtil
```

## Usage

1. Run the script using Python 3:

    ```bash
    python computer_information.py
    ```

2. The graphical user interface (GUI) window will open, displaying detailed information about your computer.

## Dependencies

- `platform`: Provides access to the platform's identifying data.
- `subprocess`: Allows the script to run shell commands.
- `tkinter`: Used to create the graphical user interface (GUI).
- `cpuinfo`: Retrieves information about the CPU.
- `psutil`: Provides an interface to gather system information, including CPU, memory, disk, and network details.

## Notes

- If any required modules are missing, the script attempts to install them automatically.
- The window is configured to resize based on the size of its contents.
- The window is centered on the screen.
