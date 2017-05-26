#!/usr/bin/env python
import json
import re
import subprocess
import sys

def get_block_devices():
    blkdevs_raw = subprocess.Popen(['lsblk', '--pairs'], stdout=subprocess.PIPE)
    blkdevs = blkdevs_raw.stdout.read().strip().split('\n')
    return blkdevs

def block_devices_dict(block_devices):
    devices = []
    for line in block_devices:
        device = {}
        key_value_pairs = line.split()
        for kv in key_value_pairs:
            device[kv.split('=')[0].strip('"')] = kv.split('=')[1].strip('"')
        devices.append(device)
    return devices

def select_device_type(devices, device_type):
    try:
        devices = filter(lambda device: device['TYPE'] == device_type, devices)
    except:
        devices = ''

    return devices

def main():
    devices = get_block_devices()
    devices_dict = block_devices_dict(devices)
    devices_by_type = select_device_type(devices_dict, sys.argv[1])

    discovery_output = { 'data': [] }

    output = { 'data': [{"{#DEVICE}": device['NAME']} for device in devices_by_type] }
    print json.dumps(output)

if __name__ == '__main__':
    main()
