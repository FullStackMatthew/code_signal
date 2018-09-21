def areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight):
        return (yourLeft == friendsLeft and yourRight == friendsRight) or (yourRight == friendsLeft and yourLeft == friendsRight)
