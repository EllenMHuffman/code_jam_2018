

def compute_damage(instructions):
    """Given a string of robot instructions, return int of damage.

    >>> compute_damage('CS')
    2
    >>> compute_damage('SCCSSC')
    9

    """

    damage = 0
    charge = 1

    for step in instructions:
        if step.upper() == 'C':
            charge *= 2
        if step.upper() == 'S':
            damage += charge

    return damage


def swap_instructions(letters):

    rev_letters = list(letters[::-1])

    for i, letter in enumerate(rev_letters):

        if (i < len(rev_letters) - 1 and
           rev_letters[i] == 'S' and
           rev_letters[i + 1] == 'C'):
            rev_letters[i], rev_letters[i + 1] = rev_letters[i + 1], rev_letters[i]
            break

    return rev_letters[::-1]


def find_swap_counts(shield_instructions):

    swap_results = []

    for case in shield_instructions:

        impossible = False
        swap_count = 0
        damage = compute_damage(case[1])

        instructions = list(case[1])

        while damage > case[0]:

            new_instructions = swap_instructions(instructions)

            if new_instructions == instructions:
                impossible = True
                break

            damage = compute_damage(new_instructions)
            swap_count += 1

            instructions = new_instructions

        if impossible:
            swap_results.append('IMPOSSIBLE')

        else:
            swap_results.append(swap_count)

    return swap_results


def save_universe():
    """Given shield strength and robot power, print moves to disarm."""

    num = int(input())

    shield_instructions = []

    for i in range(num):
        info = input()
        shield, instructions = info.split(' ')

        shield_instructions.append((int(shield), instructions.upper()))

    results = find_swap_counts(shield_instructions)

    for i, d in enumerate(results):
        print('Case #' + str(i + 1) + ': ' + str(d))


save_universe()
