# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 12:08:32 2024

@author: ADMIN
"""

chuoi = "Đại học Quốc gia, Khu phố 6, P. Linh Trung, Q. Thủ Đức, Tp. HCM"
sub_strings = chuoi.split(",")
sub_strings = [s.strip() for s in sub_strings]
print(sub_strings)