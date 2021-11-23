import os

os.name

# print(os.uname())

# os.uname()

start_path = os.getcwd()
print(start_path)

print(os.listdir())

print(os.listdir("..")[:5])

print(os.listdir("/")[:5])

print(os.getcwd())

print(os.chdir(".."))
print(os.getcwd())