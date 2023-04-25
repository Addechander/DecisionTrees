cars = [['med', 'low', '3', '4', 'med', 'med'], ['med', 'vhigh', '4', 'more', 'small', 'high'], ['high', 'med', '3', '2', 'med', 'low'],
        ['med', 'low', '4', '4', 'med', 'low'], ['med', 'low', '5more', '2', 'big', 'med'], ['med', 'med', '2', 'more', 'big', 'high'], 
        ['med', 'med', '2', 'more', 'med', 'med'], ['vhigh', 'vhigh', '2', '2', 'med', 'low'], ['high', 'med', '4', '2', 'big', 'low'], 
        ['low', 'low', '2', '4', 'big', 'med']]


car_labels = ['acc', 'acc', 'unacc', 'unacc', 'unacc', 'vgood', 'acc', 'unacc', 'unacc', 'good']

def split(dataset, labels, column): #This will split the data based on a specific index feature 
    data_subsets = []
    label_subsets = []
    counts = list(set([data[column] for data in dataset])) 
    
    """
    Goes through different values in subsets, stores the specified index value to a single value and converts the variable into list 
    which returns the different uniqiue values for the given index from different subsets
    """
    
    counts.sort()
    for k in counts:
        new_data_subset = []
        new_label_subset = []

        for i in range(len(dataset)):
            if dataset[i][column] == k:
                new_data_subset.append(dataset[i])
                new_label_subset.append(labels[i])
        
        data_subsets.append(new_data_subset)
        label_subsets.append(new_label_subset)
        
    return data_subsets, label_subsets

from pprint import pprint

split_data, split_labels =   split(cars, car_labels, 3) #This will split the data based on the third index (That feature was the number of people the car could hold).
pprint(split_data)
print(len(split_data))
pprint(split_labels)


from Test.Test_Information_Gain import weighted_information_gain
print(weighted_information_gain(car_labels, split_labels))

for i in range(0, 6):
  split_data, split_labels = split(cars, car_labels, i)
  print(weighted_information_gain(car_labels, split_labels))