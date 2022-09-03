followers = set()
update = set()

followers.add(1)
followers.add(2)
followers.add(3)

update.add(4)
update.add(5)
update.add(6)
update.add(7)

print(followers)
print(update)

followers.update(update)

print(followers)