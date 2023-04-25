import Test_Split
import Test_Information_Gain 
from collections import Counter
car_data = [['med', 'low', '3', '4', 'med', 'med'], ['med', 'vhigh', '4', 'more', 'small', 'high'], 
            ['high', 'med', '3', '2', 'med', 'low'], ['med', 'low', '4', '4', 'med', 'low'], 
            ['med', 'low', '5more', '2', 'big', 'med'], ['med', 'med', '2', 'more', 'big', 'high'], 
            ['med', 'med', '2', 'more', 'med', 'med'], ['vhigh', 'vhigh', '2', '2', 'med', 'low'], 
            ['high', 'med', '4', '2', 'big', 'low'], ['low', 'low', '2', '4', 'big', 'med']]

car_labels = ['acc', 'acc', 'unacc', 'unacc', 'unacc', 'vgood', 'acc', 'unacc', 'unacc', 'good']

def find_best_split(dataset, labels):
    best_gain = 0
    best_feature = 0

    for feature in range(len(dataset[0])):
        print(feature)
        data_subsets, label_subsets = Test_Split.split(dataset, labels, feature)
        gain = Test_Information_Gain.weighted_information_gain(labels, label_subsets)

        if gain > best_gain:
            best_gain, feature = gain, feature
    
    return best_gain, best_feature

best_gain, best_feature = find_best_split(car_data, car_labels)
print("best gain", best_gain)
print("best feature", best_feature)

best_split, best_split_label = Test_Split.split(car_data, car_labels, best_feature)


from collections import Counter
from pprint import pprint

def build_tree(data, labels):
  
  best_feature, best_gain = find_best_split(data, labels)

  if best_gain == 0: #Base Case
    print()
    return Counter(labels)
  
  data_subsets, label_subsets = Test_Split.split(data, labels, best_feature)
  

  branches = []
  for i in range(len(data_subsets)):
    branch = build_tree(data_subsets[i], label_subsets[i])
    branches.append(branch)
  return branches

tree = build_tree(car_data, car_labels)

