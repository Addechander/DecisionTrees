from collections import Counter

unsplit_labels = ["unacc", "unacc", "unacc", "unacc", "unacc", "unacc", "good", "good", "good", "good", "vgood", "vgood", "vgood"]

split_labels_1 = [
  ["unacc", "unacc", "unacc", "unacc", "unacc", "unacc", "good", "good", "vgood"], 
  [ "good", "good"], 
  ["vgood", "vgood"]
]

split_labels_2 = [
  ["unacc", "unacc", "unacc", "unacc","unacc", "unacc", "good", "good", "good", "good"], 
  ["vgood", "vgood", "vgood"]
]

from Test.Test_Gini_Impurity import impurity as gini

info_gain = gini(unsplit_labels)

for subset in split_labels_1:
  print(subset)
  print(gini(subset))
  info_gain -= gini(subset)

print("Unweighted", info_gain)

for subset in split_labels_2:
  print(subset)
  print(gini(subset))
  info_gain -= gini(subset)

print("Unweighted", info_gain)


def unweighted_information_gain(starting_labels, split_labels):
  info_gain_of_unsplit_data = gini(starting_labels)
  for subset in split_labels:
    info_gain_of_unsplit_data -= gini(subset)
  
  return info_gain_of_unsplit_data

def weighted_information_gain(starting_labels, split_labels):
  info_gain_of_unsplit_data = gini(starting_labels)
  for subset in split_labels:
    info_gain_of_unsplit_data -= gini(subset)*(len(subset)/len(starting_labels))
  
  return info_gain_of_unsplit_data

print("unweighted", unweighted_information_gain(unsplit_labels, split_labels_1))
print("unweighted", unweighted_information_gain(unsplit_labels, split_labels_2))

print("weighted", weighted_information_gain(unsplit_labels, split_labels_1))
print("weighted", weighted_information_gain(unsplit_labels, split_labels_2))
  




