with open("test.txt") as f:
    content = f.readlines()

content = [x.strip() for x in content]
ans = int(content[0])-len(content)
print(ans)