import os


for name in os.listdir():

#   if name[-len("probe_guesses.resorted.txt"):] == "probe_guesses.resorted.txt":
#     open(name[:-4] + ".pred", "w").close()
#     with open(name[:-4] + ".pred", "a") as fw:
# 
#       with open("probe_text.txt", "r") as fi:
#         with open(name, "r") as fy:
#           for inp, guess in zip(fi, fy):
#             fw.write(str((float(inp.strip()) + float(guess.strip()))) + "\n")

  if name[-len("qual_guesses.resorted.txt"):] == "qual_guesses.resorted.txt":
    open(name[:-4] + ".pred", "w").close()
    with open(name[:-4] + ".pred", "a") as fw:

      with open("qual_text.txt", "r") as fi:
        with open(name, "r") as fy:
          for inp, guess in zip(fi, fy):
            fw.write(str((float(inp.strip()) + float(guess.strip()))) + "\n")

