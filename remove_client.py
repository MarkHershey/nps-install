#!/usr/bin/env python3

import shutil
import subprocess
from pathlib import Path

_HOME = Path.home()
_NPS_DIR = _HOME / ".nps_client"
_NPC_PATH = _NPS_DIR / "npc"


def is_tool(name):
    """Check whether `name` is on PATH and marked as executable."""
    return shutil.which(name) is not None


def gain_sudo_privileges():
    """Prompt for sudo password and keep it for 15 minutes"""
    cmd = "sudo -v"
    proc = subprocess.run(cmd, shell=True, stdout=subprocess.DEVNULL)
    if proc.returncode != 0:
        print("Failed to gain sudo privileges")
        return False
    return True


def stop_npc():
    if not is_tool("npc"):
        print("npc command not found. No process to stop.")
        return

    print("Stopping npc...")
    cmd = f"sudo npc stop"
    proc = subprocess.run(cmd, shell=True, stdout=subprocess.DEVNULL)
    if proc.returncode != 0:
        print("Stop npc failed")
    else:
        print("Stop npc successful")


def uninstall_npc_profile():
    if not is_tool("npc"):
        print("npc command not found. No profile to uninstall.")
        return

    print("Uninstalling npc profile...")
    cmd = f"{_NPC_PATH} uninstall"
    proc = subprocess.run(cmd, shell=True, stdout=subprocess.DEVNULL)
    if proc.returncode != 0:
        print("Uninstall npc profile failed")
    else:
        print("Uninstall npc profile successful")


def remove_npc_client():
    if not _NPS_DIR.is_dir():
        print("NPS client directory not found. Nothing to remove.")
        return

    print("Removing NPS client...")
    try:
        shutil.rmtree(_NPS_DIR)
        print("NPS client removed successfully")
    except Exception as e:
        print(f"Error while removing NPS client: {e}")


def main():
    # ask for confirmation
    print("Are you sure? (y/n)")
    answer = input()
    if answer != "y":
        print("Aborting...")
        return
    print("Removing NPS client...\n")

    if not is_tool("npc"):
        print("npc command not found. Nothing to uninstall.")
        return

    gain_sudo_privileges()
    stop_npc()
    uninstall_npc_profile()
    remove_npc_client()


if __name__ == "__main__":
    main()
