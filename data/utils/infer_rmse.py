import math, os

opts = []

for name in os.listdir():
  if name[-len("probe_guesses.resorted.pred"):] == "probe_guesses.resorted.pred":
    opts.append(name)
print(name)

for name in opts:
  count = 0
  score = 0
  with open(name, "r") as f:
    with open("../corpus/probe.data", "r") as fr:
      for p, y in zip(f, fr):
        px = float(p.strip())
        py = float(y.strip().split(",")[2])
        x = float(px - py)
        score += x * x
        count += 1
  score = math.sqrt(score / count)
  print(name[:-len("probe_guesses.resorted.pred")])
  print(score)

