# NLP
Various natural language processing tools

## regex_tools.regex_sequence
Apply a specified list of regex transformations in a squential order. Used to easily remove or replace regex-found sequences from text. 

Example:

    in_texts = [
        "The quick brown fox, jumps over the lazy dog.",
        "AAaaa"]
        
    steps = [
        "lowercase",
        ", ",
        (r"([a-z])\1\1+",
        r"\1\1")]
        
    print(regex_sequence(in_texts, steps=steps))
    
    >>> 0    the quick brown fox jumps over the lazy dog.
    >>> 1                                              aa

        
## regex_tools.regex_around
Extract specified number of characters around a specified string

Example:

        regex_around("The quick brown fox jumps over the lazy dog", "fox", 10)
        
        >>> ['ick brown fox jumps ove']