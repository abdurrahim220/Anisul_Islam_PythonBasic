
sub = ["C","C++","Java","Python","Android","OS","PHP"]
sub.append("TOC")


sub.insert(2,"Ruby")
sub.remove("PHP")

sub.sort()
sub.reverse()

sub.pop() #remove lust index item
# sub.clear

sub1 = sub.copy()

pos = sub1.index("Java") #Showing the index item position

sub1.append("Count")
sub1.append("Count")
sub1.append("Count")
sub1.append("Count")
sub1.append("Count")
ct = sub1.count("Count")
print(ct)