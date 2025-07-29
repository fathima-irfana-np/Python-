with open("global.txt", "r") as f:
    with open("zebraaaa.txt", "x") as f1:

        content=f.read()
        print(content)
        lines=content.split('.')
        newline=""
        for sentence in lines:
            sentence=sentence.strip().capitalize()
            newline+=sentence+' .'
        print(newline)
        f1.write(newline)



