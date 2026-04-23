"""
Topic 12: Regular Expressions
=============================
Covers: re.search, re.findall, re.sub, groups, character classes
"""
import re

# ─────────────────────────────────────────
# 1. re.search(): Finding the first match
# ─────────────────────────────────────────
text = "My phone number is 123-456-7890."
if match := re.search(r"\d{3}-\d{3}-\d{4}", text):
    print(f"Found phone number: {match[0]}")
else:
    print("No phone number found.")

# ─────────────────────────────────────────
# 2. re.findall(): Finding all matches
# ─────────────────────────────────────────
text_with_emails = "Contact us at support@example.com or sales@example.com."
emails = re.findall(r"[\w\.-]+@[\w\.-]+", text_with_emails)
print(f"Found emails: {emails}")

# ─────────────────────────────────────────
# 3. re.sub(): Substituting text
# ─────────────────────────────────────────
text_to_censor = "The quick brown fox jumps over the lazy dog."
censored_text = re.sub(r"fox|dog", "animal", text_to_censor)
print(f"Censored text: {censored_text}")

# ─────────────────────────────────────────
# 4. Groups: Capturing specific parts of a match
# ─────────────────────────────────────────
date_text = "Today's date is 2023-10-27."
if date_match := re.search(r"(\d{4})-(\d{2})-(\d{2})", date_text):
    year = date_match[1]
    month = date_match[2]
    day = date_match[3]
    print(f"Year: {year}, Month: {month}, Day: {day}")

# ─────────────────────────────────────────
# 5. Character Classes and Quantifiers
# ─────────────────────────────────────────
# \d - digit
# \w - word character (letters, numbers, underscore)
# \s - whitespace
# . - any character except newline
#
# + - one or more
# * - zero or more
# ? - zero or one
# {n} - exactly n times
# {n,m} - between n and m times

text_with_various_data = "user_id: 123, name: John Doe, age: 30"
# Find all words (sequences of word characters)
words = re.findall(r"\w+", text_with_various_data)
print(f"All words: {words}")

# Find all numbers (sequences of digits)
numbers = re.findall(r"\d+", text_with_various_data)
print(f"All numbers: {numbers}")