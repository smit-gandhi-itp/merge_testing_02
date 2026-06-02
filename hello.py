"""Simple hello world module."""


def greet(name=None):
    """Greet a person by name.
    
    Args:
        name: Name of the person to greet. If None, uses 'World'
        
    Returns:
        Greeting string
    """
    if name is None:
        name = "World"
    return f"Hello, {name}!"


def greet_multiple(names):
    """Greet multiple people.
    
    Args:
        names: List of names to greet
        
    Returns:
        List of greeting strings
    """
    return [greet(name) for name in names]


def farewell(name=None):
    """Say goodbye to a person.
    
    Args:
        name: Name of the person. If None, uses 'World'
        
    Returns:
        Farewell string
    """
    if name is None:
        name = "World"
    return f"Goodbye, {name}!"


if __name__ == "__main__":
    # Example usage
    print(greet())
    print(greet("Alice"))
    print(greet("Bob"))
    print()
    print("Multiple greetings:")
    for greeting in greet_multiple(["Alice", "Bob", "Charlie"]):
        print(greeting)
    print()
    print(farewell("Alice"))
