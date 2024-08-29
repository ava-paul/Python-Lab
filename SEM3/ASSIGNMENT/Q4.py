A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
joined_AB = A.union(B)
print("Joined A and B (A ∪ B):", joined_AB)
intersection_AB = A.intersection(B)
print("Intersection of A and B (A ∩ B):", intersection_AB)
is_A_subset_B = A.issubset(B)
print("Is A a subset of B?:", is_A_subset_B)
are_A_B_disjoint = A.isdisjoint(B)
print("Are A and B disjoint sets?:", are_A_B_disjoint)
joined_A_with_B = A.union(B)
joined_B_with_A = B.union(A)
print("Join A with B:", joined_A_with_B)
print("Join B with A:", joined_B_with_A)
symmetric_difference_AB = A.symmetric_difference(B)
print("Symmetric difference between A and B:", symmetric_difference_AB)
del A
del B
try:
    print(A)
    print(B)
except NameError:
    print("Set A & B have been deleted.")
