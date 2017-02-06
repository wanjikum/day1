"""Datatype assignment"""
def data_type(arg):
    """A function that returns a string based on the datatype given"""
    if isinstance(arg, str):
        return len(arg)
    elif arg == None:
        return "no value"
    elif isinstance(arg, bool):
        return arg
    elif isinstance(arg, int):
        if arg < 100:
            return 'less than 100'
        elif arg > 100:
            return 'more than 100'
        else:
            return 'equal to 100'
    else:
        if isinstance(arg, list):
            if len(arg) <= 2:
                return None
            else:
                return arg[2]




