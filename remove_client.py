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
    uninstall_npc_profile()
    remove_npc_client()


if __name__ == "__main__":
    main()
