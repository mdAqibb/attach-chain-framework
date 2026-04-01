import os
import json
import argparse
from attack_chain_engine import AttackChainEngine
from kill_chain_mapper import KillChainMapper
from remediation_engine import RemediationEngine
from visualizer import Visualizer


ASCII_BANNER = r"""
   ___  __  __            __      ____ _           _       
  / _ |/ /_/ /____ ____  / /__   / ___| |__   __ _(_)_ __  
 / __ / __/ __/ _ `/ _ \/  '_/  | |   | '_ \ / _` | | '_ \ 
/_/ |_\__/\__/\_,_/_//_/_/\_\   | |___| | | | (_| | | | | |
                                \____|_| |_|\__,_|_|_| |_|

Attack Chain-Driven Web Application Pentesting Framework
Author: Mohammed Aqib & Team
"""


def interactive_menu():
    print("\nChoose an option:")
    print("1. Load vulnerability file")
    print("2. Build attack chain")
    print("3. Visualize attack chain")
    print("4. Generate report")
    print("5. Exit")


def main():
    print(ASCII_BANNER)

    parser = argparse.ArgumentParser(description="Attack Chain CLI Framework")
    parser.add_argument("--input", help="Path to vulnerability JSON file")
    args = parser.parse_args()

    vulnerabilities = []
    engine = None
    chain = None

    while True:
        interactive_menu()
        choice = input("Enter choice: ")

        if choice == "1":
            path = args.input if args.input else input("Enter JSON file path: ")
            if not os.path.exists(path):
                print("File not found.")
                continue

            with open(path, "r") as f:
                vulnerabilities = json.load(f)

            print(f"[+] Loaded {len(vulnerabilities)} vulnerabilities.")
            engine = AttackChainEngine(vulnerabilities)

        elif choice == "2":
            if not engine:
                print("Load vulnerabilities first.")
                continue

            chain = engine.build_attack_chain()
            print("\n[+] Attack Chain Built:")
            print(" → ".join(chain))

        elif choice == "3":
            if not chain:
                print("Build attack chain first.")
                continue

            Visualizer.generate_graph(chain)
            print("[+] Visualization saved to output/attack_chain.png")

        elif choice == "4":
            if not chain:
                print("Build attack chain first.")
                continue

            kill_map = KillChainMapper.map_chain(chain)
            remediation = RemediationEngine.generate_remediation(chain)

            Visualizer.generate_report(chain, kill_map, remediation)
            print("[+] Report generated at output/report.md")

        elif choice == "5":
            print("Exiting framework.")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    os.makedirs("output", exist_ok=True)
    main()
