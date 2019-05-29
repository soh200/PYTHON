class rectangle:
    length=5
    width=4
    a=0;
    def area(arg):
        arg.a=arg.length*arg.width
        
        return arg.a
rec=rectangle();
print(rec.area());
