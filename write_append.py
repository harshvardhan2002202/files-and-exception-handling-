try:
    text=input("Enter text to write to a file: ").strip()
    with open("output.txt","a")as f:
        f.write(text+'\n')
    print("Data successfully written to output.txt.")

    text2=input("Enter additional text to append: ").strip()
    with open("output.txt","a")as f:
        f.write(text2+'\n')
    print("Data successfully appended.")

    with open("output.txt","r")as f:
        data=f.readlines()
    print('Final Content of output.txt:')
    for l in data:
        print(l)
except FileNotFoundError:
    print("file does not exists")