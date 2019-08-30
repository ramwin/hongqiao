#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2019-08-31 00:21:07


text = open("README.md").read()
with open("README_rn.md", mode="w", newline="\r\n") as f:
    f.write(text)
with open("README_gbk.md", mode="w", encoding="gbk") as f:
    f.write(text)
with open("README_gbk_rn.md", mode="w", newline="\r\n", encoding="gbk") as f:
    f.write(text)
