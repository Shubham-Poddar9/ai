def win (b,p):
    return any(all(b[i]==p for i in line) for line in [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(2,4,6),(0,4,8)])
def nmb(b,p):
    w=win(b,'0'),win(b,'x')
    if w[0]: return 1, None
    if w[1]: return -1, None
    if ' ' not in b:return 0,None

    best=(-2,None) if p=='0'else (2,None)
    for i in[j for j,v in enumerate(b) if v==' ']:
        b[i]=p
        sc,_=nmb(b,'x' if p=='0' else '0')
        b[i]=' '
        if(p=='0' and sc> best[0]) or (p=='x' and sc> best[0]):
            best=(sc,i)
    return best

b=[' ']*9
while True:
    print("\n".join(" ".join(b[i] if b [i] != ' ' else '.' for i in range(r,r+3))for r in(0,3,6)))
    if win(b,'x')or win (b,'0')or ' 'not in b:
        break
    if b.count('x')<=b.count('0'):
        move= int(input('Move (0_8)'))
        if b[move]==' ':b[move]='x'
    else:
        b[nmb(b,'0')[1]]='0'