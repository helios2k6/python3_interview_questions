def buildFriendCircle(friends, studentToFriendCircles, rootStudent):
    numStudents = len(friends)
    needsFriendCircle = True
    friendCircleSet = None
    if rootStudent in studentToFriendCircles:
        needsFriendCircle = False
        friendCircleSet = studentToFriendCircles[rootStudent]
    else:
        friendCircleSet = {rootStudent: True}
        studentToFriendCircles[rootStudent] = friendCircleSet

    for otherStudent in range(rootStudent + 1, numStudents):
        if otherStudent in studentToFriendCircles:
            continue
        if friends[rootStudent][otherStudent] == 'Y':
            # This student belongs to the friend circle
            friendCircleSet[otherStudent] = True
            studentToFriendCircles[otherStudent] = friendCircleSet
    return needsFriendCircle

def getAllFriendsAndFoF(friends, takenStudents, rootStudent):
    numStudents = len(friends)
    takenStudents[rootStudent] = True
    for otherStudent in range(rootStudent + 1, numStudents):
        if friends[rootStudent][otherStudent] == 'Y':
            takenStudents[otherStudent] = True
            # get all the friends of this student too
            getAllFriendsAndFoF(friends, takenStudents, otherStudent)

def cycleThroughEverything(friends):
    numStudents = len(friends)
    takenStudents = {}
    numberOfFriendCircles = 0
    for student in range(0, numStudents):
        if student not in takenStudents:
            getAllFriendsAndFoF(friends, takenStudents, student)
            numberOfFriendCircles += 1
    return numberOfFriendCircles

# Complete the friendCircles function below.
def friendCircles(friends):
    numStudents = len(friends)
    studentToFriendCircles = {}
    numberOfFriendCircles = 0
    for student in range(0, numStudents):
        if buildFriendCircle(friends, studentToFriendCircles, student):
            numberOfFriendCircles += 1
    return numberOfFriendCircles

def test1():
    friends = [
        "YYNN",
        "YYYN",
        "NYYN",
        "NNNY"
    ]
    print(friendCircles(friends))
    print(cycleThroughEverything(friends))

def test2():
    friends = [
        "YNNN",
        "NYNN",
        "NNYN",
        "NNNY"
    ]
    print(friendCircles(friends))
    print(cycleThroughEverything(friends))

def test3():
    friends = [
        ""
    ]
    print(friendCircles(friends))
    print(cycleThroughEverything(friends))

test1()
test2()
test3()
