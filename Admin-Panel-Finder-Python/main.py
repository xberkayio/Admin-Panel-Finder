# -*- coding: utf-8 -*-
import os, time, sys, platform, subprocess

def clearscreen():
    system = platform.system()
    if system == "Windows": command = "cls"
    elif system == "Linux": command = "clear"
    else: command = "clear"
    os.system(command)

def rainbowtext(text, delay=0.1):
    colors = [
    "\033[31m", "\033[33m", "\033[32m", "\033[36m", "\033[34m", "\033[35m", "\033[37m",
    ]

    for i in range(len(text)):
        char = text[i]
        color = colors[i % len(colors)]
        sys.stdout.write(color + char)
        sys.stdout.flush()
        time.sleep(delay)

    sys.stdout.write("\033[0m")
    sys.stdout.write("\n")

banner = """                                                                                                           
    berkay                                       
"""

class main():
    clearscreen()
    print(banner)
    rainbowtext("Coding by berkay")
    print("""
   \u001b[35m|-*-*-*-Admin Panel Finder-*-*-*-|\n
        \u001b[94m1- So Fast (with aiohttp)
        2- Fast (with urllib3)
        3- Middle (with httpx)
        4- Slow (with requests) 
""")
    choice = int(input("Enter the any number: "))

    source_folder = "source"

    if choice == 1:
        script_path = os.path.join(source_folder, "admin-panel-finder_aiohttp.py")
    elif choice == 2:
        script_path = os.path.join(source_folder, "admin-panel-finder_urllib3.py")
    elif choice == 3:
        script_path = os.path.join(source_folder, "admin-panel-finder_httpx.py")
    elif choice == 4:
        script_path = os.path.join(source_folder, "admin-panel-finder_requests.py")
    else:
        print("\n\033[90m Invalid choice. See You Again ^-^ ")
        time.sleep(2)
    
    subprocess.run(["python", script_path])


if __name__ == "__main__":
    main_instance = main()
