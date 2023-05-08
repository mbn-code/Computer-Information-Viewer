import platform
import subprocess
import tkinter as tk
import cpuinfo
import psutil

# Check if required modules are installed and install them if necessary
required_modules = ['psutil', 'py-cpuinfo', 'GPUtil']
for module in required_modules:
    try:
        __import__(module)
    except ImportError:
        print(f"Module {module} is not installed. Installing...")
        subprocess.run(['pip', 'install', module])

# Get system information
uname = platform.uname()
system = platform.system()
release = platform.release()
version = platform.version()
machine = platform.machine()
node = platform.node()

# Get CPU information
cpu_info = cpuinfo.get_cpu_info()

# Get memory information
mem = psutil.virtual_memory()

# Get disk information
partitions = psutil.disk_partitions()
disk_usage = [psutil.disk_usage(partition.mountpoint) for partition in partitions]

# Get network information
import socket
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

# Create the Tkinter window
window = tk.Tk()
window.title("System Information")
window.configure(bg="#f0f0f0")  # Set background color

# Create a frame for each section of information
cpu_frame = tk.Frame(window, bg="#ffffff", padx=10, pady=10)  # Set background color and padding
cpu_frame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)

mem_frame = tk.Frame(window, bg="#ffffff", padx=10, pady=10)  # Set background color and padding
mem_frame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)

disk_frame = tk.Frame(window, bg="#ffffff", padx=10, pady=10)  # Set background color and padding
disk_frame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)

network_frame = tk.Frame(window, bg="#ffffff", padx=10, pady=10)  # Set background color and padding
network_frame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)

# Create labels for each section of information
cpu_label = tk.Label(cpu_frame, text="CPU Information", font=("Arial", 20, "bold"), fg="#333333")  # Set font and text color
cpu_label.pack(side=tk.TOP, anchor=tk.CENTER)

mem_label = tk.Label(mem_frame, text="Memory Information", font=("Arial", 20, "bold"), fg="#333333")  # Set font and text color
mem_label.pack(side=tk.TOP, anchor=tk.CENTER)

disk_label = tk.Label(disk_frame, text="Disk Information", font=("Arial", 20, "bold"), fg="#333333")  # Set font and text color
disk_label.pack(side=tk.TOP, anchor=tk.CENTER)

network_label = tk.Label(network_frame, text="Network Information", font=("Arial", 20, "bold"), fg="#333333")  # Set font and text color
network_label.pack(side=tk.TOP, anchor=tk.CENTER)

# Add the CPU information to the CPU frame
tk.Label(cpu_frame, text=f"Brand: {cpu_info['brand_raw']}", bg="#ffffff").pack(side=tk.TOP, anchor=tk.W)  # Set background color
tk.Label(cpu_frame, text=f"Architecture: {cpu_info['arch']}", bg="#ffffff").pack(side=tk.TOP, anchor=tk.W)  # Set background color
tk.Label(cpu_frame, text=f"Cores: {psutil.cpu_count(logical=True)} (Logical), {psutil.cpu_count(logical=False)} (Physical)", bg="#ffffff").pack(side=tk.TOP, anchor=tk.W)  # Set background color
tk.Label(cpu_frame, text=f"Frequency: {cpu_info['hz_actual_friendly']}", bg="#ffffff").pack(side=tk.TOP, anchor=tk.W)  # Set background color

# Add the memory information to the memory frame
tk.Label(mem_frame, text=f"Total: {round(mem.total / (1024**3), 2)} GB", bg="#ffffff").pack(side=tk.TOP, anchor=tk.W)  # Set background color
tk.Label(mem_frame, text=f"Available: {round(mem.available / (1024**3), 2)} GB", bg="#ffffff").pack(side=tk.TOP, anchor=tk.W)  # Set background color
tk.Label(mem_frame, text=f"Used: {round(mem.used / (1024**3), 2)} GB", bg="#ffffff").pack(side=tk.TOP, anchor=tk.W)  # Set background color
tk.Label(mem_frame, text=f"Percent Used: {mem.percent}%", bg="#ffffff").pack(side=tk.TOP, anchor=tk.W)  # Set background color

# Add the disk information to the disk frame
for i, partition in enumerate(partitions):
    tk.Label(disk_frame, text=f"Partition {i+1}: {partition.mountpoint}", bg="#ffffff").pack(side=tk.TOP, anchor=tk.W)  # Set background color
    tk.Label(disk_frame, text=f"Total: {round(disk_usage[i].total / (1024**3), 2)} GB", bg="#ffffff").pack(side=tk.TOP, anchor=tk.W)  # Set background color
    tk.Label(disk_frame, text=f"Used: {round(disk_usage[i].used / (1024**3), 2)} GB", bg="#ffffff").pack(side=tk.TOP, anchor=tk.W)  # Set background color
    tk.Label(disk_frame, text=f"Free: {round(disk_usage[i].free / (1024**3), 2)} GB", bg="#ffffff").pack(side=tk.TOP, anchor=tk.W)  # Set background color
    tk.Label(disk_frame, text=f"Percent Used: {disk_usage[i].percent}%", bg="#ffffff").pack(side=tk.TOP, anchor=tk.W)  # Set background color

# Add the network information to the network frame
tk.Label(network_frame, text=f"Hostname: {hostname}", bg="#ffffff").pack(side=tk.TOP, anchor=tk.W)  # Set background color
tk.Label(network_frame, text=f"IP Address: {ip_address}", bg="#ffffff").pack(side=tk.TOP, anchor=tk.W)  # Set background color

# Configure the window to resize based on the size of its contents
window.update_idletasks()
window.minsize(window.winfo_width() + 20, window.winfo_height() + 20)
window.resizable(0, 0)

# Center the window on the screen
window.update_idletasks()
width = window.winfo_width()
height = window.winfo_height()
x = (window.winfo_screenwidth() // 2) - (width // 2)
y = (window.winfo_screenheight() // 2) - (height // 2)
window.geometry(f"{width}x{height}+{x}+{y}")

# Start the Tkinter event loop
window.mainloop()