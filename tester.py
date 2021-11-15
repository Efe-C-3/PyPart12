
input_list_one = ['banana']
input_list_two = ['bAnAnA']
input_list_three = ['Mississippi']
input_list_four = ['MISSISSIPPI']
# input_list_five = [1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 7]

def gen_set(val_in: str) -> set:
    listed_letters = set()
    for i in val_in:
        if i.islower and i not in listed_letters:
            listed_letters.add(i.upper())
            #return listed_letters
        elif i.isupper() and i in listed_letters:
            listed_letters.remove(i.isupper())
    return listed_letters


print(gen_set(input_list_one))
print(gen_set(input_list_two))
print(gen_set(input_list_three))
print(gen_set(input_list_four))
# print(gen_set(input_list_five))
