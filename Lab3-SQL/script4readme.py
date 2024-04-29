#takes base template and creates a readme.md file
def generate_readme_from_template():
    with open("template.txt") as f:
        data = f.read()


    tasks = [30, 36, 26, 12]

    section=2

    for num_of_tasks in tasks:
        for i in range(1, num_of_tasks+1):
            data = data.replace(f"images\\{section}_0", f"images/{section}_{i}", 1)
        section+=1

    with open("README.md", 'w') as f:
        f.write(data)

#renames names of images to 2_1, 2_2, ..., 5_12 based on Date modified
def rename_images():
    import glob
    import os

    search_dir = "images/"
  
    files = list(filter(os.path.isfile, glob.glob(search_dir + "*")))
    files.sort(key=lambda x: os.path.getmtime(x))
    
    tasks = [30, 36, 26, 12]

    section=2
    file_idx = 0

    for num_of_tasks in tasks:
        for i in range(1, num_of_tasks+1):
            os.rename(files[file_idx], f'images/{section}_{i}.png')
            file_idx+=1
        section+=1

if __name__ == '__main__':
    rename_images()
    print('finished')
