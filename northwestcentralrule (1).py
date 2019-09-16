#only prints Allocations
def dis():
    for i in range(3):
        print(mat[i])
def nwcr():
    print("nwcr:")
    r=0
    c=0
    #checks if we are within the limits of table
    #makes allotments according to specified rules
    while r<3 and c<4:
        if dem[c]>sup[r]:
            dem[c]-=sup[r]
            mat[r][c]=sup[r]
            sup[r]=0
            r=r+1
        elif sup[r]>dem[c]:
            sup[r]-=dem[c]
            mat[r][c]=dem[c]
            dem[c]=0
            c=c+1
        else:
            mat[r][c]=sup[r]
            sup[r]=0
            dem[c]=0
            r=r+1
            c=c+1
        dis()
#giving input & Defining Variables
mat=[[0 for i in range(4)] for i in range(3)]
cost=[[21,16,15,3],[17,18,14,21],
      [32,27,18,41]]
sup=[11,13,19]
dem=[6,10,12,15]
nwcr()
            
        
    
