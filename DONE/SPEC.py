with open('test.txt', "r") as file:
    nums = file.read().split("\n")

mono_mass_tab = {
  71.03711 :"A",
  103.00919 :"C",
  115.02694 :"D",
  129.04259 :"E",
  147.06841 :"F",
  57.02146 :"G",
  137.05891 :"H",
  113.08406 :"I",
  128.09496 :"K",
  113.08406 :"L",
  131.04049 :"M",
  114.04293 :"N",
  97.05276 :"P",
  128.05858 :"Q",
  156.10111 :"R",
  87.03203 :"S",
  101.04768 :"T",
  99.06841 :"V",
  186.07931 :"W",
  163.06333 :"Y",
    }
 
nums = [float(x) for x in nums]
diff = []
for i in range(1, len(nums)):
    df = nums[i] - nums[i-1]
    diff.append(round(df, 5))

for df in diff:
    a = mono_mass_tab.get(df, mono_mass_tab[min(mono_mass_tab.keys(), key=lambda k: abs(k-df))])
    print(a, end="")
print()
