# Simple and basic codes

>[!NOTE]
> You can just download these if you want. Also, this is no python library or API or anything, we're just executing the ldconsole.exe file which you can do so in your terminal.

### Create an instance

```
import subprocess

ldconsole_path = r"C:\LDPlayer\LDPlayer9\ldconsole.exe"

instance_name = "NewInstanceName"

command = [ldconsole_path, "add", "--name", instance_name]

result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
```

Of course you can set the instance name through user input. Like this:

```
import subprocess

ldconsole_path = r"C:\LDPlayer\LDPlayer9\ldconsole.exe"

instance_name = input("Enter the name for the new instance: ")

command = [ldconsole_path, "add", "--name", instance_name]

result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
```

Or like this in command line:

```
import subprocess
import argparse

parser = argparse.ArgumentParser(description="Create a new LDPlayer instance.")
parser.add_argument("--name", required=True, help="Name of the new instance")
args = parser.parse_args()

ldconsole_path = r"C:\LDPlayer\LDPlayer9\ldconsole.exe"

instance_name = args.name

command = [ldconsole_path, "add", "--name", instance_name]

result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
```

> Example command: ```python CreateLDPlayerCLI.py --name "Example Name"```

### Launch

You can launch any instance by using its name like so:

```
import subprocess

ldconsole_path = r"C:\LDPlayer\LDPlayer9\ldconsole.exe"

instance_name = "Example Name"

launch_command = [ldconsole_path, "launch", "--name", instance_name]
launch_result = subprocess.run(launch_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
```

If you have more than one instance with the same name, it will boot up the latest one. Here's the input version:

```
import subprocess

ldconsole_path = r"C:\LDPlayer\LDPlayer9\ldconsole.exe"

instance_name = input("Enter the name for the new instance: ")

launch_command = [ldconsole_path, "launch", "--name", instance_name]
launch_result = subprocess.run(launch_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
```

And the command line version:

```
import subprocess
import argparse

parser = argparse.ArgumentParser(description="Create a new LDPlayer instance.")
parser.add_argument("--name", required=True, help="Name of the new instance")
args = parser.parse_args()

ldconsole_path = r"C:\LDPlayer\LDPlayer9\ldconsole.exe"

instance_name = args.name

launch_command = [ldconsole_path, "launch", "--name", instance_name]
launch_result = subprocess.run(launch_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
```

### Delete

Deleting an instance is the same as adding it, just replace  ```add``` with ```remove```. Please keep in mind that if there are more than one instance with the same name, the lasted one will be the only one affected.

```
import subprocess

ldconsole_path = r"C:\LDPlayer\LDPlayer9\ldconsole.exe"

instance_name = "NewInstanceName"

command = [ldconsole_path, "remove", "--name", instance_name]

result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
```
User input:

```
import subprocess

ldconsole_path = r"C:\LDPlayer\LDPlayer9\ldconsole.exe"

instance_name = input("Enter the name for the new instance: ")

command = [ldconsole_path, "remove", "--name", instance_name]

result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
```

Command line:
```
import subprocess
import argparse

parser = argparse.ArgumentParser(description="Create a new LDPlayer instance.")
parser.add_argument("--name", required=True, help="Name of the new instance")
args = parser.parse_args()

ldconsole_path = r"C:\LDPlayer\LDPlayer9\ldconsole.exe"

instance_name = args.name

command = [ldconsole_path, "remove", "--name", instance_name]

result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
```

### Modifying

You can modify an instance by using its name like so:

```
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
```

There are some things that cannot be modified like this (root permissions for example), so you'll have to either do it through GUI or edit the config.ini file. Here's the list of changeable settings:

| **Parameter**       | **Description**                                                                 | **Example**                     |
|----------------------|---------------------------------------------------------------------------------|---------------------------------|
| `--name`            | Specify the name of the instance.                                              | `--name "MyInstance"`          |
| `--resolution`      | Set the screen resolution (width, height, DPI).                                | `--resolution "1920,1080,280"` |
| `--cpu`             | Set the number of CPU cores allocated to the instance.                         | `--cpu 2`                      |
| `--memory`          | Set the amount of RAM allocated to the instance (in MB).                       | `--memory 4096`                |
| `--manufacturer`    | Set the device manufacturer name.                                              | `--manufacturer "Samsung"`     |
| `--model`           | Set the device model name.                                                     | `--model "Galaxy S20"`         |
| `--pnumber`         | Set the device phone number.                                                   | `--pnumber "1234567890"`       |
| `--imei`            | Set the device IMEI number.                                                    | `--imei "123456789012345"`     |
| `--imsi`            | Set the device IMSI number.                                                    | `--imsi "123456789012345"`     |
| `--simserial`       | Set the device SIM serial number.                                              | `--simserial "123456789012345"`|
| `--androidid`       | Set the device Android ID.                                                     | `--androidid "1234567890123456"`|
| `--mac`             | Set the device MAC address.                                                    | `--mac "00:11:22:33:44:55"`    |
| `--autorotate`      | Enable or disable auto-rotation.                                               | `--autorotate 1` (enable)      |
| `--lockwindow`      | Enable or disable window lock.                                                 | `--lockwindow 0` (disable)     |
| `--audio`           | Enable or disable audio.                                                       | `--audio 1` (enable)           |
| `--fastplay`        | Enable or disable fast play mode.                                              | `--fastplay 1` (enable)        |
| `--framerate`       | Set the maximum frame rate.                                                    | `--framerate 60`               |
| `--longitude`       | Set the device longitude for GPS.                                              | `--longitude "40.7128"`        |
| `--latitude`        | Set the device latitude for GPS.                                               | `--latitude "-74.0060"`        |

---

You can also use ```ldconsole.exe``` directly in cmd or powershell like this for example: ```C:\LDPlayer\LDPlayer9\ldconsole.exe modify --name "Example Name" --cpu "4"```
