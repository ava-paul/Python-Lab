rep={
    '0':('  -','| |',' ','| |','  -'),
    '1':('  ','  |',' ','  |','  '),
    '2':(' --','   |','  -','|  ',' --'),
    '3':('---','   |','  -','   |','---'),
    '4':('  ','| |','  -','  |','  '),
    '5':('  -','|  ','  -','   |','  -'),
    '6':('  -','|  ',' -','| |','  -'),
    '7':(' --','  |',' ','  |',' '),
    '8':('  -','| |','  -','| |',' -'),
    '9':('  -','| |','  -','   |','  ')
    }
def seven_seg(n):
    digits=[rep[digit]for digit in str(n)]
    for i in range(5):
        print(" ".join(segment[i] for segment in digits))
seven_seg(1)
seven_seg(2)
seven_seg(3)
seven_seg(4)
seven_seg(5)
seven_seg(6)
seven_seg(7)
seven_seg(8)
seven_seg(9)
