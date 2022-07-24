import argparse as ap
import os

parser = ap.ArgumentParser(description="A little helpersoftware to manage WSL instances.",prog="wsltools")

parser.add_argument('-c','--command', help='Specifies the WSL command.', required=True)
parser.add_argument('-i','--instance', help='Specifies the WSL instance.')
args = vars(parser.parse_args())

cmd = args["command"]
inst = args["instance"]

if inst == None:
    if cmd == "kill":
        os.system("wsl --shutdown")
        print("All WSL instances were killed.")
else:
    if cmd == "kill":
        os.system(f"wsl -t {inst}")
        print(f"The WSL instance {inst} was killed")