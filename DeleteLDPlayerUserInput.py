import subprocess

ldconsole_path = r"C:\LDPlayer\LDPlayer9\ldconsole.exe"

instance_name = input("Enter the name for the new instance: ")

command = [ldconsole_path, "remove", "--name", instance_name]

result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)