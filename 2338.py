#2338 - Morse
morsedic = {'.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f','--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l','--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r','...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x','-.--':'y','--..':'z','|':' '}
n = int(input())
for x in range(n):
    wmorse = input().replace("......"," | ").replace("===","-").replace("..."," ").replace(".","").replace("=",".").split(" ")
    morse = ""
    for y in wmorse:
        morse = morse + morsedic[y]
    print(morse)