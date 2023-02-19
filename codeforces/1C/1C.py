# https://codeforces.com/problemset/problem/1/C

import math


def inverted_slope(slope):
    if slope is None:
        return 0
    if slope == 0:
        return None
    return -1 / slope


def mid_bis_slope(x1, y1, x2, y2):
    slope = None if (x2 - x1) == 0 else (y2 - y1) / (x2 - x1)
    return (x1 + x2) / 2, (y1 + y2) / 2, inverted_slope(slope)


def distance(x1, y1, x2, y2):
    return math.sqrt((y2 - y1) ** 2 + (x2 - x1) ** 2)


def calc_angle(ax, ay, bx, by, cx, cy):
    c = distance(ax, ay, bx, by)
    b = distance(ax, ay, cx, cy)
    a = distance(bx, by, cx, cy)
    cos_angle = (a * a + c * c - b * b) / (2 * a * c)
    if cos_angle > 1.0:
        cos_angle = 1.0
    elif cos_angle < -1.0:
        cos_angle = -1.0
    radians = math.acos(cos_angle)
    angle = math.degrees(radians)
    return angle


def gcd(a, b, c):
    ret_angle, mina, minb, minc = None, a, b, c
    for pillars in range(3, 101):
        angle = (360 / pillars)
        tma = min(abs(0 - a % angle), abs(angle - a % angle))
        tmb = min(abs(0 - b % angle), abs(angle - b % angle))
        tmc = min(abs(0 - c % angle), abs(angle - c % angle))
        if tma + tmb + tmc < mina + minb + minc:
            ret_angle, mina, minb, minc = angle, tma, tmb, tmc
            if tma < 1e-5 and tmb < 1e-5 and tmb < 1e-5:
                break
    return ret_angle


def calc_3rd_side(lena, lenb, angle):
    return math.sqrt(lena ** 2 + lenb ** 2 - 2 * lena * lenb * math.cos(math.radians(angle)))


def triangle_area(a, b, c):
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area


def func_sol(raw_data):
    (Ax, Ay), (Bx, By), (Cx, Cy) = [list(map(float, line.split(' '))) for line in raw_data.split('\n')[:-1]]

    Mx1, My1, s1 = mid_bis_slope(Ax, Ay, Bx, By)
    Mx2, My2, s2 = mid_bis_slope(Bx, By, Cx, Cy)
    Mx3, My3, s3 = mid_bis_slope(Cx, Cy, Ax, Ay)

    if s1 is None:
        Mx1, My1, s1 = Mx3, My3, s3
    elif s2 is None:
        Mx2, My2, s2 = Mx3, My3, s3

    # Z = circle's center
    Zx = (My2 - My1 + s1 * Mx1 - s2 * Mx2) / (s1 - s2)
    Zy = s1 * (Zx - Mx1) + My1

    angleAB = calc_angle(Ax, Ay, Zx, Zy, Bx, By)
    angleBC = calc_angle(Bx, By, Zx, Zy, Cx, Cy)
    angleCA = calc_angle(Cx, Cy, Zx, Zy, Ax, Ay)

    angle_between_two_pillars = gcd(angleAB, angleBC, angleCA)
    total_number_of_pillars = round(360.0 / angle_between_two_pillars)

    radius = distance(Zx, Zy, Ax, Ay)
    chord = calc_3rd_side(radius, radius, angle_between_two_pillars)
    solution = total_number_of_pillars * triangle_area(radius, radius, chord)

    return str(f'{solution:.8f}') + '\n'


def main():
    try:
        from codeforces.utilities import run_tests
        run_tests(func_sol)
    except ImportError:
        from sys import stdin
        print(func_sol(stdin.read()))


main()
