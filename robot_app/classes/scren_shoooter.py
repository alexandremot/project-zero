import os
import subprocess

class ScreenShooter:
    def __init__(self, save_path=None, device_id=None):
        if save_path is None:
            os.makedirs("screenshots", exist_ok=True)
            save_path = os.path.join("screenshots", "screenshot.png")
        self.save_path = save_path
        self.device_id = device_id

    def take_screenshot(self, remote_path="/sdcard/screenshot.png"):
        adb_cmd = ["adb"]
        if self.device_id:
            adb_cmd += ["-s", self.device_id]
        try:
            result = subprocess.run(
                adb_cmd + ["shell", "screencap", "-p", remote_path],
                check=True, capture_output=True, text=True
            )
        except subprocess.CalledProcessError as e:
            print("Erro ao capturar screenshot:", e.stderr)
            raise
        subprocess.run(adb_cmd + ["pull", remote_path, self.save_path], check=True)
        subprocess.run(adb_cmd + ["shell", "rm", remote_path], check=True)
        return self.save_path
