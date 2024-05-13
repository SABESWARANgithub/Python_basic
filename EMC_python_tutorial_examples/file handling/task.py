with open("task.txt","r+") as fi:
    print(fi.writable())
    print(fi.readable())
    print(fi.readlines())

    fi.write("\n\nMacDonalds has a farm\nEe i ee i o\nIn that from there are some ducks\nEe i ee i oh\nwith a quack-quack here\nAnd a quack-quack there\nhere a quack,there quack-quack")
    print(fi.mode)

    fi.close()
    print(fi.closed)
