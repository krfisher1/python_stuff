#This is the plan for the chessboard#


'''


This is the starter file. Only fill in the areas indicated.
Do not modify existing code.
Replace this file header with the normal file header (name, etc)


#### End Add Import Statement(s) ####
def main():
    start_positions = input(Enter a starting position: ) 
    width = input(Enter your width)
    height = input(Enter the height: )
    pos = start_positions.slip(",")
    startX = pos[0]
    startY = pos[1]

    if width == "" and height == "":
        drawChessboard(startX, startY)
    elif height == "":
        drawChessboard(startX, startY, width=eval(width))
    elif width == "":
        drawChessboard(startX, startY, height=eval(height))
    else:
        drawChessboard(startX, startY, eval(width), eval(height))
main()



'''
