import time
import random
import ctypes
import win32api
import hashlib


def generate_seed():
    current_time = int(time.time() * 1000)
    print(f"Current time: {current_time}")

    mouse_x, mouse_y = win32api.GetCursorPos()
    print(f"Current mouse position: ({mouse_x}, {mouse_y})")

    volume_serial = ctypes.c_ulong()
    ctypes.windll.kernel32.GetVolumeInformationW("C:\\", None, 0, ctypes.pointer(volume_serial), None, None, None, 0)
    cpu_serial = volume_serial.value
    print(f"Serial CPU number: {cpu_serial}")

    seed = current_time ^ mouse_x ^ mouse_y ^ cpu_serial
    seed_bytes = str(seed).encode("utf-8")
    hashed_seed = hashlib.sha384(seed_bytes).hexdigest()
    print(f"Hashed seed: {hashed_seed}\n")

    return hashed_seed


seed = generate_seed()
random.seed(seed)
random_number = random.randint(1, 100)

print(f"Number: {random_number}")
