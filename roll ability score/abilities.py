"""
Outputs all possible rolls for ability scores. Paste the output of this into a
slackbot response for easy character rolling.
"""

rolls = []
for r1 in range(1, 7):
    for r2 in range(1, 7):
        for r3 in range(1, 7):
            for r4 in range(1, 7):
                rolls.append((r1, r2, r3, r4))

for x in rolls:
    lowest = min(x)

    remaining = list(x)
    remaining.remove(lowest)

    s = sum(remaining)

    print 'Rolled %s, dropping %d; score: %d' % (', '.join(map(str, x)), lowest, s)
