def whereCanIPark(spots, vehicle):
    if vehicle == 'regular':
        for i in spots:
            for x in i:
                if x == 'R':
                    return (i.index(x), spots.index(i))
            else:
                return ("false")
    elif vehicle == 'small':
        for i in spots:
            for x in i:
                if x == 'R' or x == 'S':
                    return (i.index(x), spots.index(i))
            else:
                return ("false")
    elif vehicle == 'motorcycle':
        for i in spots:
            for x in i:
                if x == 'R' or x == 'S' or x == 'M':
                    return (i.index(x), spots.index(i))
    else:
        return ("false")

print(whereCanIPark(
  [
   
    ['s', 's', 's', 'S', 'R', 'M'],
    ['s', 'M', 's', 'S', 'r', 'M'],
    ['s', 'M', 's', 'S', 'r', 'm'], 
    ['S', 'r', 's', 'm', 'r', 'M'],
    ['S', 'r', 's', 'm', 'r', 'M'],
    ['S', 'r', 'S', 'M', 'M', 'S']
  ],
  'regular'
))

print(whereCanIPark(
  [
    ['M', 'M', 'M', 'M'],
    ['M', 's', 'M', 'M'],
    ['M', 'M', 'M', 'M'],
    ['M', 'M', 'r', 'M']
  ],
  'small'
))

print(whereCanIPark(
  [
    ['s', 's', 's', 's', 's', 's'],
    ['s', 'm', 's', 'S', 'r', 's'],
    ['s', 'm', 's', 'S', 'r', 's'],
    ['S', 'r', 's', 'm', 'r', 's'],
    ['S', 'r', 's', 'm', 'R', 's'],
    ['S', 'r', 'S', 'M', 'm', 'S']
  ],
  'motorcycle'
))