#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Standalone helper program to print out IP addresses from a file passed as command line argument.

Pass the following Args at runtime:
1: filename
eg. ip_print ../examples/input1.json
    ip_print ../examples/input2.json
    ip_print ../examples/empty.json
"""

import sys
import os
import json
import logging
from json.decoder import JSONDecodeError

def get_file_format(filename):
    '''
    Get the file format from filename.
    '''
    lower_filename = filename.lower()
    format = os.path.splitext(filename)[1]
    return format[1:]

class PrintIp(object):
    def __init__(self, filename: str):
        self.filename = filename

    @staticmethod
    def log_err(exception):
        print("Exception: {}".format(type(exception).__name__))

        if 'JSONDecodeError' in type(exception).__name__:
            print("Exception message: {}".format('Json file content validation failed.'))
        else:
            print("Exception message: {}".format(exception))


    def print_ip(self):
        if self.filename:
            try:
                file_format = get_file_format(self.filename)
                if file_format != 'json':
                    raise TypeError("Input cli argument is a not valid json file.")
                with open(self.filename, 'r') as f:
                    jsonData = json.load(f)

                    if 'vm_private_ips' not in jsonData:
                        raise ValueError("Input json don't have ip address.")
                    private_ips = jsonData['vm_private_ips']['value']

                    network = None
                    if 'network' in jsonData:
                        network = jsonData['network']['vms']

                    for name,vm_ip in private_ips.items():
                        access_ipv4 = ''
                        if network != None:
                            for value in network:
                                if value['attributes']['name'] == name:
                                    access_ipv4 = value['attributes']['access_ip_v4']
                        print(vm_ip, '', access_ipv4)
                return 0


            except (TypeError, ValueError, FileNotFoundError) as err:
                self.log_err(err)
                return 1
            except Exception as exception:
                self.log_err(exception)
                return 1

def main():
    if len(sys.argv) == 2:
        filename = str(sys.argv[1])
    else:
        filename = input("Enter json file name: ")
    print_ip = PrintIp(filename)
    sys.exit(print_ip.print_ip())

if __name__ == '__main__':
    main()
