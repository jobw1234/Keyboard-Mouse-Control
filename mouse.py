from pynput import keyboard, mouse
import threading
import time

mouse_controller = mouse.Controller()

pressed = set()
speed = 10

def ctrl_held():
    return (
        keyboard.Key.ctrl_l in pressed or
        keyboard.Key.ctrl_r in pressed
    )

def move_mouse():
    while True:
        if ctrl_held():
            dx, dy = 0, 0

            if keyboard.Key.up in pressed:
                dy -= speed
            if keyboard.Key.down in pressed:
                dy += speed
            if keyboard.Key.left in pressed:
                dx -= speed
            if keyboard.Key.right in pressed:
                dx += speed

            if dx or dy:
                mouse_controller.move(dx, dy)

        time.sleep(0.01)

def on_press(key):
    if key not in pressed:
        pressed.add(key)

        # Ctrl + Enter = left click
        if ctrl_held() and key == keyboard.Key.enter:
            mouse_controller.click(mouse.Button.left)

        # Ctrl + Shift = right click
        elif ctrl_held() and key in (
            keyboard.Key.shift,
            keyboard.Key.shift_l,
            keyboard.Key.shift_r
        ):
            mouse_controller.click(mouse.Button.right)

def on_release(key):
    pressed.discard(key)

threading.Thread(target=move_mouse, daemon=True).start()

with keyboard.Listener(
    on_press=on_press,
    on_release=on_release
) as listener:
    print("Mouse control active.")
    print("Ctrl + Arrows = Move mouse")
    print("Ctrl + Enter = Left click")
    print("Ctrl + Shift = Right click")
    listener.join()