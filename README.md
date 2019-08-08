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

## dictionary_tools.sc_correct_dictionary
Iterate over each word in dictionary (for example created by sklearn CountVectorizer) 
and correct each of the words assigning the same ID for all words which got 
corrected to the same word.

Returns two outputs - one with numerical ids for all words where correct and 
misspeled words share same id, and one where each word has its correction listed

Can use these outputs

Example:
    
    from sklearn.feature_extraction.text import CountVectorizer
    sentence = "Yoou cannot end a sentence with becausse becuse becaus is a conjunction.".lower()
    cv = CountVectorizer().fit([sentence])
    remap, corrections = sc_correct_dictionary(cv.vocabulary_)
    for key in corrections.keys():
        sentence = sentence.replace(" " + key + " ", " " + corrections[key] + " ")
        
    print(cv.vocabulary_)
    print(remap, corrections)
    print(sentence)
    
    >>> {'yoou': 9, 'cannot': 3, 'end': 5, 'sentence': 7, 'with': 8, 
        'becausse': 1, 'becuse': 2, 'becaus': 0, 
        'is': 6, 'conjunction': 4}
        
    >>> {'yoou': 0, 'cannot': 1, 'end': 2, 'sentence': 3, 'with': 4, 
        'becausse': 5, 'becuse': 5, 'becaus': 5, 
        'is': 6, 'conjunction': 7}
        
    >>>{'yoou': 'you', 
        'cannot': 'cannon', 
        'end': 'end',
        'sentence': 'sentence',
        'with': 'with', 
        'becausse': 'because', 
        'becuse': 'because', 
        'becaus': 'because', 
        'is': 'is', 
        'conjunction': 'conjunction'}
        
    >>> yoou cannon end a sentence with because because because is a conjunction.
