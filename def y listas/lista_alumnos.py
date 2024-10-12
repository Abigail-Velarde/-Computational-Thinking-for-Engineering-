"""Este programa guarda un archivo."""

def main():
    outfile=open("alumnos.txt","w")
    
    outfile.write("Daniel Velarde\n")
    outfile.write("Dafne Renteria\n")
    outfile.write("Oscar Castillo\n")
    outfile.write("Vanessa Gomez\n")
    outfile.write("Adriana Islas\n")
    
    outfile.close()
    
main()    