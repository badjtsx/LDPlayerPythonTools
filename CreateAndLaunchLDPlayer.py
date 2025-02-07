import subprocess

# Path to LDPlayer's ldconsole.exe
ldconsole_path = r"C:\LDPlayer\LDPlayer9\ldconsole.exe"

instance_name = "NewInstanceName"

create_command = [ldconsole_path, "add", "--name", instance_name]
create_result = subprocess.run(create_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

launch_command = [ldconsole_path, "launch", "--name", instance_name]
launch_result = subprocess.run(launch_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)