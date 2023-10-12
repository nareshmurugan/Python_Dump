import sys,os,getopt
def main(argv):
    cpp_file =''
    exe_file =''
    opts,args = getopt.getopt(argv,"i:"['ifile='])
    for o,a in opts:
        if o in("-i","--ifile"):
            cpp_file=a+'.cpp'
            exe_file=a+'.exe'
            run(cpp_file,exe_file)
def run(cpp_file,exe_file):
    print("Compling"+cpp_file)
    os.system('g++'+cpp_file+'-o'+exe_file)
    print("Running"+exe_file)
    print("------------------")
    print
    os.system(exe_file)
    print
if__name__=='__main__':
    main(sys.argv[1:])
