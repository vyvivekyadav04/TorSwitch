import time
from stem import Signal
from stem.control import Controller
from stem.process import launch_tor_with_config

def print_bootstrap_lines(line):
  if "Bootstrapped " in line:
    print(line)

print("Starting Tor:\n")

tor_process = launch_tor_with_config(
  config = {
    'SocksPort': '7000', # Configure this to match your desired SOCKS port
    'ControlPort': '9051',
  },
  init_msg_handler = print_bootstrap_lines,
)

print("\nTor is running")

controller = Controller.from_port(port=9051)
controller.authenticate()

try:
  while True:
    print("Sleeping for 5 minutes...")
    time.sleep(5 * 60)  # Sleep for 5 minutes
    print("Switching Tor circuit...")
    controller.signal(Signal.NEWNYM)
except KeyboardInterrupt:
  tor_process.kill()  # stops tor
