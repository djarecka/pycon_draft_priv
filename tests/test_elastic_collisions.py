from pycontest import elastic_collisions as ec
from pycontest import simulation_2d_many as sim2d
from pycontest.movies import Movie_2d
from pycontest.utils import momentum, E_kin

import numpy as np
import pytest

def test_tmp():
    assert 2 == 1+1

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


def test_collision_1d_en():
    v1_i, v2_i = 1, -2
    m1, m2 = 1, 3
    v1_f, v2_f = ec.collision_1d(v1_i, v2_i, m1, m2)
    assert E_kin([v1_i, v2_i], [m1, m2]) == E_kin([v1_f, v2_f], [m1, m2])

def test_collision_1d_mom():
    v1_i, v2_i = 1, -2
    m1, m2 = 1, 3
    v1_f, v2_f = ec.collision_1d(v1_i, v2_i, m1, m2)
    assert momentum([v1_i, v2_i], [m1, m2]) == momentum([v1_f, v2_f], [m1, m2])



def test_collision_2d_1():
    v1_f, v2_f = ec.collision_2d(v1=[1, 0], v2=[-2, 0], r12=[1, 0], m1=1, m2=1)
    assert (v1_f == [-2, 0]).all()
    assert (v2_f == [1, 0]).all()


def test_collision_2d_2():
    v1_f, v2_f = ec.collision_2d(v1=[0, 1], v2=[0, -2], r12=[0, 1], m1=1, m2=1)
    assert (v1_f == [0, -2]).all()
    assert (v2_f == [0, 1]).all()


def test_collision_2d_3():
    v1_f, v2_f = ec.collision_2d(v1=[0, 1], v2=[0, -2], r12=[1, 0], m1=1, m2=1)
    assert (v1_f == [0, 1]).all()
    assert (v2_f == [0, -2]).all()
