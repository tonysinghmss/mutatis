"""
emissary.py is used for storing the details like struct, typedef, union, variables, macros, etc.
"""
import attr

@attr.s
class Emissary(object):
    """ Collection of all messages. """
    pass

@attr.s
class Message(object):
    """ Base class which will be inherited by other message classes of this module."""    
    address=attr.ib(default=None) # A tuple of(file_name, lineno)
    permitted_inclusion_vals = ["always", "never", "if_needed"]
    inclusion_policy=attr.ib(default="always", validator=attr.validators.in_(permitted_inclusion_vals))
    errors=attr.ib(factory=list)
    warnings=attr.ib(factory=list)
    

@attr.s
class StructMessage(Message):
    """Class to store struct and its details"""
    pass
