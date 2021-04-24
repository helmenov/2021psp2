from turtle import Turtle
import math

kame = Turtle()
N = int(input())

for k in range(N):
    kame.forward(200)
    kame.left(360 - 360 / N)


def come(x, y):
    """[summary]

    Args:
        x ([type]): [description]
        y ([type]): [description]
    """

