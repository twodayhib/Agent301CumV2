import requests
import json
import urllib.parse
import os
from datetime import datetime
import time
from core.helper import get_headers, countdown_timer, extract_user_data, config
from colorama import *
import random




class Agent301:
    def __init__(self) -> None:
        self.session = requests.Session()


    def clear_terminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def log(self, message):
        print(
            f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().strftime('%x %X %Z')} ]{Style.RESET_ALL}"
            f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}{message}",
            flush=True
        )

    def welcome(self):
        banner = f"""{Fore.GREEN}
 ██████  ██    ██   ██████  ██    ██  ███    ███  ██████   ███████  ██████  
██       ██    ██  ██       ██    ██  ████  ████  ██   ██  ██       ██   ██ 
██       ██    ██  ██       ██    ██  ██ ████ ██  ██████   █████    ██████  
██       ██    ██  ██       ██    ██  ██  ██  ██  ██   ██  ██       ██   ██ 
 ██████   ██████    ██████   ██████   ██      ██  ██████   ███████  ██   ██     
                                            """
        print(Fore.GREEN + Style.BRIGHT + banner + Style.RESET_ALL)
        print(Fore.GREEN + f" Agent301 v2")
        print(Fore.RED + f" FREE TO USE = Join us on {Fore.GREEN}t.me/cucumber_scripts")
        print(Fore.YELLOW + f" before start please '{Fore.GREEN}git pull{Fore.YELLOW}' to update bot")
        print(f"{Fore.WHITE}~" * 60)

    def format_seconds(self, seconds):
        hours, remainder = divmod(seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}"

    def load_data(self, query: str):
        query_params = urllib.parse.parse_qs(query)
        query = query_params.get('user', [None])[0]

        if query:
            user_data_json = urllib.parse.unquote(query)
            user_data = json.loads(user_data_json)
            first_name = user_data['first_name']
            return first_name
        else:
            raise ValueError("User data not found in query.")
        
    def get_me(self, query: str, retries=3):
        url = "https://api.agent301.org/getMe"
        self.headers.update({ 
            'Authorization': query,
            'Content-Type': 'application/json'
        })
        
        for attempt in range(retries):
            try:
                response = self.session.post(url, headers=self.headers)
                response.raise_for_status()
                result = response.json()
                if result['ok']:
                    return result['result']
                else:
                    return None
            except (requests.RequestException, requests.HTTPError, ValueError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.RED + Style.BRIGHT}HTTP ERROR:{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT} [{attempt+1}/{retries}] {Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    time.sleep(2)
                else:
                    return None
    
    def get_tasks(self, query: str, retries=3):
        url = "https://api.agent301.org/getTasks"
        self.headers.update({ 
            'Authorization': query,
            'Content-Type': 'application/json'
        })
        
        for attempt in range(retries):
            try:
                response = self.session.post(url, headers=self.headers)
                response.raise_for_status()
                result = response.json()
                if result['ok']:
                    return result['result']['data']
                else:
                    return None
            except (requests.RequestException, requests.HTTPError, ValueError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.RED + Style.BRIGHT}HTTP ERROR:{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT} [{attempt+1}/{retries}] {Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    time.sleep(2)
                else:
                    return None
    
    def complete_tasks(self, query: str, task_type: str, retries=3):
        url = "https://api.agent301.org/completeTask"
        data = json.dumps({'type':task_type})
        self.headers.update({ 
            'Authorization': query,
            'Content-Type': 'application/json'
        })

        for attempt in range(retries):
        
            try:
                response = self.session.post(url, headers=self.headers, data=data)
                response.raise_for_status()
                result = response.json()
                if result['ok']:
                    return result['result']
                else:
                    return None
            except (requests.RequestException, requests.HTTPError, ValueError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.RED + Style.BRIGHT}HTTP ERROR:{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT} [{attempt+1}/{retries}] {Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    time.sleep(2)
                else:
                    return None
    
    def load_wheel(self, query: str, retries=3):
        url = "https://api.agent301.org/wheel/load"
        self.headers.update({ 
            'Authorization': query,
            'Content-Type': 'application/json'
        })

        for attempt in range(retries):
            try:
                response = self.session.post(url, headers=self.headers)
                response.raise_for_status()
                data = response.json()
                if data['ok']:
                    return data['result']
                else:
                    return None
            except (requests.RequestException, requests.HTTPError, ValueError) as e:
                    if attempt < retries - 1:
                        print(
                            f"{Fore.RED + Style.BRIGHT}HTTP ERROR:{Style.RESET_ALL}"
                            f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                            f"{Fore.WHITE + Style.BRIGHT} [{attempt+1}/{retries}] {Style.RESET_ALL}",
                            end="\r",
                            flush=True
                        )
                        time.sleep(2)
                    else:
                        return None
                    
    def task_wheel(self, query: str, task: str, retries=3):
        url = "https://api.agent301.org/wheel/task"
        data = json.dumps({'type':task})
        self.headers.update({ 
            'Authorization': query,
            'Content-Type': 'application/json'
        })

        for attempt in range(retries):
            try:
                response = self.session.post(url, headers=self.headers, data=data)
                data = response.json()
                if data['ok']:
                    return data['result']
                else:
                    return None
            except (requests.RequestException, requests.HTTPError, ValueError) as e:
                    if attempt < retries - 1:
                        print(
                            f"{Fore.RED + Style.BRIGHT}HTTP ERROR:{Style.RESET_ALL}"
                            f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                            f"{Fore.WHITE + Style.BRIGHT} [{attempt+1}/{retries}] {Style.RESET_ALL}",
                            end="\r",
                            flush=True
                        )
                        time.sleep(2)
                    else:
                        return None
    
    def spin_wheel(self, query: str, retries=3):
        url = "https://api.agent301.org/wheel/spin"
        self.headers.update({ 
            'Authorization': query,
            'Content-Type': 'application/json'
        })

        for attempt in range(retries):
            try:
                response = self.session.post(url, headers=self.headers)
                response.raise_for_status()
                data = response.json()
                if data['ok']:
                    return data['result']
                else:
                    return None
            except (requests.RequestException, requests.HTTPError, ValueError) as e:
                    if attempt < retries - 1:
                        print(
                            f"{Fore.RED + Style.BRIGHT}HTTP ERROR:{Style.RESET_ALL}"
                            f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                            f"{Fore.WHITE + Style.BRIGHT} [{attempt+1}/{retries}] {Style.RESET_ALL}",
                            end="\r",
                            flush=True
                        )
                        time.sleep(2)
                    else:
                        return None
    
    def load_cards(self, query: str, retries=3):
        url = "https://api.agent301.org/cards/load"
        data = {}
        self.headers.update({ 
            'Authorization': query,
            'Content-Type': 'application/json'
        })

        for attempt in range(retries):
            try:
                response = self.session.post(url, headers=self.headers, json=data)
                response.raise_for_status()
                data = response.json()
                if data:
                    return data['result']
                else:
                    return None
            except (requests.RequestException, requests.HTTPError, ValueError) as e:
                    if attempt < retries - 1:
                        print(
                            f"{Fore.RED + Style.BRIGHT}HTTP ERROR:{Style.RESET_ALL}"
                            f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                            f"{Fore.WHITE + Style.BRIGHT} [{attempt+1}/{retries}] {Style.RESET_ALL}",
                            end="\r",
                            flush=True
                        )
                        time.sleep(2)
                    else:
                        return None
                    
    def check_cards(self, query: str, puzzle_combo, retries=3):
        url = "https://api.agent301.org/cards/check"
        data = json.dumps({"cards":puzzle_combo})
        self.headers.update({ 
            'Authorization': query,
            'Content-Type': 'application/json'
        })

        for attempt in range(retries):
            try:
                response = self.session.post(url, headers=self.headers, data=data)
                response.raise_for_status()
                data = response.json()
                if data:
                    return data['result']
                else:
                    return None
            except (requests.RequestException, requests.HTTPError, ValueError) as e:
                    if attempt < retries - 1:
                        print(
                            f"{Fore.RED + Style.BRIGHT}HTTP ERROR:{Style.RESET_ALL}"
                            f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                            f"{Fore.WHITE + Style.BRIGHT} [{attempt+1}/{retries}] {Style.RESET_ALL}",
                            end="\r",
                            flush=True
                        )
                        time.sleep(2)
                    else:
                        return None
        
    def question(self):
        while True:
            game_puzzle = input("Auto Play Game Puzzle? [y/n] -> ").strip().lower()
            if game_puzzle in ["y", "n"]:
                game_puzzle = game_puzzle == "y"
                break
            else:
                print(f"{Fore.RED+Style.BRIGHT}Invalid Input.{Fore.WHITE+Style.BRIGHT} Choose 'y' or 'n'.{Style.RESET_ALL}")

        puzzle_combo = []
        if game_puzzle:
            while True:
                try:
                    choices = input("Enter The 4 Number Combo Puzzle [ex: 1,2,3,4] -> ").strip()
                    puzzle_combo = [int(x) for x in choices.split(',')]
                    if len(puzzle_combo) == 4:
                        break
                    else:
                        print(f"{Fore.RED+Style.BRIGHT}The Number Entered Must Be Exactly 4.{Style.RESET_ALL}")
                except ValueError:
                    print(f"{Fore.RED+Style.BRIGHT}Invalid input. Use numbers separated by commas.{Style.RESET_ALL}")

        return game_puzzle, puzzle_combo

    def transform_reward(self, reward):
        if reward.startswith('tc'):
            return f"{reward[2:]} TON"  # Remove 'tc' and label as TON
        if reward.startswith('t'):
            return f"{reward[1:]} Ticket"  # Remove 't' and label as Tickets
        elif reward.startswith('c'):
            return f"{reward[1:]} AP"  # Remove 'c' and label as AP
        elif reward.startswith('nt'):
            return f"{reward[2:]} NOT"  # Remove 'nt' and label as NOT
        else:
            return f"Unknown Reward: {reward}"

    def set_proxy(self, proxy):
        self.session.proxies = {
            "http": proxy,
            "https": proxy,
        }
        if '@' in proxy:
            host_port = proxy.split('@')[-1]
        else:
            host_port = proxy.split('//')[-1]
        return host_port

    def process_query(self, query: str, game_puzzle: bool, puzzle_combo):

        user = self.load_data(query)
        get_me = self.get_me(query)
        if get_me:
            self.log(
                f"{Fore.MAGENTA+Style.BRIGHT}[ Account{Style.RESET_ALL}"
                f"{Fore.WHITE+Style.BRIGHT} {user} {Style.RESET_ALL}"
                f"{Fore.MAGENTA+Style.BRIGHT}] [ Balance{Style.RESET_ALL}"
                f"{Fore.WHITE+Style.BRIGHT} {get_me['balance']} {Style.RESET_ALL}"
                f"{Fore.MAGENTA+Style.BRIGHT}] [ Ticket{Style.RESET_ALL}"
                f"{Fore.WHITE+Style.BRIGHT} {get_me['tickets']} {Style.RESET_ALL}"
                f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
            )
            time.sleep(1)

            tasks = self.get_tasks(query)
            if tasks:
                for task in tasks:
                    task_type = task['type']
                    claimed = task['is_claimed']

                    if task and not claimed:
                        if task['type'] == 'video':
                            count = task['count']
                            max_count = task['max_count']

                            while count < max_count:
                                self.log(
                                    f"{Fore.MAGENTA+Style.BRIGHT}[ Task{Style.RESET_ALL}"
                                    f"{Fore.WHITE+Style.BRIGHT} {task['category']} {Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT}-{Style.RESET_ALL}"
                                    f"{Fore.WHITE+Style.BRIGHT} {task['title']} {Style.RESET_ALL}"
                                    f"{Fore.GREEN+Style.BRIGHT}Is Started{Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT} ] [ Watch{Style.RESET_ALL}"
                                    f"{Fore.WHITE+Style.BRIGHT} {count+1}/{max_count} {Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                                )
                                complete = self.complete_tasks(query, task_type)
                                if complete and complete['is_completed']:
                                    self.log(
                                        f"{Fore.MAGENTA+Style.BRIGHT}[ Task{Style.RESET_ALL}"
                                        f"{Fore.WHITE+Style.BRIGHT} {task['category']} {Style.RESET_ALL}"
                                        f"{Fore.MAGENTA+Style.BRIGHT}-{Style.RESET_ALL}"
                                        f"{Fore.WHITE+Style.BRIGHT} {task['title']} {Style.RESET_ALL}"
                                        f"{Fore.GREEN+Style.BRIGHT}Is Completed{Style.RESET_ALL}"
                                        f"{Fore.MAGENTA+Style.BRIGHT}] [ Reward{Style.RESET_ALL}"
                                        f"{Fore.WHITE+Style.BRIGHT} {complete['reward']} {Style.RESET_ALL}"
                                        f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                                    )
                                else:
                                    self.log(
                                        f"{Fore.MAGENTA+Style.BRIGHT}[ Task{Style.RESET_ALL}"
                                        f"{Fore.WHITE+Style.BRIGHT} {task['category']} {Style.RESET_ALL}"
                                        f"{Fore.MAGENTA+Style.BRIGHT}-{Style.RESET_ALL}"
                                        f"{Fore.WHITE+Style.BRIGHT} {task['title']} {Style.RESET_ALL}"
                                        f"{Fore.RED+Style.BRIGHT}Isn't Completed{Style.RESET_ALL}"
                                        f"{Fore.MAGENTA+Style.BRIGHT} ]{Style.RESET_ALL}"
                                    )
                                count += 1

                        else:
                            self.log(
                                f"{Fore.MAGENTA+Style.BRIGHT}[ Task{Style.RESET_ALL}"
                                f"{Fore.WHITE+Style.BRIGHT} {task['category']} {Style.RESET_ALL}"
                                f"{Fore.MAGENTA+Style.BRIGHT}-{Style.RESET_ALL}"
                                f"{Fore.WHITE+Style.BRIGHT} {task['title']} {Style.RESET_ALL}"
                                f"{Fore.GREEN+Style.BRIGHT}Is Started{Style.RESET_ALL}"
                                f"{Fore.MAGENTA+Style.BRIGHT} ]{Style.RESET_ALL}"
                            )

                            complete = self.complete_tasks(query, task_type)
                            if complete and complete['is_completed']:
                                self.log(
                                    f"{Fore.MAGENTA+Style.BRIGHT}[ Task{Style.RESET_ALL}"
                                    f"{Fore.WHITE+Style.BRIGHT} {task['category']} {Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT}-{Style.RESET_ALL}"
                                    f"{Fore.WHITE+Style.BRIGHT} {task['title']} {Style.RESET_ALL}"
                                    f"{Fore.GREEN+Style.BRIGHT}Is Completed{Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT}] [ Reward{Style.RESET_ALL}"
                                    f"{Fore.WHITE+Style.BRIGHT} {complete['reward']} {Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                                )
                            else:
                                self.log(
                                    f"{Fore.MAGENTA+Style.BRIGHT}[ Task{Style.RESET_ALL}"
                                    f"{Fore.WHITE+Style.BRIGHT} {task['category']} {Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT}-{Style.RESET_ALL}"
                                    f"{Fore.WHITE+Style.BRIGHT} {task['title']} {Style.RESET_ALL}"
                                    f"{Fore.RED+Style.BRIGHT}Isn't Completed{Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT} ]{Style.RESET_ALL}"
                                )
            else:
                self.log(
                    f"{Fore.MAGENTA+Style.BRIGHT}[ Task{Style.RESET_ALL}"
                    f"{Fore.RED+Style.BRIGHT} Is None {Style.RESET_ALL}"
                    f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                )
            time.sleep(1)

            if game_puzzle:
                puzzle = self.load_cards(query)
                if puzzle:
                    attempt = puzzle['attemptsLeft']
                    if attempt > 0:
                        check = self.check_cards(query, puzzle_combo)
                        if check and check['isCorrect']:
                            self.log(
                                f"{Fore.MAGENTA+Style.BRIGHT}[ Game Puzzle{Style.RESET_ALL}"
                                f"{Fore.GREEN+Style.BRIGHT} Is Success {Style.RESET_ALL}"
                                f"{Fore.MAGENTA+Style.BRIGHT}] [ Result{Style.RESET_ALL}"
                                f"{Fore.GREEN+Style.BRIGHT} You Win {Style.RESET_ALL}"
                                f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                            )
                        else:
                            self.log(
                                f"{Fore.MAGENTA+Style.BRIGHT}[ Game Puzzle{Style.RESET_ALL}"
                                f"{Fore.GREEN+Style.BRIGHT} Is Success {Style.RESET_ALL}"
                                f"{Fore.MAGENTA+Style.BRIGHT}] [ Result{Style.RESET_ALL}"
                                f"{Fore.RED+Style.BRIGHT} You Lose {Style.RESET_ALL}"
                                f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                            )
                    else:
                        self.log(
                            f"{Fore.MAGENTA+Style.BRIGHT}[ Game Puzzle{Style.RESET_ALL}"
                            f"{Fore.YELLOW+Style.BRIGHT} No Attempt Left {Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                        )
            else:
                self.log(
                    f"{Fore.MAGENTA+Style.BRIGHT}[ Game Puzzle{Style.RESET_ALL}"
                    f"{Fore.YELLOW+Style.BRIGHT} Is Skipped {Style.RESET_ALL}"
                    f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                )
            time.sleep(1)

            wheels = self.load_wheel(query)
            if wheels:
                tasks = wheels['tasks']
                

                for task_name, task_data in tasks.items():
                    if task_name == "hour":
                        count = task_data['count']

                        while count < 5:
                            complete = self.task_wheel(query, task_name)
                            if complete:
                                count += 1
                                task_data['count'] = count
                                self.log(
                                    f"{Fore.MAGENTA+Style.BRIGHT}[ Task Wheel{Style.RESET_ALL}"
                                    f"{Fore.WHITE+Style.BRIGHT} Watch Ads {Style.RESET_ALL}"
                                    f"{Fore.GREEN+Style.BRIGHT}Is Completed{Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT} ]{Style.RESET_ALL}"
                                    f"{Fore.WHITE+Style.BRIGHT}[{count}/5]{Style.RESET_ALL}"
                                )
                            else:
                                break

                    elif task_name == "daily":
                        complete = self.task_wheel(query, task_name)
                        if complete:
                            self.log(
                                f"{Fore.MAGENTA+Style.BRIGHT}[ Task Wheel{Style.RESET_ALL}"
                                f"{Fore.WHITE+Style.BRIGHT} Daily {Style.RESET_ALL}"
                                f"{Fore.GREEN+Style.BRIGHT}Is Completed{Style.RESET_ALL}"
                                f"{Fore.MAGENTA+Style.BRIGHT} ]{Style.RESET_ALL}"
                            )
                        else:
                            self.log(
                                f"{Fore.MAGENTA+Style.BRIGHT}[ Task Wheel{Style.RESET_ALL}"
                                f"{Fore.WHITE+Style.BRIGHT} Daily {Style.RESET_ALL}"
                                f"{Fore.YELLOW+Style.BRIGHT}Is Already Completed{Style.RESET_ALL}"
                                f"{Fore.MAGENTA+Style.BRIGHT} ]{Style.RESET_ALL}"
                            )

                    else:
                        if not task_data:
                            complete = self.task_wheel(query, task_name)
                            if complete:
                                self.log(
                                    f"{Fore.MAGENTA+Style.BRIGHT}[ Task Wheel{Style.RESET_ALL}"
                                    f"{Fore.WHITE+Style.BRIGHT} {task_name.upper()} {Style.RESET_ALL}"
                                    f"{Fore.GREEN+Style.BRIGHT}Is Completed{Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT} ]{Style.RESET_ALL}"
                                )
                            else:
                                self.log(
                                    f"{Fore.MAGENTA+Style.BRIGHT}[ Task Wheel{Style.RESET_ALL}"
                                    f"{Fore.WHITE+Style.BRIGHT} {task_name.upper()} {Style.RESET_ALL}"
                                    f"{Fore.RED+Style.BRIGHT}Isn't Completed{Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT} ]{Style.RESET_ALL}"
                                )
                    time.sleep(1)

                get_me = self.get_me(query)
                tickets = get_me['tickets']
                balance = get_me['balance']
                self.log(
                        f"{Fore.MAGENTA + Style.BRIGHT}[ Account{Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT} {user} {Style.RESET_ALL}"
                        f"{Fore.MAGENTA+Style.BRIGHT}] [ Balance{Style.RESET_ALL}"
                        f"{Fore.WHITE+Style.BRIGHT} {balance} {Style.RESET_ALL}"
                        f"{Fore.MAGENTA+Style.BRIGHT}] [ Ticket{Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT} {tickets} {Style.RESET_ALL}"
                        f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                    )
                time.sleep(1)
                while tickets > 0:
                    self.log(
                        f"{Fore.MAGENTA + Style.BRIGHT}[ Spin Wheel{Style.RESET_ALL}"
                        f"{Fore.GREEN + Style.BRIGHT} Is Started {Style.RESET_ALL}"
                        f"{Fore.MAGENTA + Style.BRIGHT}] [ Remaining Ticket{Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT} {tickets-1} {Style.RESET_ALL}"
                        f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                    )
                    time.sleep(5)

                    spin = self.spin_wheel(query)

                    if spin:
                        trans_reward = self.transform_reward(spin['reward'])
                        self.log(
                            f"{Fore.MAGENTA + Style.BRIGHT}[ Spin Wheel{Style.RESET_ALL}"
                            f"{Fore.GREEN + Style.BRIGHT} Is Success {Style.RESET_ALL}"
                            f"{Fore.MAGENTA + Style.BRIGHT}] [ Reward{Style.RESET_ALL}"
                            f"{Fore.WHITE + Style.BRIGHT} {trans_reward} {Style.RESET_ALL}"
                            f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                        )

                        tickets = spin['tickets']
                    else:
                        self.log(
                            f"{Fore.MAGENTA + Style.BRIGHT}[ Spin Wheel{Style.RESET_ALL}"
                            f"{Fore.RED + Style.BRIGHT} Isn't Success {Style.RESET_ALL}"
                            f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                        )
                        break

                self.log(
                    f"{Fore.MAGENTA+Style.BRIGHT}[ Spin Wheel{Style.RESET_ALL}"
                    f"{Fore.YELLOW+Style.BRIGHT} No Tickets Remaining {Style.RESET_ALL}"
                    f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                )
            else:
                self.log(
                    f"{Fore.MAGENTA+Style.BRIGHT}[ Spin Wheel{Style.RESET_ALL}"
                    f"{Fore.RED+Style.BRIGHT} Is None {Style.RESET_ALL}"
                    f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                )
            time.sleep(1)

        else:
            self.log(
                f"{Fore.MAGENTA+Style.BRIGHT}[ Account{Style.RESET_ALL}"
                f"{Fore.RED+Style.BRIGHT} Is None {Style.RESET_ALL}"
                f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
            )
        time.sleep(1)

    def main(self):
        try:
            with open('query.txt', 'r') as file:
                queries = [line.strip() for line in file if line.strip()]
            with open('proxies.txt', 'r') as file:
                proxies = [line.strip() for line in file if line.strip()]

            game_puzzle, puzzle_combo = self.question()

            while True:
                self.log(
                    f"{Fore.GREEN + Style.BRIGHT}Account's Total: {Style.RESET_ALL}"
                    f"{Fore.WHITE + Style.BRIGHT}{len(queries)}{Style.RESET_ALL}"
                )
                self.log(
                    f"{Fore.GREEN + Style.BRIGHT}Proxy's Total: {Style.RESET_ALL}"
                    f"{Fore.WHITE + Style.BRIGHT}{len(proxies)}{Style.RESET_ALL}"
                )
                self.log(
                    f"{Fore.CYAN + Style.BRIGHT}-----------------------------------------------------------------------{Style.RESET_ALL}")

                for i, query in enumerate(queries):
                    query = query.strip()
                    if query:
                        self.log(
                            f"{Fore.GREEN + Style.BRIGHT}Account: {Style.RESET_ALL}"
                            f"{Fore.WHITE + Style.BRIGHT}{i + 1} / {len(queries)}{Style.RESET_ALL}"
                        )
                        if len(proxies) >= len(queries):
                            proxy = self.set_proxy(proxies[i])  # Set proxy for each account
                            self.log(
                                f"{Fore.GREEN + Style.BRIGHT}Use proxy: {Style.RESET_ALL}"
                                f"{Fore.WHITE + Style.BRIGHT}{proxy}{Style.RESET_ALL}"
                            )

                        else:
                            self.log(
                                Fore.RED + "Number of proxies is less than the number of accounts. Proxies are not used!")

                    user_info = extract_user_data(query)
                    user_id = str(user_info.get('id'))
                    self.headers = get_headers(user_id)

                    try:
                        self.process_query(query, game_puzzle, puzzle_combo)
                    except Exception as e:
                        self.log(f"{Fore.RED + Style.BRIGHT}An error process_query: {e}{Style.RESET_ALL}")

                    self.log(f"{Fore.CYAN + Style.BRIGHT}-{Style.RESET_ALL}" * 75)
                    account_delay = config['account_delay']
                    countdown_timer(random.randint(min(account_delay), max(account_delay)))

                cycle_delay = config['cycle_delay']
                countdown_timer(random.randint(min(cycle_delay), max(cycle_delay)))

        except KeyboardInterrupt:
            self.log(f"{Fore.RED + Style.BRIGHT}[ EXIT ] Agent301 - BOT.{Style.RESET_ALL}")
        except Exception as e:
            self.log(f"{Fore.RED + Style.BRIGHT}An error occurred: {e}{Style.RESET_ALL}")

if __name__ == "__main__":
    agent301 = Agent301()
    agent301.clear_terminal()
    agent301.welcome()
    agent301.main()
