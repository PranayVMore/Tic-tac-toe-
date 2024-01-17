position=0
print('press r to roll')
print('press q to quit')
import random
def roll(position):
    inp=str(input('- '))
    while inp!='q':
        x=random.randint(1,6)
        if x==1:
            position+=1
        if x==2:
            position+=2
        if x==3:
            position+=3
        if x==4:
            position+=4
        if x==5:
            position+=5
        if x==6:
            position+=6

        print('The dice rolled',x,'step forward!')
         
        print('you were at position',position)
        if position==2:
            position=38
        if position==4:
            position=14
        if position==9:
            position=31
        if position==17:
            position=7
        if position==21:
            position=42
        if position==28:
            position=42
        if position==51:
            position=67
        if position==54:
            position=34
        if position==62:
            position=19
        if position==64:
            position=60
        if position==72:
            position=91
        if position==80:
            position=99
        if position==87:
            position=36
        if position==92:
            position=73
        if position==95:
            position=75
        if position==98:
            position=79
        if position==100:
            print('you won!')
            break
        if position<100:
            print('due to promotion/demotion/no promotion,demotion,your current position is at: ',position)
        if position>100:
            print('impossible move!')
            position=position-x
            print('due to impossible,your position still at: ',position)
            continue
        inp=str(input('-'))

roll(position)
