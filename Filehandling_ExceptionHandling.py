while True:    
    try:
        file_name = input("Enter the file name")
        o = open(file_name,'r')
    except FileNotFoundError:
        print("File not found")
    except PermissionError:
        print("Permission is denied")
    except Exception:
        print("Unexpected error")
    else:
        data = o.read()
        print(data)
    finally:
        o.close()
        print("task completed file closed")
