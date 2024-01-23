#!/usr/bin/env python3
import os
def reboot_check():
    print(os.path.exists("/run/reboot-required"))

reboot_check()
