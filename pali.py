import sys,os,getopt
def main(argv):
    c_file=''
    exe_file=''
    opts,args=getopt.getopt(argv,"i:",['ifile='])
    for o, a in opts:
        if o in ("-i","--ifile"):
            c_file=a+'.c'
            exe_file=a+'.exe'
            run(c_file,exe_file)
def run(c_file,exe_file):
    print("Compiling"+c_file)
    os.system('g++'+c_file+'-o'+exe_file)
    print("Running"+exe_file)
    print("_ "*50,end='\n')
    os.system(exe_file)
if __name__=="__main__":
    main(sys.argv[1:])
    
