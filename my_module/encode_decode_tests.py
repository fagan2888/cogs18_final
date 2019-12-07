import pytest
import encoding as encode

from string import ascii_lowercase

def test_encoding():
    ''' Tests for the 3 original encoding methods. '''
    assert encode.reverse_encode("hello") == 'olleh'
    assert encode.shift_encode("hello", 4) == 'lipps'
    assert encode.fancy_encode("hello") == 'sppil'

def attempt_decoding():
    ''' Tests for the decoding method. '''
    assert 'hello' in encode.decode_attempt('lipps', ''.join(str(v) for v in [i for i in ascii_lowercase]))