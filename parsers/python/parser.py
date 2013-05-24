#!/usr/bin/python
#
# WordExplorer
#
#
import sys, getopt
import json

class Parser(object):
    """Provides methods for parsing a text document into a JSON document
    suitable for display as a word tree."""
    
    def parse(self, str):
        """Tokenize the provided text into individual words, and then 
        iterate over the collection, building up a comprehensive list of all
        sets of words  
        document."""
        
        # Naively tokenize on whitespace
        words = str.split()
        
        # The data structure to hold the parsed result
        wordlist = {}
        
        # Iterate over the tokenized words to build the wordlist
        for index,word in enumerate(words):
        
            # Obtain the last (left) n words (n <= 5)
            left_words = words[max(0,index-5):index]
            
            # Obtain the next (right) n words (n <= 5)
            right_words = words[index+1:min(len(words),index+6)]
        
            # If this is a new word, add it to the word list
            if word not in wordlist:
                wordlist[word] = { 'lefts': [left_words], 'rights': [right_words] }
            # Otherwise, append the latest left/right pairs to the existing list
            else:
                wordlist[word]['lefts'].append(left_words)
                wordlist[word]['rights'].append(right_words)
       
        # Convert the wordlist to JSON
        return json.dumps(wordlist)
       

if __name__ == '__main__':

    inputfile = ''
    var_name = ''
    
    # Parse provided options
    try:
        opts, args = getopt.getopt(sys.argv[1:],"hv:i:")
    except getopt.GetoptError:
        print sys.argv[0], '-i <inputfile> [-v <varname>]'
        sys.exit(2)   
    for opt, arg in opts:
        if opt == '-h':
            print sys.argv[0], '-i <inputfile> [-v <varname>]'
            sys.exit()
        elif opt == '-i':
            inputfile = arg
        elif opt == '-v':
            var_name = arg
            
    # Open the input file and parse its contents
    try: 
        with open(inputfile) as f:
            parser = Parser()
            result = parser.parse(f.read())
            if var_name:
                print "var", var_name, "=", result
            else:
                print result
    except Exception as e:
        print "Error:",e
        sys.exit(2)
            
    
    
       
       
                
                
                
            
        
        

