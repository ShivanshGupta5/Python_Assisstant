def introduce():
    with open( "introduction.txt" , "r" ) as fd :
            talk(fd.read( ))
