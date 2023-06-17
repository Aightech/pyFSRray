# pyHman
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This is a Python library for controlling and communicating with the FSRray device. This library provides high-level interfaces to handling data from an FSR (Force-Sensitive Resistor) array via serial port.

## Installation

This package uses setuptools for distribution. You can install it via pip:
```bash
pip install pyFSRray
```

or directly from the source code:

```bash
git clone https://github.com/Aightech/pyFSRray.git
cd pyFSRray
python setup.py install
```

### Requirements

- Python 3.6+
- **socket** (from the Python Standard Library)
- **logging** (from the Python Standard Library)


## Usage

```python
import time
from FSRray import FSRray

def callback(values, dt):
    print("dt = {}".format(dt))
    print("values = {}".format(values))

fsrray = FSRray()
fsrray.set_callback(callback)
fsrray.connect()
time.sleep(10)
fsrray.disconnect()
```

## Features and Functions

- `FSRray(width=16, verbose=False)`: This is the constructor for the FSRray class.
- `set_callback(callback)`: Sets the callback function which is invoked with the latest data from the FSR array.
- `connect(path="/dev/ttyACM0", baud=500000, timeout=3)`: Connects to the FSR array via the serial port.
- `disconnect()`: Disconnects from the FSR array.

## Contributions

Feel free to submit a pull request if you want to contribute to this project.

## License

This library is distributed under the MIT License. Please see the LICENSE file for more information.

## Support

If you have any questions or run into any problems, please open an issue in the GitHub repository.

## Disclaimer

Use this software at your own risk. The authors are not responsible for any damage that may be caused directly or indirectly through the use of this software.