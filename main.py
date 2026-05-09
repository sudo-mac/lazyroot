import subprocess, re


def adb_info():
    result = subprocess.run(
        "adb devices -l", shell=True, capture_output=True, text=True
    )

    unauth = re.search(r"unauthorized", result.stdout)

    if unauth:
        print("ADB debugging is currently unauthorized!")
        exit()

    get_info = re.search(
        r"(\w+)\s+device\s+.*?product:(\w+)\s+model:(\w+)\s+device:(\w+)", result.stdout
    )

    if get_info:
        serialno = get_info.group(1)
        device = get_info.group(2)
    else:
        print("No devices connected via ADB.")


def fastboot_info():
    result = subprocess.run(
        "fastboot devices -l", shell=True, capture_output=True, text=True
    )

    get_info = re.search(r"(\w+)", result.stdout)

    if get_info:
        serialno = get_info.group(1)
        device = device
        locked = locked
        unlockable = unlockable
    else:
        print("No devices connected via fastboot.")


fastboot_info()
