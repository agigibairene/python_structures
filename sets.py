#A set is used to store a collection of data with no duplicates
#A set is unorderd
#A set is unchangeable
#A set is defined by curly brackets {}
#Set objects does not support indexing

List = [1,2,2,3,4,]
# A set can be used to remove duplicates from a list, which  means when "First" is printed the duplicates will be removed
First = set(List)
print(First)
SET_1 = {1,2,3,4}
SET_2 = {4,5,6,7,8,9,10}
# "|" is used to combine two or more sets together
print(SET_1 | SET_2)
# "&" is used to print the values that intersect or are common in both sets
print(SET_1 & SET_2)
# - means only values in set_1
print(SET_1 - SET_2)
#"^" this excludes the common values in the printed values
print(SET_1 ^ SET_2)


def only_diff_elements(set_1, set_2):
    unique_values = (set_1 ^ set_2)
    return unique_values
set_1 = { "Python", "C", "Javascript" }
set_2 = { "Bash", "C", "Ruby", "Perl" }
od_set = only_diff_elements(set_1, set_2)
print(sorted(list(od_set)))