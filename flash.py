from main import Device

dev = Device()


def flash():
    if dev.device == "flame":
        print("\nFlashing...")
        subprocess.run(
            ["./install.sh"],
            cwd="/run/media/dex/e-Garage/Android/Pixel4/OEM-A13-Magisk/",
            capture_output=True,
            text=True,
        )
