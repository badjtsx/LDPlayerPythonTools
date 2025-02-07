import subprocess

ldconsole_path = r"C:\LDPlayer\LDPlayer9\ldconsole.exe"

instance_name = "NewInstanceName"

command = [ldconsole_path, "add", "--name", instance_name]

result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
