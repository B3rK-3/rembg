command_functions = []

from .b_command import b_command
from .d_command import d_command
from ..main import start
from .p_command import p_command
from .s_command import s_command

command_functions.append(b_command)
command_functions.append(d_command)
command_functions.append(start)
command_functions.append(p_command)
command_functions.append(s_command)
