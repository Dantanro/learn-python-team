"""IF statement

@see: https://docs.python.org/3/tutorial/controlflow.html

There can be zero or more elif parts, and the else part is optional. The keyword ‘elif’ is
short for ‘else if’, and is useful to avoid excessive indentation.

An if … elif … elif … sequence is a substitute for the switch or case statements found
in other languages.
"""


def test_if_statement():
    """IF statement"""

    number = 15
    conclusion = ''

    if number < 0:
        conclusion = 'Number is less than zero'
    elif number == 0:
        conclusion = 'Number equals to zero'
    elif number < 1:
        conclusion = 'Number is greater than zero but less than one'
    else:
        conclusion = 'Number bigger than or equal to one'

    assert conclusion == 'Number bigger than or equal to one'


def test_if_multiple_elif_branches():
    """IF statement with multiple ELIF branches

    Conditions are checked from top to bottom and only the first branch whose condition is
    true runs. That is why the order of the elif branches matters.
    """

    def get_grade(score):
        # Check the highest range first so each elif only needs a lower bound.
        if score >= 90:
            return 'A'
        elif score >= 80:
            return 'B'
        elif score >= 70:
            return 'C'
        elif score >= 60:
            return 'D'
        else:
            return 'F'

    # A score in the middle of each range picks that range's letter.
    assert get_grade(95) == 'A'
    assert get_grade(85) == 'B'
    assert get_grade(75) == 'C'
    assert get_grade(65) == 'D'
    assert get_grade(40) == 'F'

    # A score exactly on a boundary belongs to the higher grade, because >= is used.
    assert get_grade(90) == 'A'
    assert get_grade(60) == 'D'

    # A score just below a boundary falls through to the next branch.
    assert get_grade(89) == 'B'
    assert get_grade(59) == 'F'
