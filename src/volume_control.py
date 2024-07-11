import os

def set_volume(volume):
    """
    Set system MacOS Volume

    Args:
        volume (int): value between 0 and 10
    """
    os.system(f"sudo osascript -e \"set Volume {volume}\"")
