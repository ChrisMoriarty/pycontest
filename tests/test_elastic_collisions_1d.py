import pytest

from pycontest import elastic_collisions as ec


# a simple tests for equal masses (balls should exchange velocities)

# using default values of m1 and m2
def test_collision_1d_1():
    v1_i = 1
    v2_i = -2
    v1_f, v2_f = ec.collision_1d(v1_i=v1_i, v2_i=v2_i)
    assert(v1_i == v2_f and v2_i == v1_f)


def test_collision_1d_2():
    v1_i = 1
    v2_i = -2
    v1_f, v2_f = ec.collision_1d(v1_i=v1_i, v2_i=v2_i, m1=1, m2=10**7)
    assert pytest.approx(v1_i == v2_f and v2_i == v1_f)