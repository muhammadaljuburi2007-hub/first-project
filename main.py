"""
codex

"""
secr={'a' : "30" , 'b' : "87", 'c' : "67",'d' : "65",'e' : "63", 'f' : "58",'g' : "56",'h' : "54",'i' : "52",'j' : "50",'k' : "49",'l' : "47",'m' : "45",'n' : "43",'o' : "41",'p' : "38",'q' : "36",'r' : "34",'s' : "32",'t' : "30",'u' : "29",'v' : "27",'w' : "25",'x' : "23",'y' : "21",'z' : "18",' ' : "16",'?' : "14",'.' : "12",'!' : "10",'0' : "09",'1' : "07",'2' : "05",'3' : "03", '4' : "01",'5' : "02",'6' : "04",'7' : "06",'8' : "08",'9' : "11"}
decr={"30" : 'a' ,"87" : 'b' ,"67" : 'c' ,"65" : 'd',"63" : 'e',"58" : 'f',"56" : 'g',"54" : 'h',"52" : 'i',"50" : 'j',"49" : 'k',"47" : 'l',"45" : 'm',"43" : 'n',"41" : 'o',"38" : 'p',"36" : 'q',"34" : 'r',"32" : 's',"30" : 't',"29" : 'u',"27" : 'v',"25" : 'w',"23" : 'x',"21" : 'y',"18" : 'z',"16" : ' ',"14" : '?',"12" : '.',"10" : '!',"09" : '0',"07" : '1',"05" : '2',"03" : '3',"01":'4',"02" : '5',"04" : '6',"06" : '7',"08" : '8',"11" : '9',    }
#-----DEFS----


def secros(secr,textt) :
    text= textt.lower()
    ule = ""
    for i in text :
        if i in secr :
            ule = ule + secr[i]
        elif i not in secr :
            ule = ule + i
    return ule



 
def decros(decr ,text):
    ll = 0 
    mm = ""
    nn = ""
    l = 0

    for i in text :
        ll =+ 1
        l = ll % 2
        if l == 0 :
            nn = nn + i
            xx = decr[nn]
            mm = mm + xx
        elif l != 0 :
            nn = i
    return mm



#---RUNNING---CODE---
sld = str(input("1 to code , 0 to decode : ")).strip()
if sld == '1' :
    sld = str(input("your text : "))    
    sld = sld.lower()
    print (secros(secr,sld))
elif sld == '0' :
    sld = str(input("your text : ")).strip()
    print (decros(decr,sld))



