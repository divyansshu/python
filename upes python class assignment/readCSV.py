#program to read csv file and return a list.

filename = 'data.csv'

#function to read csv file and return a list
def read_csv(filename):
    ext = filename.split('.')[-1].lower()
    assert ext == 'csv', "File must be a csv file"
    
    filehandle = open(filename, 'r')
    data = filehandle.read()
    filehandle.close()
    

    #split data by lines
    lines = data.split('\n')
    
    #split each line by commas
    # op = [list(map(lambda x: int(x.strip('"')), line.split(','))) for line in lines if line]
    
    for i in range(len(lines)):
        lines[i] = [int(x.strip('"')) for x in lines[i].split(',')]
        
    op = lines 

    return op #it should return a list of list
    
receivedData = read_csv(filename)
print(receivedData)