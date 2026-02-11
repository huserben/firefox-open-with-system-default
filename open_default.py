#!/usr/bin/env python3
import sys
import json
import struct
import webbrowser

def get_message():
    raw_length = sys.stdin.buffer.read(4)
    if len(raw_length) == 0:
        sys.exit(0)
    message_length = struct.unpack('=I', raw_length)[0]
    message = sys.stdin.buffer.read(message_length).decode('utf-8')
    return json.loads(message)

message = get_message()
url = message.get('url')
if url:
    webbrowser.open(url)
