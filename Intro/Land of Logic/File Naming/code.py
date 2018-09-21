def fileNaming(names):
    nm = [];
    s = set();
    for name in names:
        i = 1;
        temp = name
        if name not in s:
            s.add(name)
        else:
            while(True):
                if name + "("+ str(i)+")" not in s:
                    s.add(name + "("+ str(i)+")")
                    temp = name + "("+ str(i)+")"
                    break
                else:
                    i+= 1
                    temp = name + "("+ str(i)+")"
        nm.append(temp)
    return nm;