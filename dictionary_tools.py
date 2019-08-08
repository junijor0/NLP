import pandas as pd
from spellchecker import SpellChecker
sc = SpellChecker()


def sc_correct_dictionary(dictionary):
    """
    Correct input dictionary using SpellChecker.

    Args:
        dictionary: input dictionary
    Returns:
        1) corrected dictionary where each word and its corrected spelling errors have the same IDs
        2) corrections dictionary
    """
    in_df = pd.DataFrame(list(dictionary.items()), columns=["Word", "ID"])

    # find those words that may be misspelled
    misspelled = sc.unknown(in_df["Word"])
    corrections = pd.DataFrame()

    for n, word in enumerate(misspelled):
        corrections = corrections.append({
            "Error": word,
            "Correction": sc.correction(word[0:30])},
            ignore_index=True)
        if n % 10 == 0:
            print("Corrected", n, "/", len(misspelled))

    # list of corrected Dictionary IDs:
    corr = in_df.merge(corrections, left_on="Word", right_on="Error", how="left")
    corr.loc[corr['Correction'].isna(), 'Correction'] = \
        corr.loc[corr['Correction'].isna(), 'Word']

    factors = pd.factorize(corr['Correction'])
    dict_out = {in_df.at[i, "Word"]: factors[0][i]
                for i in range(len(in_df))}
    # corrections_out = {in_df.at[i, "Word"]: factors[1][factors[0][i]]
    #                    for i in range(len(in_df))}
    corrections_out = {i[0]: i[1] for i in corr.loc[corr["Word"] !=
                       corr["Correction"], :][["Word", "Correction"]].values}
    return dict_out, corrections_out
