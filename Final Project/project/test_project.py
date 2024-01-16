from project import update_scores
import pytest
import warnings
warnings.filterwarnings('ignore')

def test_update_scores():
    scores = [0,0]
    assert update_scores(1,0)==print("\nComputer Score:", scores[0], "\nPlayer Score:", scores[1])
    assert update_scores(0,1)==print("\nComputer Score:", scores[0], "\nPlayer Score:", scores[1])
