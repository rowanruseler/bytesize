"""Return human-readable size

This module can take a number of bytes and returns a human-readable string
with the size in it, in kibibyte (KiB), mebibyte (MiB), etc.
"""

__author__ = 'Rowan Ruseler <rowanruseler@gmail.com>'
__version__ = '1.1'


def bytesize(bytes):
    # binary prefix
    prefix = [
        (1024 ** 5.0, 'PiB'),
        (1024 ** 4.0, 'TiB'),
        (1024 ** 3.0, 'GiB'),
        (1024 ** 2.0, 'MiB'),
        (1024 ** 1.0, 'KiB'),
        (1024 ** 0.0, 'B'),
    ]
    for factor, symbol in prefix:
        if bytes >= factor:
            break
    amount = round(float(bytes/factor), 2)
    return '{0}{1}'.format(amount, symbol)
