def checkAir(samples, threshold):
    y = samples.count("clean")
    x = samples.count("dirty")
    z = x/(x+y)
    if z > threshold:
        return ("Polluted")
    else:
        return ("Clean")


print(checkAir(
  ['clean', 'clean', 'dirty', 'clean', 'dirty', 'clean', 'clean', 'dirty', 'clean', 'dirty'],
  0.3
))

print(checkAir(
  ['dirty', 'dirty', 'dirty', 'dirty', 'clean'],
  0.25
))

print(checkAir(
  ['clean', 'dirty', 'clean', 'dirty', 'clean', 'dirty', 'clean'],
  0.9
))