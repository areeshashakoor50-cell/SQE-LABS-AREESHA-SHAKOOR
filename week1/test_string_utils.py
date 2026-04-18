import pytest
from string_utils import *


# count_vowels
def test_count_vowels_basic():
    assert count_vowels("hello") == 2

def test_count_vowels_uppercase():
    assert count_vowels("AEIOU") == 5

def test_count_vowels_empty():
    assert count_vowels("") == 0


# reverse_string
def test_reverse_string_basic():
    assert reverse_string("abc") == "cba"

def test_reverse_string_single():
    assert reverse_string("a") == "a"


# is_palindrome
def test_is_palindrome_simple():
    assert is_palindrome("racecar") is True

def test_is_palindrome_with_spaces():
    assert is_palindrome("A man a plan a canal Panama") is True

def test_is_palindrome_false():
    assert is_palindrome("hello") is False


# word_count
def test_word_count_basic():
    assert word_count("Hello World") == 2

def test_word_count_spaces():
    assert word_count("   hello   ") == 1


# capitalise_words
def test_capitalise_words_basic():
    assert capitalise_words("hello world") == "Hello World"


# remove_duplicates
def test_remove_duplicates_basic():
    assert remove_duplicates("aaabbbcc") == "abc"

def test_remove_duplicates_single():
    assert remove_duplicates("a") == "a"


# exception tests
def test_none_input():
    with pytest.raises(TypeError):
        count_vowels(None)