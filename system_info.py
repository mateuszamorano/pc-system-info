import platform
import psutil
import socket

#Designed by Mateus Zamorano, with assistance from ChatGPT

def generate_report():
    print("=" * 45)
    print(" PC SYSTEM DIAGNOSTIC TOOL ")
    print("=" * 45)
    print("Designed by Mateus Zamorano, with assistance from ChatGPT.\n")

    print(f"Hostname: {socket.gethostname()}")
    print(f"Operating System: {platform.system()} {platform.release()}")
    print(f"Architecture: {platform.machine()}")
    print(f"Processor: {platform.processor()}")

    memory = psutil.virtual_memory()
    print("\n--- MEMORY ---")
    print(f"Total RAM: {round(memory.total / (1024 ** 3), 2)} GB")
    print(f"Available RAM: {round(memory.available / (1024 ** 3), 2)} GB")

    disk = psutil.disk_usage('/')
    print("\n--- DISK ---")
    print(f"Total Disk: {round(disk.total / (1024 ** 3), 2)} GB")
    print(f"Free Disk: {round(disk.free / (1024 ** 3), 2)} GB")

    input("\nPress ENTER to exit...")

if __name__ == "__main__":
    generate_report()
