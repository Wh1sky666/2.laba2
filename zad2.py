# определите общие символы в двух строках, введенных с клавиатуры.

# !/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    u = set("abcdefghijklmnopqrstuvwxyz")

    a = set(input("Введите первую строку: "))
    b = set(input("А теперь вторую: "))

    bn = u.difference(b)
    c = a.difference(bn)
    print(len(c), " - Количество общих элементов")
    print(c, " - общие элементы")
