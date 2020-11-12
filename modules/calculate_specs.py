# !/usr/bin/env python3

from math import pi, sqrt

from PyQt5 import QtWidgets


def calculate(self):
    out_diameter = int(self.spin_box_out_diameter.value())
    internal_diameter_big = int(self.spin_box_internal_diameter_big.value())
    internal_diameter_small = int(self.spin_box_internal_diameter_small.value())
    height = int(self.spin_box_height.value())

    try:
        product_mass = (out_diameter ** 2 - (
                (internal_diameter_big + internal_diameter_small) / 2) ** 2) * 6.16 * height
        electrode_mass = (out_diameter ** 2 - ((internal_diameter_big + internal_diameter_small) / 2) ** 2) \
                         * 6.16 * height * 1.05
        electrode_mass_true = ((out_diameter + 10) ** 2 - ((internal_diameter_big+0.5 + internal_diameter_small+0.5) / 2) ** 2) \
                         * 6.16 * height * 1.05
        value = (pi * (out_diameter / 2) ** 2) - \
                ((1 / 3) * pi * height * (internal_diameter_big ** 2 + internal_diameter_big * internal_diameter_small
                                          + internal_diameter_small ** 2))
        speed = 84.6 * sqrt(height - (internal_diameter_big ** 2 - internal_diameter_small ** 2))
    except Exception:
        pass
    else:
        print(out_diameter, internal_diameter_big, internal_diameter_small, height)
        print(product_mass, electrode_mass, electrode_mass_true, value, speed)
