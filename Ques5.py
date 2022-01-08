"""
Question 5:
(a) Print a specified list after removing 4th element i.e. Black.
(b) Remove Black and Pink from the list and replace it with Purple.
"""

color_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

# Print (a) part
print('\n (a)')
print(color_list)
# Remove 4th element that is Black
color_list.remove('Black')
print("\n List after removing Black Color:\n ", color_list)

color_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# Print (b) part
print('\n (b)')
print(color_list)
# Replace Black and Pink with Purple
color_list[3:5] = ['Purple']
print("\n List after replacing Black and Pink with Purple Color:\n ", color_list)
