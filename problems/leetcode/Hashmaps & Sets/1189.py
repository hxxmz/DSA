# 1189. Maximum Number of Balloons

def maxNumberOfBalloons(text: str) -> int:

    # Time: O(n)
    # Space: O(1)

    balloon = {'b', 'a', 'l', 'o', 'n'} # set("balloon")
    counts = {}
    for letter in text:
        if letter in balloon:
            counts[letter] = counts.get(letter, 0) + 1

    return min(
        counts.get('b', 0),
        counts.get('a', 0),
        counts.get('l', 0) // 2,
        counts.get('o', 0) // 2,
        counts.get('n', 0)
    )
    
def maxNumberOfBalloons_alt(text: str) -> int:
    counts = {'b': 0, 'a': 0, 'l': 0, 'o': 0, 'n': 0}
    
    for letter in text:
        if letter in counts:
            counts[letter] += 1

    return min(
        counts['b'],
        counts['a'],
        counts['l'] // 2,
        counts['o'] // 2,
        counts['n']
    )

print(maxNumberOfBalloons(text = "nlaebolko"))
print(maxNumberOfBalloons(text = "loonbalxballpoon"))
print(maxNumberOfBalloons(text = "leetcode"))
