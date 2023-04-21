import select
import platform
import sys
import os
import re
import json
import urllib.request
import time
from colorama import init, Fore
import pyfiglet
init(autoreset=True)

if sys.platform == 'win32':
    import msvcrt
else:
    import termios
    import tty


def starter():
    ascii_text = pyfiglet.figlet_format(f"{Fore.CYAN}INFORMATION IP GATHERING")
    print(Fore.CYAN + ascii_text)


platform_name = platform.system()


def clear_terminal():
    # Clear the terminal screen based on the platform
    if platform_name == "Windows":
        os.system("cls")
    elif platform_name in ["Linux", "Darwin"]:
        os.system("clear")
    else:
        print("Sorry, I don't know how to clear the terminal on this platform.")


def is_valid_ip(ip):
    # Regular expression for matching an IP address
    pattern = re.compile(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$')

    # Check if the given IP matches the pattern
    if pattern.match(ip):
        # Split the IP address into its four components
        parts = ip.split('.')
        # Check that each component is a valid number between 0 and 255
        if all(0 <= int(part) <= 255 for part in parts):
            return True
    return False


def get_ip_data(ip):
    clear_terminal()
    starter()
    print(f"{Fore.LIGHTWHITE_EX}Creator : GiuCoder\n\n")
    print("\nGetting Data ...")
    time.sleep(2)
    clear_terminal()
    starter()
    print(f"{Fore.LIGHTWHITE_EX}Creator : GiuCoder\n\n")
    # Construct the URL for the IPinfo API
    url = f'http://ipinfo.io/{ip}/json'
    try:
        # Retrieve the data from the API
        response = urllib.request.urlopen(url)
        # Parse the JSON data
        data = json.load(response)

        # Extract the desired fields from the JSON data
        ip = data.get('ip', '')
        org = data.get('org', '')
        city = data.get('city', '')
        country = data.get('country', '')
        region = data.get('region', '')
        timezone = data.get('timezone', '')
        loc = data.get('loc', '')
        postal = data.get('postal', '')
        # Construct a dictionary containing the extracted data
        ip_data = {
            'IP': ip,
            'Organization': org,
            'City': city,
            'Country': country,
            'Region': region,
            'Timezone': timezone,
            'Location': loc,
            'Postal': postal
        }
        return ip_data
    except urllib.error.URLError as e:
        print(f"Error while retrieving data from API: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"Error while parsing JSON data: {e}")
        return None


def starter():
    ascii_text = pyfiglet.figlet_format("INFORMATION IP GATHERING")
    print(ascii_text)


platform_name = platform.system()


def clear_terminal():
    # Clear the terminal screen based on the platform
    if platform_name == "Windows":
        os.system("cls")
    elif platform_name in ["Linux", "Darwin"]:
        os.system("clear")
    else:
        print("Sorry, I don't know how to clear the terminal on this platform.")


def is_valid_ip(ip):
    # Regular expression for matching an IP address
    pattern = re.compile(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$')

    # Check if the given IP matches the pattern
    if pattern.match(ip):
        # Split the IP address into its four components
        parts = ip.split('.')
        # Check that each component is a valid number between 0 and 255
        if all(0 <= int(part) <= 255 for part in parts):
            return True
    return False


def get_ip_data(ip):
    clear_terminal()
    starter()
    print(f"{Fore.LIGHTWHITE_EX}\nCreator : GiuCoder\n\n")
    print("\nGetting Data ...")
    time.sleep(2)
    clear_terminal()
    starter()
    # Construct the URL for the IPinfo API
    url = f'http://ipinfo.io/{ip}/json'
    try:
        # Retrieve the data from the API
        response = urllib.request.urlopen(url)
        # Parse the JSON data
        data = json.load(response)

        # Extract the desired fields from the JSON data
        ip = data.get('ip', '')
        org = data.get('org', '')
        city = data.get('city', '')
        country = data.get('country', '')
        region = data.get('region', '')
        timezone = data.get('timezone', '')
        loc = data.get('loc', '')
        postal = data.get('postal', 'N/A')
        # Construct a dictionary containing the extracted data
        ip_data = {
            'IP': ip,
            'Organization': org,
            'City': city,
            'Country': country,
            'Region': region,
            'Timezone': timezone,
            'Location': loc,
            'Postal': postal
        }
        return ip_data
    except urllib.error.URLError as e:
        print(f"Error while retrieving data from API: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"Error while parsing JSON data: {e}")
        return None


def starter():
    ascii_text = pyfiglet.figlet_format("INFORMATION IP GATHERING")
    print(ascii_text)


platform_name = platform.system()


def clear_terminal():
    # Clear the terminal screen based on the platform
    if platform_name == "Windows":
        os.system("cls")
    elif platform_name in ["Linux", "Darwin"]:
        os.system("clear")
    else:
        print("Sorry, I don't know how to clear the terminal on this platform.")


def is_valid_ip(ip):
    # Regular expression for matching an IP address
    pattern = re.compile(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$')

    # Check if the given IP matches the pattern
    if pattern.match(ip):
        # Split the IP address into its four components
        parts = ip.split('.')
        # Check that each component is a valid number between 0 and 255
        if all(0 <= int(part) <= 255 for part in parts):
            return True
    return False


def get_ip_data(ip):
    clear_terminal()
    starter()
    print(f"{Fore.LIGHTWHITE_EX}Creator : GiuCoder\n\n")
    print(f"{Fore.YELLOW}\nGetting Data ...")
    time.sleep(2)
    clear_terminal()
    starter()
    # Construct the URL for the IPinfo API
    url = f'http://ipinfo.io/{ip}/json'
    try:
        # Retrieve the data from the API
        response = urllib.request.urlopen(url)
        # Parse the JSON data
        data = json.load(response)

        # Extract the desired fields from the JSON data
        ip = data.get('ip', '')
        org = data.get('org', '')
        city = data.get('city', '')
        country = data.get('country', '')
        region = data.get('region', '')
        timezone = data.get('timezone', '')
        loc = data.get('loc', '')
        postal = data.get('postal', '')
        # Construct a dictionary containing the extracted data
        ip_data = {
            'IP': ip,
            'Organization': org,
            'City': city,
            'Country': country,
            'Region': region,
            'Timezone': timezone,
            'Location': loc,
            'Postal': postal
        }
        return ip_data
    except urllib.error.URLError as e:
        print(f"{Fore.RED}Error while retrieving data from API: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"{Fore.RED}Error while parsing JSON data: {e}")
        return None


def myip():
    # Get the current IP address
    url_my_ip = 'https://api.ipify.org?format=json'
    response = urllib.request.urlopen(url_my_ip)
    data = json.load(response)
    myip = data['ip']
    return myip


def loading_animation():
    animation_frames = ['-', '\\', '|', '/']
    for i in range(len(animation_frames)):
        sys.stdout.write(f'\rLoading {animation_frames[i]}')
        sys.stdout.flush()
        time.sleep(0.2)

    sys.stdout.write('\r')


clear_terminal()
starter()
print(f"{Fore.LIGHTWHITE_EX}Creator : GiuCoder\n\n")
loading_animation()
while True:
    clear_terminal()
    starter()
    loading_animation()
    clear_terminal()
    starter()
    print(f"{Fore.LIGHTWHITE_EX}Creator : GiuCoder\n\n")

    # Prompt the user to enter an IP address
    ipaddr = input(
        f"Your IP Address : {myip()}\n\nPlease enter an IP address (e.g. 125.164.x.x) : ")
    # Validate the input IP address
    if is_valid_ip(ipaddr):
        print(f'{Fore.GREEN}{ipaddr} is a valid IP address')
        # Prompt the user to generate information for the entered IP address
        generate = input(
            f"{Fore.CYAN}Do you want to generate information for this IP address? (y/n): ")
        if generate.lower() == 'y':
            # Retrieve the IP data for the entered IP address
            ip_data = get_ip_data(ipaddr)
            # Print the retrieved IP data
            for key, value in ip_data.items():
                if value is None:
                    value = value if value else "Not available"
                print(f'{key}: {value}')

            # Print a message
            print("\n\nPress any key to continue...")

            if sys.platform == 'win32':
                # Wait for the user to press a key
                while not msvcrt.kbhit():
                    pass

                # Clear the keyboard buffer
                msvcrt.getch()
            else:
                # Set terminal settings to allow reading of single keystrokes
                fd = sys.stdin.fileno()
                old_settings = termios.tcgetattr(fd)
                tty.setraw(fd)

                # Wait for the user to press a key
                rlist, _, _ = select.select([sys.stdin], [], [], None)
                if rlist:
                    # Read and discard the key
                    sys.stdin.read(1)

                # Restore terminal settings
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        else:
            print("Okay, goodbye!")
    else:
        print(f'{ipaddr} is not a valid IP address')
