import re
import pandas as pd


def regex_sequence(ls, steps=["default_cleanup"]):
    r"""
    Apply a specified list of regex transformations in a squential order.
    Used to easily remove or replace regex-found sequences from text

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
                4) (r"[a-z]\1\1+", r"\1\1")  - limit repeating letters to two ('aaaaaannn' -> 'aann')
    Returns:
        Output regexed list, example: ['text*string*one','text*string*two']
    """
    if steps == ["default_cleanup"]:
        steps = [
            r"""[!"'#$%&()*+,-./:;<=>\[\]?@\^_`{|}~\\]""",
            r" +",
            r"lowercase",
            (r"([a-z])\1\1+", r"\1\1")]
    elif steps is None:
        return ls

    if ls.__class__ is not pd.core.series.Series:
        ls = pd.DataFrame({"tmp": ls})["tmp"]

    for step in steps:
        if str(step).lower() in ["lowercase"]:
            ls = ls.str.lower()
        elif step.__class__ is str:
            ls = ls.str.replace(step, " ")
        elif step.__class__ is tuple:
            # change regex, preserving ls:
            ls = pd.DataFrame(
                {"tmp": [re.sub(step[0], step[1], i) for i in ls]})["tmp"]
        else:
            print("Failed to replace ", step, ". Continuing...")
    return ls

