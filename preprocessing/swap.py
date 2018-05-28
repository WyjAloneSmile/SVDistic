open("residuals.dta", 'w').close()

with open("residuals.dta", "a") as res:
  with open("res.txt", "r") as raw_res:

    with open("all.idx", "r") as idx:
      with open("all.dta", "r") as dta:

        for line_dta, line_idx in zip(dta, idx):

          line_parts = line_dta.split(" ")
          current_idx = int(line_idx.strip())

          if current_idx in [1, 2, 3]:
            res.write(",".join(
              [line_parts[0], line_parts[1], next(raw_res)]
            ))

