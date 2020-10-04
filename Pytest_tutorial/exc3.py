'''

Prepare function which is sort list contains names:
-in alphabetical order of the first letter
-in alphabetical order of the last letter
-by name lenght


'''


class Sorter:

    def sorter(self, names, first_letter = False, last_letter = False, length = False):
        if first_letter:
            names.sort()

        if last_letter:
            names.sort(key=lambda name: name[::-1])

        if length:
            names.sort(key = len)

        return names
