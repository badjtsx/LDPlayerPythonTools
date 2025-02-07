import subprocess

ldconsole_path = r"C:\LDPlayer\LDPlayer9\ldconsole.exe"

instance_name = input("Enter the name for the new instance: ")

launch_command = [ldconsole_path, "launch", "--name", instance_name]
launch_result = subprocess.run(launch_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)