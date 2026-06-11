import time
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

FOLDER = r"C:\Users\rayra\OneDrive\Desktop\learning python"

class Handler(FileSystemEventHandler):
    def on_any_event(self, event):
        if event.is_directory:
            return

        print("Change detected")

        subprocess.run(["git", "add", "."], cwd=FOLDER)
        subprocess.run(["git", "commit", "-m", "Auto update"], cwd=FOLDER)
        subprocess.run(["git", "push"], cwd=FOLDER)

observer = Observer()
observer.schedule(Handler(), FOLDER, recursive=True)
observer.start()

print("Watching folder...")

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()

observer.join()