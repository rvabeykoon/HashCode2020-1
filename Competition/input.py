filename = 'a_example.txt'
# filename = 'b_read_on.txt'
# filename = 'c_incunabula.txt'
# filename = 'd_tough_choices.txt'
# filename = 'e_so_many_books.txt'
# filename = 'f_libraries_of_the_world.txt'

file = open(filename, 'r')
lineCount = 0

B = 0
L = 0
D = 0
bookScores = []

libraryNumBooks = []
librarySignupDays = []
libraryShipPerDay = []
libraryBookIDs = []


# Reading file
for line in file:
    line = line.strip()
    line = line.split(' ')

    if line == ['']:
        lineCount += 1
        continue
    
    line = list(map(int, line))
    
    if lineCount == 0:
        B = line[0] # number of different books
        L = line[1] # number of libraries
        D = line[2] # number of days
    elif lineCount == 1:
        bookScores = line # scores of each book
    else:
        if lineCount % 2 == 0:
            N = line[0] # number of books in library
            T = line[1] # number of days to finish library signup
            M = line[2] # number of books that can be shipped per day
            libraryNumBooks.append(N)
            librarySignupDays.append(T)
            libraryShipPerDay.append(M)
        else:
            IDs = line # book IDs
            libraryBookIDs.append(IDs)

    lineCount += 1

file.close()