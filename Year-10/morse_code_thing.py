
def morse(text):
    encrypt = {"a"	 : "*-",
               "b"	 : "-***",	
               "c"	 : "-*-*",	
               "d"	 : "-**",	
               "e"	 : "*",	    
               "f"	 : "**-*",	
               "g"	 : "--*",	  
               "h"	 : "****",	
               "i"	 : "**",   
               "j"	 : "*---",	
               "k"  : "-*-",	  
               "l"	 : "*-**",	
               "m"	 : "--",	   
               "n"	 : "-*",	   
               "o"	 : "---",	  
               "p"	 : "*--*",
               "q"  : "--*-",
               "r"	 : "*-*",  
               "s"	 : "***",	  
               "t"	 : "-",	    
               "u"	 : "**-",	  
               "v"	 : "***-",	
               "w"	 : "*--",	  
               "x"	 : "-**-",	
               "y"	 : "-*--",
               "z"	 : "--**",
               " "   : "|"}
    
    #swaps keys and values -> for decryption
    decrypt = {value: key for key, value in encrypt.items()}

    
    if "-" in text or "*" in text:
        return "".join(decrypt[i] for i in text.split())    
    
    return " ".join(encrypt[i] for i in text.lower())



text = input("Enter here: ")


print(morse(text))

