import os
import subprocess

print("🤖 File Manager AI Ready")
print("Type: open downloads | open desktop | list files | exit")

while True:
    command = input("\nYou: ").lower()

    if command == "exit":
        print("Goodbye 👋")
        break

    elif "open downloads" in command:
        os.startfile(os.path.expanduser("~/Downloads"))

    elif "open desktop" in command:
        os.startfile(os.path.expanduser("~/Desktop"))

    elif "list files" in command:
        files = os.listdir(".")
        for f in files:
            print("📄", f)

    elif "open notepad" in command:
        subprocess.Popen(["notepad.exe"])

    else:
        print("❌ Command samajh nahi aayi")
