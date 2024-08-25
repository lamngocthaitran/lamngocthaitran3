# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 12:15:25 2024

@author: ADMIN
"""

chuoi = "Đại học Quốc gia, Khu phố 6, P. Linh Trung, Q. Thủ Đức, Tp. HCM"
phan_tach = chuoi.split(",")
ket_qua = []
for phan in phan_tach:
    phan = phan.strip()
    if phan.startswith("P.") or phan.startswith("Q.") or phan.startswith("Tp."):
        phan = phan[2:]
    ket_qua.append(phan)

print(ket_qua)