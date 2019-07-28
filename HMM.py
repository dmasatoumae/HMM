import numpy as np
def tre_matrix():
    #遷移確率
    a=np.array([
        [0.6,0.4],
        [0.7,0.3],
        [0.5,0.5]
        ])
    #出力確率
    b=np.array([
        [0.8,0.2],
        [0.2,0.8],
        [0.6,0.4]
        ])
    #RBRR
    c=np.array([0,1,0,0])
    return a,b,c

def keisan(a,b,c):

    tre=np.array([
        [0.0,0.0,0.0,0.0,0.0],
        [0.0,b[0][c[0]],b[0][c[1]],0.0,0.0],
        [0.0,0.0,b[1][c[1]],b[1][c[2]],0.0],
        [0.0,0.0,0.0,b[2][c[2]],b[2][c[3]]]])
    print(tre)


    for i in range(3):

        for j in range(4):

            if(i==0)and(j==0):
                tre[i+1][j+1]=tre[i+1][j+1]
            else:
            
                tre[i+1][j+1]=tre[i+1][j+1]*tre[i][j]*a[i-1][1]+tre[i+1][j+1]*tre[i+1][j]*a[i][0]
                
        
    kekka=tre[3][4]*a[2][1]

    return kekka,tre

#def viterbi(tre):
    
#    for i range(4):
#        if 
#def 
def main():
    a,b,c=tre_matrix()
    kakuritu,treris=keisan(a,b,c)
    
    print(treris)
    print("確率＝")
    print(kakuritu)



    
if __name__ == "__main__":
    main()
