def solve(input, num_steps):
  out = input
  for _ in xrange(num_steps):
    out = look_and_say(out)
  print len(out)


def look_and_say(s):
  curr_char = s[0]
  curr_count = 0
  res = ""
  for c in s:
    if curr_char == c:
      curr_count += 1
    else:
      res += "%d%s" % (curr_count, curr_char)
      curr_char = c
      curr_count = 1
  res += "%d%s" % (curr_count, curr_char)
  return res


input = "1113122113"


if __name__ == "__main__":
  solve(input, 50)
