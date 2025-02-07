import subprocess

ldconsole_path = r"C:\LDPlayer\LDPlayer9\ldconsole.exe"

instance_name = "Example Name"

modify_command = [
    ldconsole_path, "modify", "--name", instance_name,
    "--resolution", "1920,1080,280",
    "--cpu", "2",
    "--memory", "4096"
]
subprocess.run(modify_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)