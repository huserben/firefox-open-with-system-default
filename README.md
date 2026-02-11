# Open in Default Browser - Firefox Extension

A simple Firefox extension that adds a context menu option to open links using your system's default browser/application handler.

## Installation

### For Personal Use (Signed)
1. Download the latest `.xpi` file from the Releases page
2. Open Firefox and go to `about:addons`
3. Click the gear icon → "Install Add-on From File..."
4. Select the downloaded `.xpi` file

### Native Messaging Host Setup

This extension requires a native messaging host to communicate with your system.

1. Create the Python script `open_default.py`:
```python
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
```

2. Make it executable:
```bash
chmod +x open_default.py
```

3. Create the native messaging manifest at `~/.mozilla/native-messaging-hosts/open_default.json`:
```json
{
  "name": "open_default",
  "description": "Open URLs in default browser",
  "path": "/full/path/to/open_default.py",
  "type": "stdio",
  "allowed_extensions": ["open-in-default@yourname.com"]
}
```

Replace `/full/path/to/open_default.py` with the actual path to your script and update the extension ID if you changed it.

## Usage

1. Right-click any link on a webpage
2. Select "Open in Default"
3. The link will open using your system's default handler

## Development

To build and sign the extension yourself:

1. Get API credentials from https://addons.mozilla.org/en-US/developers/addon/api/key/
2. Install web-ext: `npm install -g web-ext`
3. Sign the extension:
```bash
web-ext sign --api-key=YOUR_JWT_ISSUER --api-secret=YOUR_JWT_SECRET --channel=unlisted
```

## License

MIT
