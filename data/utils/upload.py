import os
import requests

opts = []
for name in os.listdir():
  if name[-len("qual_guesses.resorted.pred"):] == "qual_guesses.resorted.pred":
    opts.append(name)
print(name)


for name in opts:
  def get_score(filename):
    files = {
      'file': open(filename, 'rb')
      }
    data = {
        'teamid': 'qfwgcbmu',
        'valset': '2'
      }
    r = requests.post('http://cs156.caltech.edu/scoreboard', files=files, data=data)
    assert(r.status_code == 200)
    try:
      score = float(r.text.strip().split()[54])
      print(filename, score)
    except:
      print(r.text)

  get_score(name)

