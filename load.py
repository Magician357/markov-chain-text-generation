print("""Which text(s) to load?
1. Catching Fire
2. Shakespeare
3. Tf2 updates
(split by comma)""")
choice=input(":")
text=""
if "1" in choice:
    with open("texts/catching_fire.txt","r") as f:
        texts=f.read()
        text+="--SPLITTER--".join(texts.split(""" | P a g e 



Catching Fire - Suzanne Collins """))
if "2" in choice:
    with open("texts/shakespeare.txt","r") as f:
        texts=f.read()
        text+="--SPLITTER--".join(texts.split("Scene"))
if "3" in choice:
    with open("texts/shakespeare.txt","r") as f:
        texts=f.read()
        text+="--SPLITTER--".join(texts.split("Team Fortress 2 Update Released"))
        
with open("input.txt","w") as f:
    f.write(text)