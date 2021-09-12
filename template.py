import os

os.path.join

dirs =[
    os.path.join("data","raw"),
    os.path.join("data","processed"),
    "notebooks",
    "saved_models",
    "src"
] 

for dir_ in dirs:
    os.makedirs(dir_,exist_ok=True) # To check if file is already created and if not create new one

    # Add empty file gitkeep inside folder 
    # If you will not mention write then it will give error as it will not be able to create new file.
    with open(os.path.join(dir_,".gitkeep"),"w") as f: 
        pass

files = [
    "dvc.yaml",
    "params.yaml",
    ".gitignore",
    os.path.join("src","__init__.py"),
]

for file_ in files:
    with open(file_,"w") as f:
        pass