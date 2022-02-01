import chess
import chess.pgn
from stockfish import Stockfish
import os

def get_evaluation(current_evaluation):
    if current_evaluation["type"]=="mate":
        
        return str("M"+str(current_evaluation["value"]))
    else:
        return str(float(current_evaluation["value"])/100)



stockfish = Stockfish(path="stockfish")
current_directory = os.getcwd()

pgn_file = input("Enter pgn file: ")

try:
    gamepgn = open(pgn_file)
except:
    print("PGN file is not corrent.")
    exit()

generate_from_pgn = chess.pgn.read_game(gamepgn)

print("Enter name of analysis Folder: ",end=" ")
dir_name=input()
os.mkdir(dir_name)

board = generate_from_pgn.board()
print(board)
stockfish.set_position([])

board_visual = stockfish.get_board_visual()

dir_path=dir_name+"/"

svg_visual = chess.svg.board(board, size=500)  
f = open(dir_path+"0.svg","w")
f.write(svg_visual)

no_of_moves=2

print(generate_from_pgn.mainline_moves())

sc=open(dir_path+"script.js","w")
sc.write("const evalution ={\n0:'0',\n")

for move in generate_from_pgn.mainline_moves():

    board.push(move)
    peeked=board.peek()
    #print(peeked)
    
    print("move: ",int(no_of_moves/2))
    
    if no_of_moves%2==0:
        print("White's Turn: ")
    else:
        print("Black's Turn: ")
    
    no_of_moves+=1
    
    stockfish.make_moves_from_current_position([peeked])
    
    board_visual = stockfish.get_board_visual()

    svg_visual = chess.svg.board(board, size=500)  
    f = open(dir_path+str(no_of_moves-2)+".svg","w")
    f.write(svg_visual)

    #print(svg_visual)

    print(board_visual)

    if board.is_checkmate():
        str_evalution="!!CheckMate: "
        if no_of_moves%2==0:  
            str_evalution = str_evalution + " Black Wins !!"
            print("!!CheckMate: ","Black Wins!!")
            sc_write_statement = str(no_of_moves-2) + ": '" + str_evalution + "',\n"
            sc.write(sc_write_statement)
        else:
            str_evalution = str_evalution + " White Wins !!"
            print("!!CheckMate: ","White Wins!!")
            sc_write_statement = str(no_of_moves-2) + ": '" + str_evalution + "',\n"
            sc.write(sc_write_statement)
        break

    current_evaluation = stockfish.get_evaluation()

    print("Evaluation: ",end="")

    str_evalution = get_evaluation(current_evaluation)
    sc_write_statement = str(no_of_moves-2) + ": '" + str_evalution + "',\n"
    sc.write(sc_write_statement)


sc.write("}\n")
sc.write("total_moves="+str(no_of_moves-2))
sc.write("\n")
current_sc=open("template_script.js","r")
sc.write(current_sc.read())

temp_index=open("template_index.html",'r')
new_index=open(dir_path+"index.html",'w')
new_index.write(temp_index.read())
new_index.close()
print("\nAll analysis files are ready....")
#os.startfile(dir_path+"index.html")