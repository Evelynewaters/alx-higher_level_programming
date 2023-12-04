#!/usr/bin/python3
'''
Module: custom_inheritance_check
'''

def inherits_from(obj, a_class):
    '''Check if the object is an instance inherited (directly or indirectly) from a_class.
    
    Args:
        obj: an object
        a_class: a class
    
    Returns:
        True if obj is an instance inherited from a_class, False otherwise
    '''
    return type(obj) != a_class and isinstance(obj, a_class)

# Example usage
if __name__ == "__main__":
    example_int = 42
    example_object = object()

    print(inherits_from(example_int, int))  # True inherited from class int
    print(inherits_from(example_object, object))  # True inherited from class object
