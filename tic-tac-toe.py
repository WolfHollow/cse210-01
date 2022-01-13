


def main():
    tl = 1
    tm = 2
    tr = 3
    ml = 4
    mm = 5
    mr = 6
    bl = 7
    bm = 8
    br = 9
    turn = "x"
    inputnum = 0
    game = "playing" 
    turns = 0
    while game == "playing" and turns < 9:
        turns = turns + 1
        game = over(tl,tm,tr,ml,mm,mr,bl,bm,br)
        
        if turn == "x":
            turn = "o"
        else:
            turn = "x"
            
        inputnum = int(input(f"Its {turn}'s turn pick a number betwing 1-9 that hasnt been used yet."))
        if inputnum == 1:
            tl = turn
        elif inputnum == 2:
            tm = turn
        elif inputnum == 3:
            tr = turn
        elif inputnum == 4:
            ml = turn
        elif inputnum == 5:
            mm = turn
        elif inputnum == 6:
            mr = turn
        elif inputnum == 7:
            bl = turn
        elif inputnum == 8:
            bm = turn
        elif inputnum == 9:
            br = turn
        
        if game == "xwon":
            print ("Congrats X")
        elif game == "owon":
            print ("Congrats O")

        print (f"{tl} | {tm} | {tr}")
        print ("--+---+--")
        print (f"{ml} | {mm} | {mr}")
        print ("--+---+--")
        print (f"{bl} | {bm} | {br}")



    
    
    



    

def over(tl,tm,tr,ml,mm,mr,bl,bm,br):
    if tl == "x" and tm == "x" and tr == "x":
        game = "xwon"
    elif ml == "x" and mm == "x" and mr == "x":
        game = "xwon"
    elif bl == "x" and bm == "x" and br == "x":
        game = "xwon"

    elif tl == "x" and ml == "x" and bl == "x":
        game = "xwon"
    elif tm == "x" and mm == "x" and bm == "x":
        game = "xwon"
    elif tr == "x" and mr == "x" and br == "x":
        game = "xwon"

    elif tl == "x" and mm == "x" and br == "x":
        game = "xwon"
    elif bl == "x" and mm == "x" and tr == "x":
        game = "xwon"
    

    elif tl == "o" and tm == "o" and tr == "o":
        game = "owon"
    elif ml == "o" and mm == "o" and mr == "o":
        game = "xwon"
    elif bl == "o" and bm == "o" and br == "o":
        game = "owon"

    elif tl == "o" and ml == "o" and bl == "o":
        game = "owon"
    elif tm == "o" and mm == "o" and bm == "o":
        game = "owon"
    elif tr == "o" and mr == "o" and br == "o":
        game = "owon"

    elif tl == "o" and mm == "o" and br == "o":
        game = "owon"
    elif bl == "o" and mm == "o" and tr == "o":
        game = "owon"

    else:
        game = "playing"

    return game

if __name__ == "__main__":
    main()