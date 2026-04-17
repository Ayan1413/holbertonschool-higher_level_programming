#!/usr/bin/python3
"""
Bu modul '0-add_integer' funksiyasını təqdim edir.
Bu funksiya iki tam ədədi toplamaq üçün istifadə olunur.
"""


def add_integer(a, b=98):
    """İki tam ədədi toplayır.

    Arqumentlər:
        a: Birinci ədəd (int və ya float).
        b: İkinci ədəd (int və ya float).

    Geri qaytarır:
        İki arqumentin tam ədəd cəmi.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
