# !/usr/bin/env python3

from math import pi, sqrt

from PyQt5 import QtWidgets


def calculate(self):
    try:
        D = int(self.spin_box_out_diameter.value()) / 100
        d1 = int(self.spin_box_internal_diameter_big.value()) / 100
        d2 = int(self.spin_box_internal_diameter_small.value()) / 100
        dsr = (d1 + d2) / 2
        h = int(self.spin_box_height.value()) / 100

        product_mass = (D**2 - dsr**2) * 6.16 * h
        electrode_mass = (D**2 - dsr**2) * 6.16 * h * 1.05

        D_true = D + 0.01
        d1_true = d1 + 0.01
        d2_true = d2 + 0.01
        dsr_true = (d1_true + d2_true) / 2
        h_true = h + 0.01
        electrode_mass_true = (D_true**2 - dsr_true**2) * 6.16 * h_true * 1.05

        value_out = pi * (D / 2)**2 * h
        value_internal = (1 / 3) * pi * h * ((d1 / 2)**2 + (d1 / 2) * (d2 / 2) + (d2 / 2)**2)
        value = value_out - value_internal

        speed = 84.6 * sqrt((h / 10) / ((d1 / 10)**2 - (d2 / 10)**2))
    except Exception as e:
        print(e)
    else:
        self.label_mass_product.setText(str("Масса изделия: " + str(round(product_mass, 2))))
        self.label_mass_metal.setText(str("Масса тебуемого электрода: " + str(round(electrode_mass, 2))))
        self.label_mass_metal_true.setText(str("Рекомендуемая масса электрода: " + str(round(electrode_mass_true, 2))))
        self.label_value.setText(str("Объём: " + str(round(value, 2))))
        self.label_speed.setText(str("Скорость вращения: " + str(round(speed, 2))))
