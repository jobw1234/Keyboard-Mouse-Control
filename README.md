# Keyboard-Mouse-Control
A lightweight Python utility that lets you control your mouse entirely with your keyboard — no external dependencies beyond pynput. Perfect for accessibility, remote sessions, or when your mouse stops working mid-task.

Python
pynput
Platform
License

✨ Features
🎯 Move the mouse using Ctrl + Arrow keys
👆 Left click with Ctrl + Enter
👉 Right click with Ctrl + Shift
⚡ ~100Hz update loop for smooth movement
🧵 Runs in a background daemon thread — non-blocking
🪶 Single-file, zero-config, plug-and-play
📦 Requirements
Python 3.7 or higher
pynput library
🚀 Installation
1. Clone the repository
bash

git clone [https://github.com/YOUR_USERNAME/keyboard-mouse-control.git](https://github.com/jobw1234/Keyboard-Mouse-Control)
cd keyboard-mouse-control
2. Install dependencies
bash

pip install pynput

🎮 Usage
Run the script:

bash

python mouse_control.py
You'll see:

text

Mouse control active.
Ctrl + Arrows = Move mouse
Ctrl + Enter = Left click
Ctrl + Shift = Right click
The script runs continuously in the foreground. Press Ctrl + C in the terminal to stop it.

⌨️ Controls
Action
Shortcut
Move mouse up	Ctrl + ↑
Move mouse down	Ctrl + ↓
Move mouse left	Ctrl + ←
Move mouse right	Ctrl + →
Left click	Ctrl + Enter
Right click	Ctrl + Shift

💡 You can hold multiple arrow keys simultaneously to move diagonally.

⚙️ Configuration
You can tweak the mouse movement speed by editing the speed variable at the top of the script:

python

speed = 10  # Increase for faster, decrease for slower movement
You can also adjust the update interval in the move_mouse() function:

python

time.sleep(0.01)  # 10ms = ~100 updates per second
🛠️ How It Works
The script uses two concurrent mechanisms:

Background thread (move_mouse) — Polls the set of currently-pressed keys every 10ms. If Ctrl is held along with any arrow key, it moves the mouse by speed pixels in the corresponding direction.
Keyboard listener (pynput.keyboard.Listener) — Records key press/release events into a set, enabling stateful detection of chord combinations (e.g., Ctrl + Enter). Click actions are triggered on key press for responsiveness.
The combination of these two allows both continuous movement (held keys) and discrete clicks (single press events).

🐛 Troubleshooting
Linux
On some Linux distributions, you may need to run with sudo for pynput to capture keyboard events globally:

bash

sudo python mouse_control.py
Alternatively, ensure your user is in the input group:

bash

sudo usermod -aG input $USER
Then log out and back in.

macOS
macOS may prompt you to grant Accessibility permissions to your terminal or IDE. Go to:

System Settings → Privacy & Security → Accessibility → Add your terminal/Python

Windows
Should work out of the box. If the script doesn't capture input, try running your terminal as Administrator.

📁 Project Structure
text

keyboard-mouse-control/
│
├── mouse_control.py      # Main script
├── README.md             # This file
└── LICENSE               # MIT License

pynput>=1.7.6
🤝 Contributing
Contributions are welcome! Ideas for improvement:

Adjustable speed via hotkeys (Ctrl + + / Ctrl + -)
Drag-and-drop support (hold to keep button pressed)
Scroll wheel emulation (Ctrl + Page Up / Page Down)
Config file for custom keybindings
System tray icon
Fork the repo
Create a branch (git checkout -b feature/your-feature)
Commit your changes (git commit -m 'Add your feature')
Push (git push origin feature/your-feature)
Open a Pull Request
📜 License
This project is licensed under the MIT License — see the LICENSE file for details.

⚠️ Disclaimer
This tool captures global keyboard input. Use it responsibly and only on systems you own or have permission to control. The author is not responsible for any misuse.

