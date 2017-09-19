#!/usr/bin/python

from string import ascii_lowercase, maketrans

data = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
intab = ascii_lowercase
outtab = ascii_lowercase[2:] + ascii_lowercase[:2]
trantab = maketrans(intab,outtab)
print(data.translate(trantab))