import hashlib


def solve(input):
  i = 0
  while True:
    md5 = md5_hash(input + str(i))
    if md5.startswith('000000'):
      print 'Hash of %i starts with 000000!' % i
      break
    i += 1


def md5_hash(s):
  m = hashlib.md5()
  m.update(s)
  return m.hexdigest()


input = "ckczppom"


if __name__ == "__main__":
  solve(input)
