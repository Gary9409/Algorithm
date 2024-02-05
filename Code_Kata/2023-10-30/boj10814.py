import sys

members = []
for i in range(int(sys.stdin.readline())):
    age, name = sys.stdin.readline().split()
    members.append((int(age), name))
print(sorted(members, key=lambda x: x[0]))