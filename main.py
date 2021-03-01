import gzip
import shutil

with open('sample.txt','rb') as f_input:
  with gzip.open('sample.gz','wb') as f_output:
    shutil.copyfileobj(f_input,f_output)