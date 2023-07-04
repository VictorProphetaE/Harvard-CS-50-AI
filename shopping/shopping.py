import csv
import sys
import calendar


from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

TEST_SIZE = 0.4


def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python shopping.py data")

    # Load data from spreadsheet and split into train and test sets
    evidence, labels = load_data(sys.argv[1])
    X_train, X_test, y_train, y_test = train_test_split(
        evidence, labels, test_size=TEST_SIZE
    )

    # Train model and make predictions
    model = train_model(X_train, y_train)
    predictions = model.predict(X_test)
    sensitivity, specificity = evaluate(y_test, predictions)

    # Print results
    print(f"Correct: {(y_test == predictions).sum()}")
    print(f"Incorrect: {(y_test != predictions).sum()}")
    print(f"True Positive Rate: {100 * sensitivity:.2f}%")
    print(f"True Negative Rate: {100 * specificity:.2f}%")


def load_data(filename):
    """
    Load shopping data from a CSV file `filename` and convert into a list of
    evidence lists and a list of labels. Return a tuple (evidence, labels).

    evidence should be a list of lists, where each list contains the
    following values, in order:
        - Administrative, an integer
        - Administrative_Duration, a floating point number
        - Informational, an integer
        - Informational_Duration, a floating point number
        - ProductRelated, an integer
        - ProductRelated_Duration, a floating point number
        - BounceRates, a floating point number
        - ExitRates, a floating point number
        - PageValues, a floating point number
        - SpecialDay, a floating point number
        - Month, an index from 0 (January) to 11 (December)
        - OperatingSystems, an integer
        - Browser, an integer
        - Region, an integer
        - TrafficType, an integer
        - VisitorType, an integer 0 (not returning) or 1 (returning)
        - Weekend, an integer 0 (if false) or 1 (if true)

    labels should be the corresponding list of labels, where each label
    is 1 if Revenue is true, and 0 otherwise.
    """
    #Create a dict for months 
    month = {}
    cont = 0
    for i in range(1,13):
      month[calendar.month_abbr[i]] = cont
      cont += 1    
    month['June'] = month.pop('Jun')
    
    evidence_list = []
    labels_list = []
    
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            temporary = []
            #Appending to a temporary list, to next append to the final list
            temporary.append(int(row["Administrative"]))
            temporary.append(float(row["Administrative_Duration"]))
            temporary.append(int(row["Informational"]))
            temporary.append(float(row["Informational_Duration"]))
            temporary.append(int(row["ProductRelated"]))
            temporary.append(float(row["ProductRelated_Duration"]))
            temporary.append(float(row["BounceRates"]))
            temporary.append(float(row["ExitRates"]))
            temporary.append(float(row["PageValues"]))
            temporary.append(float(row["SpecialDay"]))
            temporary.append(month[row["Month"]])
            temporary.append(int(row["OperatingSystems"]))
            temporary.append(int(row["Browser"]))
            temporary.append(int(row["Region"]))
            temporary.append(int(row["TrafficType"]))
            if row["VisitorType"] == "Returning_Visitor":
                temporary.append(1)
            else:
                temporary.append(0)
            if row["Weekend"] == "TRUE":
                temporary.append(1)
            else:
                temporary.append(0)
            
            evidence_list.append(temporary)
            if row["Revenue"] == "TRUE":
                labels_list.append(1)
            else:
                labels_list.append(0)
                
    return (evidence_list, labels_list)


def train_model(evidence, labels):
    """
    Given a list of evidence lists and a list of labels, return a
    fitted k-nearest neighbor model (k=1) trained on the data.
    """
    
    model = KNeighborsClassifier(n_neighbors = 1)
    model.fit(evidence, labels)

    return model


def evaluate(labels, predictions):
    """
    Given a list of actual labels and a list of predicted labels,
    return a tuple (sensitivity, specificity).

    Assume each label is either a 1 (positive) or 0 (negative).

    `sensitivity` should be a floating-point value from 0 to 1
    representing the "true positive rate": the proportion of
    actual positive labels that were accurately identified.

    `specificity` should be a floating-point value from 0 to 1
    representing the "true negative rate": the proportion of
    actual negative labels that were accurately identified.
    """
    #Initialization of the variables
    sensitivity = float(0)
    specificity = float(0)   
    pos = 0
    neg = 0
    
    #First loop to separate the pos and neg
    for label in labels:
        if label == 1:
            pos += 1
        if label == 0:
            neg += 1
    #Second loop to separate the sensitivity and specificity
    for label, prediction in zip(labels,predictions):
        if label == prediction and label == 1:
            sensitivity += 1
        if label == prediction and label == 0:
            specificity += 1
            
    sensitivity /= pos
    specificity /= neg
    
    return (sensitivity, specificity)


if __name__ == "__main__":
    main()
