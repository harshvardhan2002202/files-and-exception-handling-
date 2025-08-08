# %%
try:
    with open("sample.txt","r") as f:
        lines=f.readlines()
    count=1
    for line in lines:
        print(f"Line {count}: ",line.strip())
        count+=1
    
except FileExistsError:
    print(f"Error:the file sample.txt was not found")
# %%
