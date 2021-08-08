ada_family = { 'Judith Blunt-Lytton': ['Anne Isabella Blunt', 'Wilfrid Scawen Blunt'],
              'Ada King-Milbanke': ['Ralph King-Milbanke', 'Fanny Heriot'],
              'Ralph King-Milbanke': ['Augusta Ada King', 'William King-Noel'],
              'Anne Isabella Blunt': ['Augusta Ada King', 'William King-Noel'],
              'Byron King-Noel': ['Augusta Ada King', 'William King-Noel'],
              'Augusta Ada King': ['Anne Isabella Milbanke', 'George Gordon Byron'],
              'George Gordon Byron': ['Catherine Gordon', 'Captain John Byron'],
              'John Byron': ['Vice-Admiral John Byron', 'Sophia Trevannion'] }


def ancestors(genealogy, person):
    result = []
    if person in genealogy:
        parents = genealogy[person]
        result.append(parents)
        for parent in parents:
            result += ancestors(genealogy, parent)
        return result
    return []
# print(ancestors(ada_family, 'Judith Blunt-Lytton'))
# print(ada_family)

#>>> ['Anne Isabella Blunt', 'Wilfrid Scawen Blunt', 'Augusta Ada King',
#    'William King-Noel', 'Anne Isabella Milbanke', 'George Gordon Byron',
#    'Catherine Gordon', 'Captain John Byron', 'Catherine Gordon',
#    'Captain John Byron', 'Anne Isabella Milbanke', 'George Gordon Byron',
#    'Catherine Gordon', 'Captain John Byron', 'Catherine Gordon',
#    'Captain John Byron', 'Catherine Gordon', 'Captain John Byron',
#    'Catherine Gordon', 'Captain John Byron']
#
#>>> {'Ralph King-Milbanke': ['Augusta Ada King', 'William King-Noel'],
#    'Ada King-Milbanke': ['Ralph King-Milbanke', 'Fanny Heriot'],
#    'Anne Isabella Blunt': ['Augusta Ada King', 'William King-Noel', 'Anne Isabella Milbanke', 'George Gordon Byron', 'Catherine Gordon', 'Captain John Byron', 'Catherine Gordon', 'Captain John Byron'],
#    'Augusta Ada King': ['Anne Isabella Milbanke', 'George Gordon Byron', 'Catherine Gordon', 'Captain John Byron', 'Catherine Gordon', 'Captain John Byron'],
#    'Judith Blunt-Lytton': ['Anne Isabella Blunt', 'Wilfrid Scawen Blunt', 'Augusta Ada King', 'William King-Noel', 'Anne Isabella Milbanke', 'George Gordon Byron', 'Catherine Gordon', 'Captain John Byron', 'Catherine Gordon', 'Captain John Byron', 'Anne Isabella Milbanke', 'George Gordon Byron', 'Catherine Gordon', 'Captain John Byron', 'Catherine Gordon', 'Captain John Byron', 'Catherine Gordon', 'Captain John Byron', 'Catherine Gordon', 'Captain John Byron'],
#    'Byron King-Noel': ['Augusta Ada King', 'William King-Noel'],
#    'George Gordon Byron': ['Catherine Gordon', 'Captain John Byron'],
#    'John Byron': ['Vice-Admiral John Byron', 'Sophia Trevannion']}


a = 2  #不可更改对象
b = a
a = 5
print(a,b)   #5 2

a = [1, 2, 5]
b = a
a = [2, 5, 9]
print(a, b)  #[2, 5, 9] [1, 2, 5]

a = [1, 2, 5]  #可更改对象
b = a
a[0] = 9
print(a, b)  #[9, 2, 5] [9, 2, 5]