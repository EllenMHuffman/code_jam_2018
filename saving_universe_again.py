

def save_universe(test_cases, *args):
    pass


def compute_damage(instructions):
    """Given a string of robot instructions, return int of damage.

    >>> compute_damage('CS')
    2
    >>> compute_damage('SCCSSC')
    9

    """

    damage = 0
    charge = 1

    for step in instructions.lower():
        if step == 'c':
            charge *= 2
        if step == 's':
            damage += charge

    return damage
