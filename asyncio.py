import asyncio
import pyshark

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

capture = pyshark.FileCapture('capture.pcapng')

for packet in capture:
    print(packet)