# NLP
Various natural language processing tools

## regex_tools.regex_sequence
Apply a specified list of regex transformations in a squential order. Used to easily remove or replace regex-found sequences from text. 

Example:

    print(regex_sequence([
        "The quick brown fox, jumps over the lazy dog.", 
        "AAaaa"], 
        steps=["lowercase", 
        ", ", 
        (r"([a-z])\1\1+", r"\1\1")]))
    >>> 0    the quick brown fox jumps over the lazy dog.
    >>> 1                                              aa

Docstring:

    Args:
        ls: input list or column of pandas dataframe,
            for example: ['Text string...    one', 'Text. string two']
        steps: list of regex replace steps. Make sure it's a list or None. (default = "default_cleanup")
            Each list element can be one of these types:
                1) string to replace identified text with " "
                2) 2-length tuple to replace text with a custom string
                3) (special case) "lowercase" to lowercase whole text
            If steps = None, no transformations will be performed.
            If steps = "default_cleanup", the defauls steps will be performed:
                1) '''[!"'#$%&()*+,-./:;<=>\[\]?@\^_`{|}~\\\]''' - remove all symbols except '
                2) " +"                       - remove repeating spaces
                3) "lowercase"                - this is a pre-defined command
                4) (r"[a-z])\1\1+", r"\1\1")  - limit repeating letters to two ('aaaaaannn' -> 'aann')
    Returns:
        Output regexed list, example: ['text*string*one','text*string*two']