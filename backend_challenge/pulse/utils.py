import re

from .models import Pulse


# Matches a letter followed by an uppercase letter
split_re = re.compile(r'([a-z])([A-Z])')

# Matches one or more non-word characters
underscore_re = re.compile(r'\W+')

def header_to_field(value):
    value = split_re.sub(r'\1 \2', value)
    value = underscore_re.sub(r'_', value)
    return value.lower()

