with open("followers.txt") as followers:
    contents = followers.read()
    with open("following.txt") as following:
        following_lines = following.readlines()
        for i in range(len(following_lines)):
            if following_lines[i] not in contents:
                print(following_lines[i])

        following.close()
followers.close()

