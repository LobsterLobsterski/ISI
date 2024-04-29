with open("template.txt") as f:
    data = f.read()


tasks = [30, 36, 26, 12]

section=2

for num_of_tasks in tasks:
    for i in range(1, num_of_tasks+1):
        data = data.replace(f"{section}_0", f"{section}_{i}", 1)
    section+=1

with open("README.md", 'w') as f:
    f.write(data)
