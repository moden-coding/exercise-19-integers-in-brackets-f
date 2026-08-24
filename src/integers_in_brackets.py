#!/usr/bin/env python3
import re

def integers_in_brackets(s):
    pass
    
    

def main():
    print(integers_in_brackets(" afd [asd] [12 ] [a34] [ -43 ]tt [+12]xxx")) 
    #Output for the above should be: [12, -43, 12]

    print(integers_in_brackets("  afd [128+] [47 ] [a34]  [ +-43 ]tt [+12]xxx")
    #Output for the above should be: [47, 12]
    
    print(integers_in_brackets("")
    #Output for the above should be: []
    
    

if __name__ == "__main__":
    main()
