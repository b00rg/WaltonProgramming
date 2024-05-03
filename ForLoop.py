n = 4
for i in range(0, n):
    print(i)

print("List Iteration")
l = ["Walton", "Club", "2024"]
for i in l:
    print(i)
print("\nTuple Iteration")
t = ("Walton", "Club", "2024")
for i in t:
    print(i)
print("\nString Iteration")
s = "Walton"
for i in s:
    print(i)
print("\nDictionary Iteration")
d = dict()
d['xyz'] = 123
d['abc'] = 345
for i in d:
    print("%s  %d" % (i, d[i]))
print("\nSet Iteration")
set1 = {1, 2, 3, 4, 5, 6}
for i in set1:
    print(i),

list = ["Walton", "Club", "2024"]
for index in range(len(list)):
    print(list[index])

list_2d = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in list_2d: 
    for element in row: 
        print(element, end=' ')
    print()  

def populate_board(self):
    # Populate pawns
    for i in range(8):
        self.board[1][i] = Pawn("black", i, 1)  
        self.board[6][i] = Pawn("white", i, 6)  
            

