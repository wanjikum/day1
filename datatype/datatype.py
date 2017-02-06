"""Datatype assignment"""
def data_type(arg):
    """A function that returns a string based on the datatype given"""
    if isinstance(arg, str):
    	return len(arg)
    elif arg == None:
    	return "no value"
    elif isinstance(arg, bool):
    	return bool
    	

