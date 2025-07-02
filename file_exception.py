try:
    file=open("example1.txt",'r')
    content=file.read()
    a=b
    print(content)
except FileNotFoundError:
    print("the file not exists")
except Exception as ex:
    print(ex)
finally:
    
    if 'file' in locals() and not file.close():
        print("file closed")