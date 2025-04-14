"""
This is a sample module.
"""
 
def add(x, y):
    """
    Adds two numbers.
 
    :param x: The first number.
    :type x: int
    :param y: The second number.
    :type y: int
    :returns: The sum of x and y.
    :rtype: int
    """
    return x + y
 
 
class MyClass:
    """
    This is a sample class.
    """
 
    def __init__(self, name):
        """
        Initializes an instance of MyClass.
 
        :param name: The name of the instance.
        :type name: str
        """
        self.name = name
 
    def greet(self):
        """
        Returns a greeting.
 
        :returns: A greeting string.
        :rtype: str
        """
        return f"Hello, {self.name}!"