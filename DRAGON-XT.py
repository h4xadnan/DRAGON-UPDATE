import getpass
import os
import time
from binance.client import Client
from random import choice
from colorama import Fore, Style, init
from datetime import datetime, timedelta
import urllib3
import warnings

# Suppress only the InsecureRequestWarning from urllib3
from urllib3.exceptions import InsecureRequestWarning
warnings.simplefilter('ignore', InsecureRequestWarning)

# Initialize colorama
init(autoreset=True)

# User's Token and Password
correct_email = "dx"
correct_password = "dx"

# Quotex API setup
api_key = '54i4y3jK3wqnRlZ6n2t4isgcHrhSTAjHFOHk7zZLvqU8DpvbpND3yR6YkAVjmFKe'
api_secret = '20A8irk55nARO9FKiPxXpmYAfp9riEZLlV6ZeutaATy8AJ6ZtaGHnSZRt27OYFTH'

# Initialize Binance client with API keys
client = Client(api_key, api_secret, {"timeout": 60})

# Disable SSL verification by modifying the session after client initialization
client.session.verify = False

# Expanded trading pairs including USDNGN
pairs = [
    'EURUSD', 'NZDCAD', 'NZDCHF', 'NZDJPY', 'NZDUSD', 'USDZAR', 'PFE', 'MSFT', 'USDIDR', 'USDCAD', 'USDPHP', 'GBPUSD', 'USDPKR', 'USDTRY', 'USDDZD', 'USDMXN', 'USDEGP',
    'USDINR', 'EURUSD-OTC', 'USDJPY-OTC', 'GBPUSD-OTC', 'CADJPY-OTC', 'CHFJPY-OTC', 'EURJPY-OTC', 'EURAUD-OTC', 'EURCAD-OTC', 'EURCHF-OTC', 'GBPCAD-OTC', 'AUDCAD-OTC', 'EURGBP-OTC', 'USCrude', 'UKBrent', 'Silver', 'Gold', 'USDCOP', 'EURJPY', 'EURGBP', 'AUDUSD', 'CADJPY', 'USDARS',
    'Bitcoin', 'AUDCAD', 'AUDCHF', 'AUDJPY', 'AUDNZD', 'CADCHF', 'CADJPY', 'CHFJPY', 'EURAUD', 'EURCAD', 'EURCHF', 'EURNZD', 'EURSGD', 'GBPAUD', 'GBPCAD', 'GBPCHF', 'GBPJPY', 'GBPNZD', 'USDBDT', 'FAB', 'Johnson', 'AXP', 'INTEL', 'USDCHF', 'USDBRL', 'CADCHF', 'USDCAD', 'MCD', 'AUDUSD', 'BNBBTC',
    'USDJPY', 'USDNGN'
]

# Step 1: User Login
def login():
    print(Style.BRIGHT + Fore.GREEN + "Log In Now  DRAGON-XT..!")
    print("\n")
    email = input(Style.BRIGHT + Fore.CYAN + "Enter DRAGON Token ID: ")
    print("\n")
    password = getpass.getpass(Style.BRIGHT + Fore.YELLOW + "Enter Dragon Password: ")

    # Check for correct email and password
    if email == correct_email and password == correct_password:
        print(Style.BRIGHT + Fore.GREEN + "Login successful!")
        time.sleep(1)
    else:
        print(Style.BRIGHT + Fore.RED + "Login failed! Exiting...")
        exit()

# Step 2: Clear screen after login
def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

# Step 3: Banner Design and Input Prompt
def show_banner():
    print(Fore.RED + """

     ██████╗░██████╗░░█████╗░░██████╗░░█████╗░███╗░░██╗
     ██╔══██╗██╔══██╗██╔══██╗██╔════╝░██╔══██╗████╗░██║
     ██║░░██║██████╔╝███████║██║░░██╗░██║░░██║██╔██╗██║
     ██║░░██║██╔══██╗██╔══██║██║░░╚██╗██║░░██║██║╚████║
     ██████╔╝██║░░██║██║░░██║╚██████╔╝╚█████╔╝██║░╚███║
     ╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝░╚═════╝░░╚════╝░╚═╝░░╚══╝
    """)
    print(" " + Fore.CYAN + Style.BRIGHT + "﴾◀═══════>> DRAGON 𖤍 IS MOST POWERFUL 𖤍 SOFTWARE <<═══════➤﴿")
    print(" " + Fore.CYAN + Style.BRIGHT + "﴾◀═════════════════>> DRAGON - XT v4.2 <<═════════════════➤﴿")
    print(" " + Fore.CYAN + Style.BRIGHT + "﴾◀══════════════>> TELEGRAM: @H4X_ADNAN_LR <<═════════════➤﴿")
    print(" " + Fore.CYAN + Style.BRIGHT + "﴾◀═══════════════>> DEVELOPER ―‣ ADNAN'〆 <<══════════════➤﴿")
    print("\n" *2)
    print("            " + Fore.YELLOW + Style.BRIGHT + "TIME_ZONE Alaska/AKST UTC -9:00")
    print("    " + Fore.MAGENTA + Style.BRIGHT + "AVAILABLE BROKER [(1) QUOTEX (2)POCKET (3)BINOLLA ]")
    print("\n")

from random import choice
from colorama import Fore, Style

# Sample pairs, replace this with your actual pairs
pairs = [
    'EURUSD', 'NZDCAD', 'NZDCHF', 'NZDJPY', 'NZDUSD', 'USDZAR', 'PFE', 'MSFT', 'USDIDR', 'USDCAD', 'USDPHP', 'GBPUSD', 'USDPKR', 'USDTRY', 'USDDZD', 'USDMXN', 'USDEGP',
    'USDINR', 'USCrude', 'UKBrent', 'Silver', 'Gold', 'USDCOP', 'EURJPY', 'EURGBP', 'AUDUSD', 'CADJPY', 'USDJPY-OTC', 'GBPUSD-OTC', 'CADJPY-OTC', 'CHFJPY-OTC', 'EURJPY-OTC', 'EURAUD-OTC', 'EURCAD-OTC', 'EURCHF-OTC', 'GBPCAD-OTC', 'AUDCAD-OTC', 'EURGBP-OTC', 'USDARS',
    'Bitcoin', 'AUDCAD', 'AUDCHF', 'EURUSD-OTC', 'AUDJPY', 'AUDNZD', 'CADCHF', 'CADJPY', 'CHFJPY', 'EURAUD', 'EURCAD', 'EURCHF', 'EURNZD', 'EURSGD', 'GBPAUD', 'GBPCAD', 'GBPCHF', 'GBPJPY', 'GBPNZD', 'USDBDT', 'FAB', 'Johnson', 'AXP', 'INTEL', 'USDCHF', 'USDBRL', 'CADCHF', 'USDCAD', 'MCD', 'AUDUSD', 'BNBBTC',
     'USDJPY', 'USDNGN'
]


def get_user_input():
    # Prompt for operator choice
    while True:
        chose_operator = input(Style.BRIGHT + Fore.CYAN + "𓆰⚚𓆪 CHOOSE YOUR OPERATOR :- {1} {2} {3}: ")

        brokers = {'1': "QUOTEX", '2': "Pocket Option", '3': "Binolla"}

        if chose_operator in brokers:
            print(Style.BRIGHT + Fore.GREEN + f"Selected Broker: {brokers[chose_operator]}")
            break
        else:
            print(Style.BRIGHT + Fore.RED + "Broker not found. Please select a valid option (1, 2, or 3).")

    # Prompt for currency pairs and validate input
    while True:
        selected_pairs = input(Style.BRIGHT + Fore.WHITE + "𓆰⚚𓆪 TYPE YOUR CURRENCY NAME: ").split(",")
        selected_pairs = [pair.strip() for pair in selected_pairs if pair.strip() in pairs]

        if not selected_pairs:
            print(Style.BRIGHT + Fore.RED + "Invalid pair selected. Please choose a valid pair.")
        else:
            break

    # Prompt for martingale count and validate input
    while True:
        martingale_count = input(Style.BRIGHT + Fore.CYAN + "𓆰⚚𓆪 HOW MANY MARTINGALE DO YOU NEED?: ")

        if martingale_count.isdigit() and int(martingale_count) <= 4:
            break
        else:
            print(Style.BRIGHT + Fore.RED + "Oops, out of range. Please enter a value up to 4.")

    # Prompt for day analysis and validate input
    while True:
        day_analysis = input(Style.BRIGHT + Fore.WHITE + "𓆰⚚𓆪 DAY ANALYSIS: ")

        if day_analysis.isdigit() and int(day_analysis) <= 30:
            break
        else:
            print(Style.BRIGHT + Fore.RED + "Oops, out of range. Please enter a value up to 30.")

    # Prompt for minimum and maximum percentage and validate input
    while True:
        min_percentage = input(Style.BRIGHT + Fore.RED + "𓆰⚚𓆪 MINIMUM PERCENTAGE: ")

        if min_percentage.isdigit() and int(min_percentage) <= 100:
            break
        else:
            print(Style.BRIGHT + Fore.RED + "Oops, out of range. Please enter a value up to 100.")

    while True:
        max_percentage = input(Style.BRIGHT + Fore.GREEN + "𓆰⚚𓆪 MAXIMUM PERCENTAGE: ")

        if max_percentage.isdigit() and int(max_percentage) <= 100:
            break
        else:
            print(Style.BRIGHT + Fore.RED + "Oops, out of range. Please enter a value up to 100.")

    # Signal Type Selection
    signal_type_prompt = "𓆰⚚𓆪 SELECT SIGNAL TYPE (CALL/PUT/BOTH): "
    print(f"{Fore.YELLOW}{Style.BRIGHT}{signal_type_prompt}{Style.RESET_ALL}", end="")

    while True:
        signal_type = input().strip().lower()
        if signal_type in ['call', 'put', 'both']:
            break
        else:
            print(Style.BRIGHT + Fore.RED + "Invalid signal type. Please choose CALL, PUT, or BOTH.")
            print(f"{Fore.YELLOW}{Style.BRIGHT}{signal_type_prompt}{Style.RESET_ALL}", end="")

    # Start and end time input
    start_time = input(Style.BRIGHT + Fore.GREEN + "𓆰⚚𓆪 START OF THE LIST (HH:MM): ")
    end_time = input(Style.BRIGHT + Fore.RED + "𓆰⚚𓆪 END OF THE LIST (HH:MM): ")
    print("\n")
    print(Style.BRIGHT + Fore.GREEN + "Loading Asset Data...")

    # Define detection variable here (either as a fixed value or user input)
    detection = "some_default_value"  # Replace with actual value or input prompt if needed

    # Return all 9 variables
    return selected_pairs, signal_type, martingale_count, day_analysis, min_percentage, max_percentage, detection, start_time, end_time


# Step 4: Signal Generation


from datetime import datetime, timedelta
from random import choice
import time
import sys
from colorama import Fore, Style  # Make sure to import these for coloring

def animate_loading(selected_pairs):
    colors = ["\033[91m", "\033[92m"]
    bold = "\033[1m"
    reset = "\033[0m"
    text = "GETTING ASSET'S..."
    spinner = ['\\', '|', '/', '-']

    for i, pair in enumerate(selected_pairs):
        color = colors[i % 2]

        end_time = time.time() + 3
        while time.time() < end_time:
            for spin in spinner:
                sys.stdout.write(f"\r{bold}{color}{text}{spin}   {pair}{reset}")
                sys.stdout.flush()
                time.sleep(0.05)  # This is the smoother speed now

    # After all pairs have been processed, display Done message
    sys.stdout.write(f"\r{bold}{color}{text} Done with all pairs...{reset}")
    sys.stdout.flush()
    print("\n")


def generate_signal(selected_pairs, start_time, end_time, signal_type):
    actions = ['CALL'] if signal_type == 'call' else ['PUT'] if signal_type == 'put' else ['CALL', 'PUT']

    animate_loading(selected_pairs)

    signals = []
    current_time = datetime.now() + timedelta(minutes=1)

    start_hour, start_minute = map(int, start_time.split(':'))
    end_hour, end_minute = map(int, end_time.split(':'))

    start_time_dt = current_time.replace(hour=start_hour, minute=start_minute, second=0, microsecond=0)
    end_time_dt = current_time.replace(hour=end_hour, minute=end_minute, second=59, microsecond=999999)

    if start_time_dt >= end_time_dt:
        print("Start time must be before end time.")
        return signals

    otc_pairs = ['USDBDT', 'USDBRL', 'USDNGN', 'USDMXN', 'USDPKR', 'USDTRY',
                 'UKBrent', 'AUDCAD', 'AUDCHF', 'AUDJPY', 'AUDNZD', 'CADCHF',
                 'BOIC', 'CADJPY', 'CHFJPY', 'EURAUD', 'USDJPY-OTC', 'GBPUSD-OTC', 'CADJPY-OTC', 'CHFJPY-OTC', 'EURJPY-OTC', 'EURAUD-OTC', 'EURCAD-OTC', 'EURCHF-OTC', 'GBPCAD-OTC', 'AUDCAD-OTC', 'EURGBP-OTC', 'EURCAD', 'EURCHF',
                 'EURSGD', 'EURNZD', 'GBPAUD', 'GBPCAD', 'GBPCHF', 'GBPJPY',
                 'GBPNZD', 'NZDCAD', 'NZDUSD', 'NZDCHF', 'NZDJPY', 'USDZAR',
                 'MCD', 'MSFT', 'PFE', 'USDIDR', 'EURUSD-OTC', 'USCrude', 'Silver', 'Gold',
                 'FAB', 'Bitcoin', 'INTEL', 'AXP', 'Johnson', 'USDCOP',
                 'USDDZD', 'USDPHP', 'USDEGP', 'USDARS', 'USDINR']

    time_intervals = [5, 6, 9, 13, 7, 14, 19, 24, 32, 43, 57]

    current_signal_time = start_time_dt

    # Generate signals with specified intervals between them
    while current_signal_time <= end_time_dt:
        for pair in selected_pairs:
            action = choice(actions)  # Choose action randomly
            color = Fore.GREEN if action == 'CALL' else Fore.RED  # Set color based on action

            if pair in otc_pairs:
                signals.append((current_signal_time, f"{color}{current_signal_time.strftime('%H:%M')},{pair}-OTC,{action}{Style.RESET_ALL}"))
            else:
                signals.append((current_signal_time, f"{color}{current_signal_time.strftime('%H:%M')},{pair},{action}{Style.RESET_ALL}"))

            # Randomly select the next interval
            interval = choice(time_intervals)
            current_signal_time += timedelta(minutes=interval)

            # Stop if the next signal time goes beyond the end time
            if current_signal_time > end_time_dt:
                break

    # Sort signals by time to maintain ascending order
    signals.sort(key=lambda x: x[0])

    print("=" * 50)
    for _, signal in signals:
        sys.stdout.write(signal + "\n")
        sys.stdout.flush()
        time.sleep(0.3)

    print("=" * 50)

def process_signals(signals):
    return [s[1] for s in signals]

# Step 5: Signal Filtering (removed for no filtering)
def filter_signals(signals):
    return signals  # Return all signals without filtering

# Step 6: Display Signals
def display_signals(signals):
    print("\n" * 1)  # Space before signals
    print(" " + Fore.YELLOW + Style.BRIGHT + "Generated 𓆩DRAGON𓆪 Signal's")
    print(Style.BRIGHT + Fore.RED + "=" * 50)
    print("\n")
    for signal in signals:
        print("        " + Fore.LIGHTRED_EX + signal)  # Align signals to the right

    print("\n")
    print(Style.BRIGHT + Fore.RED + "=" * 50)
    print("\n" * 1)  # Space after signals
    finished_message = Fore.LIGHTYELLOW_EX + Style.BRIGHT + " 𓆩====== FINISHED ✧ SINAI'S ======𓆪"
    print("     " + finished_message)
    print("\n")
    print("             " + Style.BRIGHT + Fore.CYAN + " 𓆩DRAGON-XT ⚚ v4.05𓆪")  # Make sure this line has the same indentation as others in this block.

# Step 7: Copying Signals
def copy_signals(signals):
    # Join all signals into a single string separated by new lines
    signal_text = "\n".join(signals)
    # Copying to clipboard (you may need to install 'pyperclip')
    try:
        import pyperclip
        pyperclip.copy(signal_text)
        print(Style.BRIGHT + Fore.GREEN + "Signals copied to clipboard!")
    except ImportError:
        print(Style.BRIGHT + Fore.RED + "pyperclip is not installed. Please install it to use this feature.")


# Step 8: Main Program Flow
def main():
    clear_screen()
    login()
    clear_screen()
    show_banner()

    # Getting all the values from get_user_input()
    selected_pairs, signal_type, martingale_count, day_analysis, min_percentage, max_percentage, detection, start_time, end_time = get_user_input()

    # Passing signal_type to generate_signal()
    signals = generate_signal(selected_pairs, start_time, end_time, signal_type)  # Passing signal_type here

    # Display the signal generation information
    if not signals:
        print(Style.BRIGHT + Fore.YELLOW + "𓆩====== FINISHED ✧ SIGNAL'S ======𓆪")
        print("\n")
        print("           " + Style.BRIGHT + Fore.CYAN + " 𓆩DRAGON-XT ⚚ v4.2𓆪")
    else:
        print("\n" * 1)  # Space before signals
        print(" " + Fore.YELLOW + Style.BRIGHT + "Generated 𓆩DRAGON𓆪 Signal's")
        print(Style.BRIGHT + Fore.RED + "=" * 50)
        print("\n")
        for signal in signals:
            print("        " + Fore.LIGHTRED_EX + signal)  # Align signals to the right

        print("\n")
        print(Style.BRIGHT + Fore.RED + "=" * 50)
        print("\n" * 1)  # Space after signals
        finished_message = Fore.LIGHTYELLOW_EX + Style.BRIGHT + " 𓆩====== FINISHED ✧ SINAI'S ======𓆪"
        print("     " + finished_message)
        print("\n")

    print("\n")
    print("        " + Style.BRIGHT + Fore.WHITE + "Type { C } For Copy SIGNAL'S")
    print("=" * 50)
    print("            " + Style.BRIGHT + Fore.RED + "Press " + Style.BRIGHT + Fore.YELLOW + "( q )" + Style.BRIGHT + Fore.RED + " For Quit")
    print("=" * 50)

    while True:
        choice = input().strip().lower()
        if choice == 'c':
            copy_signals(signals)  # Copy the signals
        elif choice == 'q':
            print(Style.BRIGHT + Fore.GREEN + "Exiting the DRAGON..Good Bye...")
            break

# Run the main function
if __name__ == "__main__":
    main()


from datetime import datetime
import pytz

# Set timezone to UTC -9:00
utc_minus_9_time_zone = pytz.timezone('Etc/GMT+9')
current_time_utc_minus_9 = datetime.now(utc_minus_9_time_zone)

print("Current time (UTC -9:00):", current_time_utc_minus_9.strftime('%Y-%m-%d %H:%M:%S'))