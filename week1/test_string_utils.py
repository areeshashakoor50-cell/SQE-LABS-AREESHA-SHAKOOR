import pytest
from string_utils import (
    count_vowels,
    reverse_string,
    is_palindrome,
    word_count,
    capitalise_words,
    remove_duplicates
)

# -------------------- count_vowels --------------------

def test_count_vowels_basic():
    assert count_vowels("hello") == 2

def test_count_vowels_uppercase():
    assert count_vowels("AEIOU") == 5

def test_count_vowels_empty():
    assert count_vowels("") == 0

def test_count_vowels_none():
    with pytest.raises(TypeError):
        count_vowels(None)


# -------------------- reverse_string --------------------

def test_reverse_string_basic():
    assert reverse_string("abc") == "cba"

def test_reverse_string_single():
    assert reverse_string("a") == "a"

def test_reverse_empty():
    assert reverse_string("") == ""

def test_reverse_none():
    with pytest.raises(TypeError):
        reverse_string(None)


# -------------------- is_palindrome --------------------

def test_is_palindrome_simple():
    assert is_palindrome("racecar") is True

def test_is_palindrome_with_spaces():
    assert is_palindrome("A man a plan a canal Panama") is True

def test_is_palindrome_false():
    assert is_palindrome("hello") is False

def test_is_palindrome_none():
    with pytest.raises(TypeError):
        is_palindrome(None)


# -------------------- word_count --------------------

def test_word_count_basic():
    assert word_count("Hello world") == 2

def test_word_count_spaces():
    assert word_count("   hello   world   ") == 2

def test_word_count_empty():
    assert word_count("") == 0

def test_word_count_none():
    with pytest.raises(TypeError):
        word_count(None)


# -------------------- capitalise_words --------------------

def test_capitalise_words_basic():
    assert capitalise_words("hello world") == "Hello World"

def test_capitalise_mixed_case():
    assert capitalise_words("hELLo woRLD") == "Hello World"

def test_capitalise_empty():
    assert capitalise_words("") == ""

def test_capitalise_none():
    with pytest.raises(TypeError):
        capitalise_words(None)


# -------------------- remove_duplicates --------------------

def test_remove_duplicates_basic():
    assert remove_duplicates("aaabbbcc") == "abc"

def test_remove_duplicates_single():
    assert remove_duplicates("a") == "a"

def test_remove_duplicates_long():
    assert remove_duplicates("aaaaaa") == "a"

def test_remove_duplicates_none():
    with pytest.raises(TypeError):
        remove_duplicates(None)