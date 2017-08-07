from typing import List, Tuple

import numpy as np


def generate_map(w=64, h=64, l=0, t=0):
    """ Generates a list of subsequential coordinates on the curve which fills 2d space of specified width and height
    :param l: left
    :type l: int
    :param t: top
    :type t: int
    :param w: width
    :type w: int
    :param h: height
    :type h: int
    :rtype: (list of (int, int), dict of (int, int): int)
    :return:
    """
    if h > w:
        if (h % 2 == 1) and (w % 2 == 0):
            ret = go(l, t, w, 0, 0, h, "m")  # go diagonal
        else:
            ret = go(l, t, w, 0, 0, h, "r")  # go top->down
    else:
        if (w % 2 == 1) and (h % 2 == 0):
            ret = go(l, t, w, 0, 0, h, "m")  # go diagonal
        else:
            ret = go(l, t, w, 0, 0, h, "l")  # go left->right
    return ret, dict((cord, i) for i, cord in enumerate(ret))


def go(x0, y0, dxl, dyl, dxr, dyr, dir):
    """
    :param x0: start corner looking to the center of the rectangle
    :type x0: int
    :param y0: start corner looking to the center of the rectangle
    :type y0: int
    :param dxl: vector from the start corner to the left corner of the rectangle
    :type dxl: int
    :param dyl: vector from the start corner to the left corner of the rectangle
    :type dyl: int
    :param dxr: vector from the start corner to the right corner of the rectangle
    :type dxr: int
    :param dyr: vector from the start corner to the right corner of the rectangle
    :type dyr: int
    :param dir: direction to go - "l"=left, "m"=middle, "r"=right
    :type dir: str
    :rtype: list of (int, int)
    :return:
    """
    ret = []
    if abs((dxl + dyl) * (dxr + dyr)) <= 6:
        if abs(dxl + dyl) == 1:
            ddx = dxr / abs(dxr + dyr)
            ddy = dyr / abs(dxr + dyr)
            for ii in range(abs(dxr + dyr)):
                ret.append((x0 + ii * ddx + (dxl + ddx - 1) / 2, y0 + ii * ddy + (dyl + ddy - 1) / 2))
            return ret
        if abs(dxr + dyr) == 1:
            ddx = dxl / abs(dxl + dyl)
            ddy = dyl / abs(dxl + dyl)
            for ii in range(abs(dxl + dyl)):
                ret.append((x0 + ii * ddx + (dxr + ddx - 1) / 2, y0 + ii * ddy + (dyr + ddy - 1) / 2))
            return ret
        if dir == "l":
            ddx = dxr / abs(dxr + dyr)
            ddy = dyr / abs(dxr + dyr)
            for ii in range(abs(dxr + dyr)):
                ret.append((x0 + ii * ddx + (dxl / 2 + ddx - 1) / 2, y0 + ii * ddy + (dyl / 2 + ddy - 1) / 2))
            for ii in range(abs(dxr + dyr) - 1, -1, -1):
                ret.append(
                    (x0 + ii * ddx + (dxl + dxl / 2 + ddx - 1) / 2, y0 + ii * ddy + (dyl + dyl / 2 + ddy - 1) / 2))
            return ret
        if dir == "r":
            ddx = dxl / abs(dxl + dyl)
            ddy = dyl / abs(dxl + dyl)
            for ii in range(abs(dxl + dyl)):
                ret.append((x0 + ii * ddx + (dxr / 2 + ddx - 1) / 2, y0 + ii * ddy + (dyr / 2 + ddy - 1) / 2))
            for ii in range(abs(dxl + dyl) - 1, -1, -1):
                ret.append(
                    (x0 + ii * ddx + (dxr + dxr / 2 + ddx - 1) / 2, y0 + ii * ddy + (dyr + dyr / 2 + ddy - 1) / 2))
            return ret
        if dir == "m":
            if abs(dxr + dyr) == 3:
                ddx = dxr / abs(dxr + dyr)
                ddy = dyr / abs(dxr + dyr)
                ret.append((x0 + (dxl / 2 + ddx - 1) / 2, y0 + (dyl / 2 + ddy - 1) / 2))
                ret.append((x0 + (dxl + dxl / 2 + ddx - 1) / 2, y0 + (dyl + dyl / 2 + ddy - 1) / 2))
                ret.append((x0 + ddx + (dxl + dxl / 2 + ddx - 1) / 2, y0 + ddy + (dyl + dyl / 2 + ddy - 1) / 2))
                ret.append((x0 + ddx + (dxl / 2 + ddx - 1) / 2, y0 + ddy + (dyl / 2 + ddy - 1) / 2))
                ret.append((x0 + 2 * ddx + (dxl / 2 + ddx - 1) / 2, y0 + 2 * ddy + (dyl / 2 + ddy - 1) / 2))
                ret.append((x0 + 2 * ddx + (dxl + dxl / 2 + ddx - 1) / 2, y0 + 2 * ddy + (dyl + dyl / 2 + ddy - 1) / 2))
                return ret
            if abs(dxl + dyl) == 3:
                ddx = dxl / abs(dxl + dyl)
                ddy = dyl / abs(dxl + dyl)
                ret.append((x0 + (dxr / 2 + ddx - 1) / 2, y0 + (dyr / 2 + ddy - 1) / 2))
                ret.append((x0 + (dxr + dxr / 2 + ddx - 1) / 2, y0 + (dyr + dyr / 2 + ddy - 1) / 2))
                ret.append((x0 + ddx + (dxr + dxr / 2 + ddx - 1) / 2, y0 + ddy + (dyr + dyr / 2 + ddy - 1) / 2))
                ret.append((x0 + ddx + (dxr / 2 + ddx - 1) / 2, y0 + ddy + (dyr / 2 + ddy - 1) / 2))
                ret.append((x0 + 2 * ddx + (dxr / 2 + ddx - 1) / 2, y0 + 2 * ddy + (dyr / 2 + ddy - 1) / 2))
                ret.append((x0 + 2 * ddx + (dxr + dxr / 2 + ddx - 1) / 2, y0 + 2 * ddy + (dyr + dyr / 2 + ddy - 1) / 2))
                return ret
        raise Exception('Render error')
    # divide into 2 parts if necessary
    if 2 * (abs(dxl) + abs(dyl)) > 3 * (abs(dxr) + abs(dyr)):  # left side much longer than right side
        dxl2 = round(dxl / 2)
        dyl2 = round(dyl / 2)
        if (abs(dxr) + abs(dyr)) % 2 == 0:  # right side is even
            if (abs(dxl) + abs(dyl)) % 2 == 0:  # make 2 parts from even side
                if dir == "l":
                    if (abs(dxl) + abs(dyl)) % 4 == 0:
                        ret.extend(go(x0, y0, dxl2, dyl2, dxr, dyr, "l"))
                        ret.extend(go(x0 + dxl2, y0 + dyl2, dxl - dxl2, dyl - dyl2, dxr, dyr, "l"))
                    else:
                        ret.extend(go(x0, y0, dxl2, dyl2, dxr, dyr, "m"))
                        ret.extend(go(x0 + dxl2 + dxr, y0 + dyl2 + dyr, -dxr, -dyr, dxl - dxl2, dyl - dyl2, "m"))
                    return ret
            else:  # make 2 parts from odd side
                if dir == "m":
                    if (abs(dxl2) + abs(dyl2)) % 2 == 0:
                        ret.extend(go(x0, y0, dxl2, dyl2, dxr, dyr, "l"))
                        ret.extend(go(x0 + dxl2, y0 + dyl2, dxl - dxl2, dyl - dyl2, dxr, dyr, "m"))
                    else:
                        ret.extend(go(x0, y0, dxl2, dyl2, dxr, dyr, "m"))
                        ret.extend(go(x0 + dxl2 + dxr, y0 + dyl2 + dyr, -dxr, -dyr, dxl - dxl2, dyl - dyl2, "r"))
                    return ret
        else:  # right side is odd
            if dir == "l":
                ret.extend(go(x0, y0, dxl2, dyl2, dxr, dyr, "l"))
                ret.extend(go(x0 + dxl2, y0 + dyl2, dxl - dxl2, dyl - dyl2, dxr, dyr, "l"))
                return ret
            if dir == "m":
                ret.extend(go(x0, y0, dxl2, dyl2, dxr, dyr, "l"))
                ret.extend(go(x0 + dxl2, y0 + dyl2, dxl - dxl2, dyl - dyl2, dxr, dyr, "m"))
                return ret
    if 2 * (abs(dxr) + abs(dyr)) > 3 * (abs(dxl) + abs(dyl)):  # right side much longer than left side
        dxr2 = round(dxr / 2)
        dyr2 = round(dyr / 2)
        if (abs(dxl) + abs(dyl)) % 2 == 0:  # left side is even
            if (abs(dxr) + abs(dyr)) % 2 == 0:  # make 2 parts from even side
                if dir == "r":
                    if (abs(dxr) + abs(dyr)) % 4 == 0:  # make 2 parts even-even from even side
                        ret.extend(go(x0, y0, dxl, dyl, dxr2, dyr2, "r"))
                        ret.extend(go(x0 + dxr2, y0 + dyr2, dxl, dyl, dxr - dxr2, dyr - dyr2, "r"))
                    else:  # make 2 parts odd-odd from even side
                        ret.extend(go(x0, y0, dxl, dyl, dxr2, dyr2, "m"))
                        ret.extend(go(x0 + dxr2 + dxl, y0 + dyr2 + dyl, dxr - dxr2, dyr - dyr2, -dxl, -dyl, "m"))
                    return ret
            else:  # make 2 parts from odd side
                if dir == "m":
                    if (abs(dxr2) + abs(dyr2)) % 2 == 0:
                        ret.extend(go(x0, y0, dxl, dyl, dxr2, dyr2, "r"))
                        ret.extend(go(x0 + dxr2, y0 + dyr2, dxl, dyl, dxr - dxr2, dyr - dyr2, "m"))
                    else:
                        ret.extend(go(x0, y0, dxl, dyl, dxr2, dyr2, "m"))
                        ret.extend(go(x0 + dxr2 + dxl, y0 + dyr2 + dyl, dxr - dxr2, dyr - dyr2, -dxl, -dyl, "l"))
                    return ret
        else:  # left side is odd
            if dir == "r":
                ret.extend(go(x0, y0, dxl, dyl, dxr2, dyr2, "r"))
                ret.extend(go(x0 + dxr2, y0 + dyr2, dxl, dyl, dxr - dxr2, dyr - dyr2, "r"))
                return ret
            if dir == "m":
                ret.extend(go(x0, y0, dxl, dyl, dxr2, dyr2, "r"))
                ret.extend(go(x0 + dxr2, y0 + dyr2, dxl, dyl, dxr - dxr2, dyr - dyr2, "m"))
                return ret
    if (dir == "l") or (dir == "r"):
        dxl2 = round(dxl / 2)
        dyl2 = round(dyl / 2)
        dxr2 = round(dxr / 2)
        dyr2 = round(dyr / 2)
        if (abs(dxl + dyl) % 2 == 0) and (abs(dxr + dyr) % 2 == 0):  # even-even
            if abs(dxl2 + dyl2 + dxr2 + dyr2) % 2 == 0:  # ee-ee or oo-oo
                if dir == "l":
                    ret.extend(go(x0, y0, dxl2, dyl2, dxr2, dyr2, "r"))
                    ret.extend(go(x0 + dxr2, y0 + dyr2, dxl2, dyl2, dxr - dxr2, dyr - dyr2, "l"))
                    ret.extend(go
                               (x0 + dxr2 + dxl2, y0 + dyr2 + dyl2, dxl - dxl2, dyl - dyl2, dxr - dxr2, dyr - dyr2,
                                "l"))
                    ret.extend(go(x0 + dxr2 + dxl, y0 + dyr2 + dyl, dxl2 - dxl, dyl2 - dyl, -dxr2, -dyr2, "r"))
                else:
                    ret.extend(go(x0, y0, dxl2, dyl2, dxr2, dyr2, "l"))
                    ret.extend(go(x0 + dxl2, y0 + dyl2, dxl - dxl2, dyl - dyl2, dxr2, dyr2, "r"))
                    ret.extend(go
                               (x0 + dxr2 + dxl2, y0 + dyr2 + dyl2, dxl - dxl2, dyl - dyl2, dxr - dxr2, dyr - dyr2,
                                "r"))
                    ret.extend(go(x0 + dxr + dxl2, y0 + dyr + dyl2, -dxl2, -dyl2, dxr2 - dxr, dyr2 - dyr, "l"))
            else:  # ee-oo or oo-ee
                if (dxr2 + dyr2) % 2 == 0:  # ee-oo
                    if dir == "l":
                        ret.extend(go(x0, y0, dxl2, dyl2, dxr2, dyr2, "r"))
                        ret.extend(go(x0 + dxr2, y0 + dyr2, dxl2, dyl2, dxr - dxr2, dyr - dyr2, "m"))
                        ret.extend(go
                                   (x0 + dxr + dxl2, y0 + dyr + dyl2, dxr2 - dxr, dyr2 - dyr, dxl - dxl2, dyl - dyl2,
                                    "m"))
                        ret.extend(go(x0 + dxr2 + dxl, y0 + dyr2 + dyl, dxl2 - dxl, dyl2 - dyl, -dxr2, -dyr2, "r"))
                    else:  # ee-oo for dir="r" not possible, so transforming into e-1,e+1-oo = oo-oo
                        if dxr2 != 0:
                            dxr2 += 1
                        else:
                            dyr2 += 1
                        ret.extend(go(x0, y0, dxl2, dyl2, dxr2, dyr2, "l"))
                        ret.extend(go(x0 + dxl2, y0 + dyl2, dxl - dxl2, dyl - dyl2, dxr2, dyr2, "m"))
                        ret.extend(go
                                   (x0 + dxl + dxr2, y0 + dyl + dyr2, dxr - dxr2, dyr - dyr2, dxl2 - dxl, dyl2 - dyl,
                                    "m"))
                        ret.extend(go(x0 + dxl2 + dxr, y0 + dyl2 + dyr, -dxl2, -dyl2, dxr2 - dxr, dyr2 - dyr, "l"))
                else:  # oo-ee
                    if dir == "r":
                        ret.extend(go(x0, y0, dxl2, dyl2, dxr2, dyr2, "l"))
                        ret.extend(go(x0 + dxl2, y0 + dyl2, dxl - dxl2, dyl - dyl2, dxr2, dyr2, "m"))
                        ret.extend(go
                                   (x0 + dxl + dxr2, y0 + dyl + dyr2, dxr - dxr2, dyr - dyr2, dxl2 - dxl, dyl2 - dyl,
                                    "m"))
                        ret.extend(go(x0 + dxl2 + dxr, y0 + dyl2 + dyr, -dxl2, -dyl2, dxr2 - dxr, dyr2 - dyr, "l"))
                    else:  # oo-ee for dir="l" not possible, so transforming into oo-e-1,e+1 = oo-oo
                        if dxl2 != 0:
                            dxl2 += 1
                        else:
                            dyl2 += 1
                        ret.extend(go(x0, y0, dxl2, dyl2, dxr2, dyr2, "r"))
                        ret.extend(go(x0 + dxr2, y0 + dyr2, dxl2, dyl2, dxr - dxr2, dyr - dyr2, "m"))
                        ret.extend(go
                                   (x0 + dxr + dxl2, y0 + dyr + dyl2, dxr2 - dxr, dyr2 - dyr, dxl - dxl2, dyl - dyl2,
                                    "m"))
                        ret.extend(go(x0 + dxr2 + dxl, y0 + dyr2 + dyl, dxl2 - dxl, dyl2 - dyl, -dxr2, -dyr2, "r"))
        else:  # not even-even
            if (abs(dxl + dyl) % 2 != 0) and (abs(dxr + dyr) % 2 != 0):  # odd-odd
                if dxl2 % 2 != 0: dxl2 = dxl - dxl2  # get it in a shape eo-eo
                if dyl2 % 2 != 0: dyl2 = dyl - dyl2
                if dxr2 % 2 != 0: dxr2 = dxr - dxr2
                if dyr2 % 2 != 0: dyr2 = dyr - dyr2
                if dir == "l":
                    ret.extend(go(x0, y0, dxl2, dyl2, dxr2, dyr2, "r"))
                    ret.extend(go(x0 + dxr2, y0 + dyr2, dxl2, dyl2, dxr - dxr2, dyr - dyr2, "m"))
                    ret.extend(
                        go(x0 + dxr + dxl2, y0 + dyr + dyl2, dxr2 - dxr, dyr2 - dyr, dxl - dxl2, dyl - dyl2, "m"))
                    ret.extend(go(x0 + dxr2 + dxl, y0 + dyr2 + dyl, dxl2 - dxl, dyl2 - dyl, -dxr2, -dyr2, "r"))
                else:
                    ret.extend(go(x0, y0, dxl2, dyl2, dxr2, dyr2, "l"))
                    ret.extend(go(x0 + dxl2, y0 + dyl2, dxl - dxl2, dyl - dyl2, dxr2, dyr2, "m"))
                    ret.extend(
                        go(x0 + dxl + dxr2, y0 + dyl + dyr2, dxr - dxr2, dyr - dyr2, dxl2 - dxl, dyl2 - dyl, "m"))
                    ret.extend(go(x0 + dxl2 + dxr, y0 + dyl2 + dyr, -dxl2, -dyl2, dxr2 - dxr, dyr2 - dyr, "l"))
            else:  # even-odd or odd-even
                if abs(dxl + dyl) % 2 == 0:  # odd-even
                    if dir == "l":
                        if dxr2 % 2 != 0: dxr2 = dxr - dxr2  # get it in a shape eo-xx
                        if dyr2 % 2 != 0: dyr2 = dyr - dyr2
                        if abs(dxl + dyl) > 2:
                            ret.extend(go(x0, y0, dxl2, dyl2, dxr2, dyr2, "r"))
                            ret.extend(go(x0 + dxr2, y0 + dyr2, dxl2, dyl2, dxr - dxr2, dyr - dyr2, "l"))
                            ret.extend(go(x0 + dxr2 + dxl2, y0 + dyr2 + dyl2, dxl - dxl2, dyl - dyl2, dxr - dxr2,
                                          dyr - dyr2, "l"))
                            ret.extend(go(x0 + dxr2 + dxl, y0 + dyr2 + dyl, dxl2 - dxl, dyl2 - dyl, -dxr2, -dyr2, "r"))
                        else:
                            ret.extend(go(x0, y0, dxl2, dyl2, dxr2, dyr2, "r"))
                            ret.extend(go(x0 + dxr2, y0 + dyr2, dxl2, dyl2, dxr - dxr2, dyr - dyr2, "m"))
                            ret.extend(go
                                       (x0 + dxr + dxl2, y0 + dyr + dyl2, dxr2 - dxr, dyr2 - dyr, dxl - dxl2,
                                        dyl - dyl2, "m"))
                            ret.extend(go(x0 + dxr2 + dxl, y0 + dyr2 + dyl, dxl2 - dxl, dyl2 - dyl, -dxr2, -dyr2, "r"))
                    else:
                        raise Exception(
                            '4-part-error1: {}, {}, {}, {}, {}, {}, {}'.format(x0, y0, dxl, dyl, dxr, dyr, dir))
                else:  # even-odd
                    if dir == "r":
                        if dxl2 % 2 != 0: dxl2 = dxl - dxl2  # get it in a shape xx-eo
                        if dyl2 % 2 != 0: dyl2 = dyl - dyl2
                        if abs(dxr + dyr) > 2:
                            ret.extend(go(x0, y0, dxl2, dyl2, dxr2, dyr2, "l"))
                            ret.extend(go(x0 + dxl2, y0 + dyl2, dxl - dxl2, dyl - dyl2, dxr2, dyr2, "r"))
                            ret.extend(go(x0 + dxr2 + dxl2, y0 + dyr2 + dyl2, dxl - dxl2, dyl - dyl2, dxr - dxr2,
                                          dyr - dyr2, "r"))
                            ret.extend(go(x0 + dxr + dxl2, y0 + dyr + dyl2, -dxl2, -dyl2, dxr2 - dxr, dyr2 - dyr, "l"))
                        else:
                            ret.extend(go(x0, y0, dxl2, dyl2, dxr2, dyr2, "l"))
                            ret.extend(go(x0 + dxl2, y0 + dyl2, dxl - dxl2, dyl - dyl2, dxr2, dyr2, "m"))
                            ret.extend(go
                                       (x0 + dxl + dxr2, y0 + dyl + dyr2, dxr - dxr2, dyr - dyr2, dxl2 - dxl,
                                        dyl2 - dyl, "m"))
                            ret.extend(go(x0 + dxl2 + dxr, y0 + dyl2 + dyr, -dxl2, -dyl2, dxr2 - dxr, dyr2 - dyr, "l"))
                    else:
                        raise Exception(
                            '4-part-error2: {}, {}, {}, {}, {}, {}, {}'.format(x0, y0, dxl, dyl, dxr, dyr, dir))
    # start
    else:  # dir=="m" -> divide into 3x3 parts
        if (abs(dxl + dyl) % 2 == 0) and (abs(dxr + dyr) % 2 == 0):
            raise Exception('9-part-error1:: {}, {}, {}, {}, {}, {}, {}'.format(x0, y0, dxl, dyl, dxr, dyr, dir))
        if abs(dxr + dyr) % 2 == 0:  # even-odd: oeo-ooo
            dxl2 = round(dxl / 3)
            dyl2 = round(dyl / 3)
            dxr2 = round(dxr / 3)
            dyr2 = round(dyr / 3)
            if (dxl2 + dyl2) % 2 == 0:  # make it odd
                dxl2 = dxl - 2 * dxl2
                dyl2 = dyl - 2 * dyl2
            if (dxr2 + dyr2) % 2 == 0:  # make it odd (not necessary, however results are better for 12x30, 18x30 etc.)
                if abs(dxr2 + dyr2) != 2:
                    if dxr < 0: dxr2 += 1
                    if dxr > 0: dxr2 -= 1  # dont use else: here !
                    if dyr < 0: dyr2 += 1
                    if dyr > 0: dyr2 -= 1  # dont use else: here !
        else:  # odd-even: ooo-oeo
            dxl2 = round(dxl / 3)
            dyl2 = round(dyl / 3)
            dxr2 = round(dxr / 3)
            dyr2 = round(dyr / 3)
            if (dxr2 + dyr2) % 2 == 0:  # make it odd
                dxr2 = dxr - 2 * dxr2
                dyr2 = dyr - 2 * dyr2
            if (dxl2 + dyl2) % 2 == 0:  # make it odd (not necessary, however results are better for 12x30, 18x30 etc.)
                if abs(dxl2 + dyl2) != 2:
                    if dxl < 0: dxl2 += 1
                    if dxl > 0: dxl2 -= 1  # dont use else: here !
                    if dyl < 0: dyl2 += 1
                    if dyl > 0: dyl2 -= 1  # dont use else: here !
        if abs(dxl + dyl) < abs(dxr + dyr):
            ret.extend(go(x0, y0, dxl2, dyl2, dxr2, dyr2, "m"))
            ret.extend(go(x0 + dxl2 + dxr2, y0 + dyl2 + dyr2, -dxr2, -dyr2, dxl - 2 * dxl2, dyl - 2 * dyl2, "m"))
            ret.extend(go(x0 + dxl - dxl2, y0 + dyl - dyl2, dxl2, dyl2, dxr2, dyr2, "m"))
            ret.extend(go(x0 + dxl + dxr2, y0 + dyl + dyr2, dxr - 2 * dxr2, dyr - 2 * dyr2, -dxl2, -dyl2, "m"))
            ret.extend(go(x0 + dxr - dxr2 + dxl - dxl2, y0 + dyr - dyr2 + dyl - dyl2, 2 * dxl2 - dxl, 2 * dyl2 - dyl,
                          2 * dxr2 - dxr, 2 * dyr2 - dyr, "m"))
            ret.extend(go(x0 + dxl2 + dxr2, y0 + dyl2 + dyr2, dxr - 2 * dxr2, dyr - 2 * dyr2, -dxl2, -dyl2, "m"))
            ret.extend(go(x0 + dxr - dxr2, y0 + dyr - dyr2, dxl2, dyl2, dxr2, dyr2, "m"))
            ret.extend(go(x0 + dxr + dxl2, y0 + dyr + dyl2, -dxr2, -dyr2, dxl - 2 * dxl2, dyl - 2 * dyl2, "m"))
            ret.extend(go(x0 + dxr - dxr2 + dxl - dxl2, y0 + dyr - dyr2 + dyl - dyl2, dxl2, dyl2, dxr2, dyr2, "m"))

        else:
            ret.extend(go(x0, y0, dxl2, dyl2, dxr2, dyr2, "m"))
            ret.extend(go(x0 + dxl2 + dxr2, y0 + dyl2 + dyr2, dxr - 2 * dxr2, dyr - 2 * dyr2, -dxl2, -dyl2, "m"))
            ret.extend(go(x0 + dxr - dxr2, y0 + dyr - dyr2, dxl2, dyl2, dxr2, dyr2, "m"))
            ret.extend(go(x0 + dxr + dxl2, y0 + dyr + dyl2, -dxr2, -dyr2, dxl - 2 * dxl2, dyl - 2 * dyl2, "m"))
            ret.extend(go(x0 + dxr - dxr2 + dxl - dxl2, y0 + dyr - dyr2 + dyl - dyl2, 2 * dxl2 - dxl, 2 * dyl2 - dyl,
                          2 * dxr2 - dxr, 2 * dyr2 - dyr, "m"))
            ret.extend(go(x0 + dxl2 + dxr2, y0 + dyl2 + dyr2, -dxr2, -dyr2, dxl - 2 * dxl2, dyl - 2 * dyl2, "m"))
            ret.extend(go(x0 + dxl - dxl2, y0 + dyl - dyl2, dxl2, dyl2, dxr2, dyr2, "m"))
            ret.extend(go(x0 + dxl + dxr2, y0 + dyl + dyr2, dxr - 2 * dxr2, dyr - 2 * dyr2, -dxl2, -dyl2, "m"))
            ret.extend(go(x0 + dxr - dxr2 + dxl - dxl2, y0 + dyr - dyr2 + dyl - dyl2, dxl2, dyl2, dxr2, dyr2, "m"))

    return ret


def coord_to_position(coordinate, curve_map):
    """ Gives a position on the curve which corresponds to given coordinate. Domain: [0, 1]
    :param coordinate: Coordinate within the space the curve is filling
    :type coordinate: (int, int)
    :param curve_map: Generated curve map
    :type curve_map: (list of (int, int), dict of (int, int): int)
    :rtype: float
    :return:
    """
    max_len = len(curve_map[0]) - 1
    try:
        i = curve_map[1][coordinate]
        return i / max_len
    except Exception:
        raise Exception('Coordinate is not on the the curve!')


def position_to_coord(pos, curve_map):
    """ Gives a coordinate which corresponds to given position.
    :param pos: Position on the curve. Domain [0, 1]
    :type pos: float
    :param curve_map: Generated curve map
    :type curve_map: (list of (int, int), dict of (int, int): int)
    :rtype: (int, int)
    :return:
    """
    curve_length = len(curve_map[0]) - 1
    ipos = round(curve_length * pos)
    try:
        return curve_map[0][ipos]
    except Exception:
        raise Exception('Point is not on the curve!')
