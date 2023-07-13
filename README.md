# GahDat
This script is a toolkit for creating different types of payloads and generates a text file with the payload creation details.

# Payload Creator

This script allows you to create different types of payloads using Metasploit's `msfvenom` tool. The supported payload types are:

1. Windows EXE
2. Python
3. Bash
4. DLL

## Prerequisites

- Metasploit Framework is installed on your system.
- You have administrative privileges (sudo access) to run the script.

## Usage

1. Clone the repository:

```shell
git clone https://github.com/CollinEdward/GahDat.git
```

Navigate to the script directory:

```shell
cd GahDat
```

Run the script with sudo privileges:
```shell
python3 GahDat.py
```

Follow the menu instructions to select and create the desired payload.

**Available Options**

The script provides the following options:

- Create Windows EXE payload: Generates a Windows EXE payload with specified configurations.
- Create Python payload: Generates a Python payload with specified configurations.
- Create Bash payload: Generates a Bash payload with specified configurations.
- Create DLL payload: Generates a DLL payload with specified configurations.
- Exit: Exits the script.

**Output**

After creating a payload, the script generates the corresponding payload file and a details file for reference. The details file includes information about the payload such as name, encoder, iterations, LHOST, LPORT, and timestamp.

**Note**

Make sure to review the details file for the payload you created to access a longer view of the payload creation process.

Note: This README assumes that you have the necessary dependencies installed and provides a basic structure for your GitHub README. You can customize it further to include additional information if needed.
