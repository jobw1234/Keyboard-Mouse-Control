

```markdown
<div align="center">

# ⌨️ Keyboard-Mouse-Control

**Control your mouse entirely with your keyboard.**

A lightweight, zero-config Python utility that transforms keyboard input into precise mouse movements and clicks. Built for accessibility, remote sessions, or those moments your mouse dies mid-task.

[![Python 3.7+](https://img.shields.io/badge/python-3.7%2B-blue.svg)](https://www.python.org/downloads/)
[![pynput](https://img.shields.io/badge/pynput-1.7.6%2B-green.svg)](https://pypi.org/project/pynput/)
[![License: MIT](https://img.shields.io/badge/license-MIT-yellow.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg)]()

[Features](#-features) · [Installation](#-installation) · [Usage](#-usage) · [Controls](#-controls) · [Configuration](#-configuration) · [Troubleshooting](#-troubleshooting)

</div>

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🎯 **Smooth Movement** | Move the cursor using `Ctrl` + `Arrow Keys` |
| 👆 **Left Click** | Trigger with `Ctrl` + `Enter` |
| 👉 **Right Click** | Trigger with `Ctrl` + `Shift` |
| ⚡ **~100Hz Update Loop** | Butter-smooth cursor movement |
| 🧵 **Non-Blocking** | Runs in a background daemon thread |
| 🪶 **Single File** | Zero-config, plug-and-play |
| 🌐 **Cross-Platform** | Works on Windows, macOS, and Linux |

---

## 📦 Requirements

- **Python 3.7** or higher
- **[pynput](https://pypi.org/project/pynput/)** library (`>=1.7.6`)

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/jobw1234/Keyboard-Mouse-Control.git
cd Keyboard-Mouse-Control
```

### 2. Install dependencies

```bash
pip install pynput
```

---

## 🎮 Usage

Run the script:

```bash
python mouse_control.py
```

You'll see the following output:

```
Mouse control active.
Ctrl + Arrows = Move mouse
Ctrl + Enter  = Left click
Ctrl + Shift  = Right click
```

> The script runs continuously in the foreground. Press **`Ctrl + C`** in the terminal to stop it.

---

## ⌨️ Controls

| Action | Shortcut |
|:-------|:---------|
| Move mouse up | `Ctrl` + `↑` |
| Move mouse down | `Ctrl` + `↓` |
| Move mouse left | `Ctrl` + `←` |
| Move mouse right | `Ctrl` + `→` |
| Left click | `Ctrl` + `Enter` |
| Right click | `Ctrl` + `Shift` |

> 💡 **Tip:** Hold multiple arrow keys simultaneously to move diagonally.

---

## ⚙️ Configuration

### Movement Speed

Adjust the `speed` variable at the top of the script:

```python
speed = 10  # Increase for faster, decrease for slower movement
```

### Update Interval

Fine-tune the polling rate inside the `move_mouse()` function:

```python
time.sleep(0.01)  # 10ms ≈ 100 updates per second
```

---

## 🛠️ How It Works

The script relies on **two concurrent mechanisms** working in tandem:

```
┌─────────────────────────────────────────────────┐
│                 Main Thread                      │
│  ┌───────────────────────────────────────────┐  │
│  │  pynput.keyboard.Listener                 │  │
│  │  ├─ on_press()  → Add key to pressed set  │  │
│  │  └─ on_release() → Remove key from set    │  │
│  │                                           │  │
│  │  Triggers discrete actions (clicks) on    │  │
│  │  key press for instant responsiveness.    │  │
│  └───────────────────────────────────────────┘  │
│                      │                          │
│              shared set: pressed_keys           │
│                      │                          │
│  ┌───────────────────────────────────────────┐  │
│  │  Background Daemon Thread (move_mouse)     │  │
│  │                                           │  │
│  │  Every 10ms:                              │  │
│  │  ├─ Check if Ctrl + Arrow is held         │  │
│  │  └─ Move cursor by `speed` pixels         │  │
│  │                                           │  │
│  │  Enables continuous, smooth movement.     │  │
│  └───────────────────────────────────────────┘  │
└─────────────────────────────────────────────────┘
```

- **Background thread (`move_mouse`)** — Polls the set of currently-pressed keys every 10 ms. If `Ctrl` is held alongside any arrow key, it moves the mouse by `speed` pixels in the corresponding direction.
- **Keyboard listener (`pynput.keyboard.Listener`)** — Records key press/release events into a shared set, enabling stateful detection of chord combinations (e.g., `Ctrl` + `Enter`). Click actions fire on key press for immediate responsiveness.

This combination enables both **continuous movement** (held keys) and **discrete clicks** (single press events).

---

## 🐛 Troubleshooting

### Linux

On some distributions, `pynput` needs elevated privileges to capture global keyboard events:

```bash
# Option 1: Run with sudo
sudo python mouse_control.py

# Option 2: Add your user to the input group
sudo usermod -aG input $USER
# Then log out and back in
```

### macOS

macOS will prompt you to grant **Accessibility** permissions to your terminal or IDE:

> **System Settings** → **Privacy & Security** → **Accessibility** → **Add your terminal / Python**

### Windows

Should work out of the box. If input capture fails, try running your terminal **as Administrator**.

---

## 📁 Project Structure

```
keyboard-mouse-control/
│
├── mouse_control.py      # Main script
├── README.md             # This file
└── LICENSE               # MIT License
```

---

## 🤝 Contributing

Contributions are welcome! Here are some ideas to get started:

- [ ] Adjustable speed via hotkeys (`Ctrl` + `+` / `Ctrl` + `-`)
- [ ] Drag-and-drop support (hold to keep button pressed)
- [ ] Scroll wheel emulation (`Ctrl` + `Page Up` / `Page Down`)
- [ ] Config file for custom keybindings
- [ ] System tray icon

### Steps

1. **Fork** the repository
2. Create a feature branch — `git checkout -b feature/your-feature`
3. Commit your changes — `git commit -m 'Add your feature'`
4. Push to the branch — `git push origin feature/your-feature`
5. Open a **Pull Request**

---

## 📜 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

## ⚠️ Disclaimer

> This tool captures **global keyboard input**. Use it responsibly and only on systems you own or have explicit permission to control. The author is not responsible for any misuse.
```

**Key improvements made:**

- **Centered header** with badge row and quick-nav links
- **Feature table** instead of a flat list — easier to scan
- **ASCII architecture diagram** in "How It Works" — instantly communicates the dual-thread design
- **Proper code fences** with language tags on every block
- **Consistent heading hierarchy** (H2 → H3, never skipping levels)
- **Blockquotes** for tips and disclaimers to visually separate them
- **Checkbox-style** contribution ideas for a modern feel
- **Removed duplicated content** (your prompt had the full text pasted twice)
- **Clean horizontal rules** to separate major sections
- **Fixed the clone URL** to match your actual repo (`jobw1234/Keyboard-Mouse-Control`)
