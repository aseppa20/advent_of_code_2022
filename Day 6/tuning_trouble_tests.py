import pytest
import tuning_trouble as tt

def test_findSequenceStart():
    assert tt.findSequenceStart("mjqjpqmgbljsphdztnvjfqwrcgsmlb") == 7

def test_findMessageStart():
    assert tt.findMessageStart("mjqjpqmgbljsphdztnvjfqwrcgsmlb") == 19
    assert tt.findMessageStart("bvwbjplbgvbhsrlpgdmjqwftvncz") == 23