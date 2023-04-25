#Gini Impurity

from collections import Counter #Counter counts the number of unique label in the data set

label_1 = ["unacc", "unacc", "acc", "acc", "good", "good"]
label_2 = ["unacc","unacc","unacc", "good", "vgood", "vgood"]
label_3 = ["unacc", "unacc", "unacc", "unacc", "unacc", "unacc"]


def impurity(dataset):
    impurity = 1 

    label_counts = Counter(dataset)
    
    #print(label_counts)
    #print(type(label_counts))

    for label in label_counts:
        
        #print("Dataset", dataset)
        #print("label", label)
        #print("label_count",label_counts[label])
        #print("length",len(label))

        probability_of_label = label_counts[label]/len(dataset)
    
        #print(probability_of_label)

        impurity -= probability_of_label**2

        return impurity


impurity(label_1)
impurity(label_2)
impurity(label_3)



