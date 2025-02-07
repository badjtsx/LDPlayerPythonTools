import subprocess
import argparse

parser = argparse.ArgumentParser(description="Create a new LDPlayer instance.")
parser.add_argument("--name", required=True, help="Name of the new instance")
args = parser.parse_args()

ldconsole_path = r"C:\LDPlayer\LDPlayer9\ldconsole.exe"

instance_name = args.name

launch_command = [ldconsole_path, "launch", "--name", instance_name]
launch_result = subprocess.run(launch_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)