mem = {}
for i in range(100):
    mem[i] = 0

def bf(s):
    cur = 0
    while len(s) > 0:
        i = s[0]
        if i == "+": mem[cur]+=1
        elif i == "-": mem[cur]-=1
        elif i == ".": print(chr(mem[cur]))
        elif i == ",": mem[cur] = ord(input())
        elif i == "<":
            if cur != 0: cur -=1
        elif i == ">": cur += 1
        elif i == "[":
            m = s[1:s.find("]")]
            o = cur
            while mem[o] != 0:
                for n in m:
                    if n == "+":
                        mem[cur]+=1
                    elif n == "-":
                        mem[cur]-=1
                    elif n == ".":
                        print(chr(mem[cur]))
                    elif n == ",":
                        mem[cur] = ord(input())
                    elif n == "<":
                        if cur != 0: cur -=1
                    elif n == ">":
                        cur += 1
            s = s[len(m)+1:]
        s = s[1:]
    print(mem)


bf(",+++++ > +++++ < ++++++ >>>>> -------- > +++++++ < -------")
