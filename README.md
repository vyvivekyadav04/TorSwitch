# TorSwitch

This Python script uses the Stem library to automate the task of launching a Tor process, sleep for a specific duration, and switch the Tor circuit.

Stem is a Python controller library that allows applications to interact with the Tor process using the Tor Control Protocol.

For any updates in Tor's bootstrap process, this script prints them on the screen. On termination of the process, the script even provides you with the ability to kill the Tor process.

Here's how to use this script:

## Why another script to switch tor ?
It wasn't easy to find a script which works for Mac. This one Does.
Though, I don't love Mac/Apple a lot , but anyways.

## Pre-requisite
The script requires you to have Python and stem library installed.
If not, start by installing the prerequisite. 
For python, you can download it from official Python site: [Python](https://www.python.org/downloads/)
For Stem, use the following pip command:
```sh
pip install stem
```

## Installation

1. Clone the repo.
2. Open the file in a text editor and go through the comments to understand and configure it according to your preferences. 

##Note
To route your traffic through this proxy, go to System Preferences -> Network -> Advanced -> Proxies. Check the "SOCKS Proxy" box and enter `127.0.0.1` as the SOCKS Proxy Server and `7000` as the port.

## Usage 

1. You can choose to run the script from command line:
```sh
python filename.py
```

## Code description

Let's break down the script:

* It starts a Tor process with a specific configuration (Specified SOCKS port and Control port): 

```python
tor_process = launch_tor_with_config(
  config = {
    'SocksPort': '7000',
    'ControlPort': '9051',
  },
  init_msg_handler = print_bootstrap_lines,
)
```
* It continuously prints a line every time the script sleeps for 5 minutes:

```python
while True:
    print("Sleeping for 5 minutes...")
    time.sleep(5 * 60)
    print("Switching Tor circuit...")
    controller.signal(Signal.NEWNYM)
```
* The script handles Keyboard Interrupts and stops the Tor process when the interrupt occurs:

```python
except KeyboardInterrupt:
  tor_process.kill()
```

This makes our script an efficient Tor process handler.

Please make sure to update tests as appropriate.

## License
Code is released under the [MIT License](https://opensource.org/licenses/MIT).

## Contact 

Author: Vivek Yadav   
E-Mail: vyvivekyadav04@gmail.com

