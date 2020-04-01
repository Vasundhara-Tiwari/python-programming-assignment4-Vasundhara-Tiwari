def flatten_Dictionary ( nestedDictionary , Dictionary , currentKey ):
    for i in nestedDictionary.keys():
        if type ( nestedDictionary [ i ] ) == int :
            Dictionary [ ( currentKey + "." + i ) . strip ( "." ) ] = nestedDictionary [ i ]
        else:
            Dictionary = flatten_Dictionary ( nestedDictionary [ i ] , Dictionary , (currentKey + "." + i ) . strip ( '.' ) )
    return Dictionary

user_input = eval ( input (" Enter your nested dictionary in its original nested form    :    " ) )
print( flatten_Dictionary ( user_input , dict() , "" ) )