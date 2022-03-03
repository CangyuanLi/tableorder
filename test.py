import re

test_string = "appendixtable\\ref{sometablehere} afterparty appendixtable\\ref{blah}"
test2 = "Ihavenumber123459andyouhave123459"

pattern = re.compile(r"appendixtable\\ref{.*?}")
pattern2 = re.compile(r"\d+")
x = re.findall(pattern, test_string)
y = re.findall(pattern2, test2)
print(x)
print(y)
