# Courtsey: sRTike
import dt_util as utils

class Tuple:
    def __init__(self, row) -> None:
        self._attributes = row[:-1]
        self._class = row[-1]

    def _print(self):
        print(self._attributes, "|", self._class)

# Function to list all different types on attributes
def list_attributes(dataset):
    n_atb = len(dataset[0]._attributes)
    attributes = [[] for _ in range(n_atb + 1)]
    for item in dataset:
        for i in range(n_atb):
            if item._attributes[i] not in attributes[i]:
                attributes[i].append(item._attributes[i])
        if item._class not in attributes[n_atb]:
            attributes[n_atb].append(item._class)
    return attributes

# Function to get attribute counts
def get_attribute_counts(dataset, attributes):
    n_atb = len(dataset[0]._attributes)
    c_attributes = []
    for i in attributes[:-1]:
        atb_list = {}
        for atb in i:
            atb_dict = {}
            for _cls in attributes[-1]:
                atb_dict[_cls] = 0
            atb_list[atb] = atb_dict
        c_attributes.append(atb_list)

    # Filling attribute counts
    for item in dataset:
        for i in range(n_atb):
            atb = item._attributes[i]
            _cls = item._class
            c_attributes[i][atb][_cls] += 1
    return c_attributes

# Function to get I(p,n) values for the attributes
def get_ipns(c_attributes):
    n_atb = len(c_attributes)
    ipns = []
    for i in range(n_atb):
        vals = {}
        for atb in c_attributes[i]:
            information = utils.information_gain(classes_dict = c_attributes[i][atb])
            vals[atb] = information
        ipns.append(vals)
    return ipns

# Function to get gains
def get_gains(classes, c_attributes, ipns, max_information = 1):
    n_atb = len(c_attributes)
    gains = []
    total = 0
    for key in classes:
        total += classes[key]

    for i in range(n_atb):
        entropy = 0
        for key in c_attributes[i]:
            num = 0
            for _cls in c_attributes[i][key]:
                num += c_attributes[i][key][_cls]
            entropy += (num / total) * ipns[i][key]
        gains.append(max_information - entropy)
    return gains

def get_next_root(dataset):
    classes = {}
    for item in dataset:
        if item._class not in classes.keys():
            classes[item._class] = 1
        else:
            classes[item._class] += 1
# Calculating initial information
    max_information = utils.information_gain(classes_dict= classes)
    # print("Max Information =", max_information)

# List of all different types of attributes
    attributes = list_attributes(dataset)

# Getting attribute counts w.r.t. class
    c_attributes = get_attribute_counts(dataset, attributes)
    # print("Attribute counts :", c_attributes)

# Calculating I(p,n) values for each different type of attribute
    ipns = get_ipns(c_attributes)
    # print("Information Gains :", ipns)

# Calculating Gain Values
    gains = get_gains(classes, c_attributes, ipns, max_information)

    Max= 0.0
    arg = 0
    for i in range(len(gains)):
        if Max < gains[i]:
            Max = gains[i]
            arg = i

    root = arg + 1
    return root, gains, c_attributes, ipns

if __name__ == "__main__":
    print("Enter the tuples")
    dataset = []
    while True:
        ip = input()
        if ip == "Q":
            break
        row = ip.split(" ")
        dataset.append(Tuple(row))
    for item in dataset:
        item._print()
    root, gains, c_attributes, ipns = get_next_root(dataset)
    print("Next root = Attribute :", root, "(1 indexed)")
# For intermediary steps, uncomment following-
    # print("Gains :", gains)
    # print("Attribute counts :",c_attributes)
    # print("Informations Gains :",ipns)