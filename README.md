create env

'''bash
conda create -n wineq python=3.7 -y
'''

activate env

'''bash
conda activate wineq
'''

created a requirements.txt file

install the req

'''bash
pip install -r requirements.txt 
'''

Download the data:- https://drive.google.com/drive/folders/1xw0XX-WK74uxtFFLySbtnX-ODdmdK5Ec

git init
dvc init
dvc  add  data_given/winequality.csv
git add .
git commit -m "First commit"

git add . && git commit -m "update README.md"