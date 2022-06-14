def instructorWithLongestName(instructors):
    i=0
    h = {}
    for p in instructors:
        for k,y in p.items():
            if k == 'name' or k == 'course':
                j = len(y)
                if len(y) > i:
                    i = len(y)
                    l= { k: y }
                    h.update(l)
                else:
                    continue
            else:
                continue
    e = h  
    c = e.values()
    for p in instructors:
        for k, y in p.items():
            if y in c:
                return p
            else:
                continue
    return(p)
    
    

        
               
print(instructorWithLongestName([
  {"name": "Samuel", "course": "iOS"},
  {"name": "Jeremiah", "course": "Data"},
  {"name": "Ophilia", "course": "Web"},
  {"name": "Donald", "course": "Web"}
]))
print(instructorWithLongestName([
  {"name": "Matthew", "course": "Data"},
  {"name": "David", "course": "iOS"},
  {"name": "Domascus", "course": "Web"}
]))