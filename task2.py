from collections import deque


def is_palindrome(string):
    string = string.lower().replace(" ", "")
    ch_queue = deque(string)

    while len(ch_queue) > 1:
        if ch_queue.popleft() != ch_queue.pop():
            return False
    return True


test_string_1 = "qWErty YtRewQ"
if is_palindrome(test_string_1):
    print(f"Line '{test_string_1}' is a palindrome")
else:
    print(f"Line '{test_string_1}' is not a palindrome")

test_string_2 = "wireeun wdomdlr"
if is_palindrome(test_string_2):
    print(f"Line '{test_string_2}' is a palindrome")
else:
    print(f"Line '{test_string_2}' is not a palindrome")
