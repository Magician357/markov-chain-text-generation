from random import choice

def compile_dict(cur_dict):
    # Turns the dictionary model into a tuple for easier random choosing
    curpos=()
    for key in cur_dict:
        addon=tuple(key for _ in range(cur_dict[key]))
        curpos=curpos+addon
    return tuple(curpos)

class chain:
    def __init__(self,corpus:tuple,state_size:int):
        self.corpus,self.state_size=corpus,state_size
        self.model=self.build(corpus,state_size)
    
    def build(self,corpus,state_size):
        cd={}
        for text_in in corpus: # for each text in the corpus
            text=tuple("__BEGIN__" for _ in range(state_size))+text_in+("__END__",) # append beginning and end tokens
            for i in range(len(text)-state_size):
                state=tuple(text[i:i+state_size]) # current state
                next=text[i+state_size] # next token
                if state not in cd: # add to current directory if not already in
                    cd[state]={}
                if next not in cd[state]: # add to current directory if not already in
                    cd[state][next]=0
                cd[state][next]+=1 # increment by 1
        return cd
    
    def generate_next(self,state):
        return choice(compile_dict(self.model[tuple(state)]))
    
    def generate(self,max_len=10000,min_len=0):
        current=["__BEGIN__" for _ in range(self.state_size)] # add starting tokens
        for _ in range(max_len):
            state=current[len(current)-self.state_size:len(current)] # get current state
            current.append(self.generate_next(state)) # add next token
            if current[-1] == "__END__": # if algorithm generates end
                if len(current) >= min_len: # end if length is greater then min_len
                    return current
                else:
                    current.pop() # force to continue
                    
                    
def display_generation(generated,con=" "):
    # Takes the generated list and turns it into a readable string
    current=""
    for word in generated:
        if word in ("__BEGIN__", "__END__"):
            continue
        current+=word+con
    return current


if __name__ == "__main__":
    print("loading...")
    
    with open("input.txt","r") as f:
        text=f.read()
    parts=text.split("Catching Fire - Suzanne Collins")
    # splitted=tuple(tuple(thing.split(" ")) for thing in parts)
    splitted=tuple(tuple([*thing]) for thing in parts)
    
    # print(splitted[-1])
    # input()
    
    print("creating model...")
    
    model=chain(splitted,3)
    
    # print(model.model)
    # input()
    
    print("generating text...")
    
    generated=model.generate(max_len=10000,min_len=1000)
    
    display=display_generation(generated,"")
    print(display)
    
    with open("output.txt","w") as f:
        f.write(display)