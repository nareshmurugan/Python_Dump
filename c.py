f=222
while (block := f.read(256)) != '':
    process(block)
