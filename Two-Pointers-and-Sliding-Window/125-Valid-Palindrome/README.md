# Valid Palindrome

## Intuition

A palindrome reads the same from both sides.

I use two pointers:

* `left` starts from the beginning.
* `right` starts from the end.

I ignore non-alphanumeric characters and compare the characters from both sides.

If any two characters are different, the string is not a palindrome.

## Approach

1. Convert the string to lowercase using `lower()`.
2. Set `left` to `0` and `right` to the last index.
3. Move `left` forward if the character is not alphanumeric.
4. Move `right` backward if the character is not alphanumeric.
5. Compare the characters at `left` and `right`.
6. If they are different, return `False`.
7. Otherwise, move both pointers toward the center.
8. If all characters match, return `True`.

## Complexity

* Time complexity: **O(n)**
* Space complexity: **O(1)**

## Code

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()

        left = 0
        right = len(s) - 1

        while left < right:

            if not s[left].isalnum():
                left += 1
                continue

            if not s[right].isalnum():
                right -= 1
                continue

            if s[left] != s[right]:
                return False

            left += 1
            right -= 1

        return True
```
