from pycontest import elastic_collisions as ec
from pycontest import simulation_2d_many as sim2d
from pycontest.movies import Movie_2d
from pycontest.utils import momentum, E_kin

import numpy as np
import pytest


# simple pytest examples
def test_collision_1d_1():
    v1_f, v2_f = ec.collision_1d(v1_i=1, v2_i=-2)
    assert v1_f == -2
    assert v2_f == 1

def test_collision_1d_2():
    v1_f, v2_f = ec.collision_1d(v1_i=1, v2_i=-2, m1=2, m2=2)
    assert v1_f == -2
    assert v2_f == 1

def test_collision_1d_3():
    v1_f, v2_f = ec.collision_1d(v1_i=1, v2_i=-2, m1=1, m2=1e6)
    assert v2_f == pytest.approx(-2, rel=1e-3)

