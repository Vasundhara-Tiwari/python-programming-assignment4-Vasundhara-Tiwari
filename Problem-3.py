user_input = eval ( input( "Enter all the elements of suggestion list in the list form  :   " ) )
Query = input ( "Enter the Query String   :   " )
Temp = [ ]
for i in user_input:
      if i.startswith ( Query ) :
          Temp.append( i )
      else:
          pass
print ("Here are your suggestions   : ")
length = 0
for k in Temp :
    length = length + 1
for j in Temp :
    length = length - 1
    if length > 0:
        print( j , end = ", " )
    else:
        print( j )