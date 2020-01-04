

import subprocess
import arabic_reshaper
from bidi.algorithm import get_display


def to_arabic(t):
    t_reshaped = arabic_reshaper.reshape(t)
    t_display = get_display(t_reshaped)
    return t_display