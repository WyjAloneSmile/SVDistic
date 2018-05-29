docker-machine scp "awsres:/home/ubuntu/data/saves/*-inferred.txt" ../saves/

python3 recorrelate.py
for i in $( ls | grep _guesses ); do
  sort -k2,2n -k1,1n -t"," -o $i.resorted $i
  rm $i
done 
python score_only.py
rm *.resorted
python3 add_residuals.py
python3 upload.py

