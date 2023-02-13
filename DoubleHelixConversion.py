import random
base_pair = {"A":"T",
             "G": "C",
             "T": "A",
             "C":"G",
             }
def convert():
    downstream = ""
    sequence = input("Paste your sequence here: ")
    for i in sequence:

        downstream += base_pair[i]
        if i in " ":
            downstream += i
        else:
            return "Invalid input"
    return "Your sequence is: " + downstream
def create_random_sequence():
    list_base_pair = list(base_pair)
    a = random.choices(list_base_pair,k =3)
    b = ''.join(a)
    return b
print(convert())
print(create_random_sequence())