import numpy as np
#import scipy.stats
def first_matrix():
    a=np.array([
        [0.5,0.5],
        [0.5,0.5],
        [0.5,0.5]
        ])


    b=np.array([
        [0.5,0.5],
        [0.5,0.5],
        [0.5,0.5]
        ])

    c=np.array([0,1,1,0])
    
    return a,b,c

def prob_calc(a,b,c):
    #3パターン計算
    one=b[0][c[0]]*a[0][0]*b[0][c[1]]*a[0][1]*b[1][c[2]]*a[1][1]*b[2][c[3]]*a[2][1]

    two=b[0][c[0]]*a[0][1]*b[1][c[1]]*a[1][0]*b[1][c[2]]*a[1][1]*b[2][c[3]]*a[2][1]

    thr=b[0][c[0]]*a[0][1]*b[1][c[1]]*a[1][1]*b[2][c[2]]*a[2][0]*b[2][c[3]]*a[2][1]
    #kake=(1/(one+two+thr))
    #one=kake*one
    #two=kake*two
    #thr=kake*thr

    
    return one,two,thr

def case_prob():
    Aa=np.array([
        [0.5,0.5],
        [0,1],
        [0,1]
        ])
    Ba=np.array([
        [0,1],
        [0.5,0.5],
        [0,1]
        ])
    Ca=np.array([
        [0,1],
        [0,1],
        [0.5,0.5]
        ])

    Ab=np.array([
        [0.5,0.5],
        [0,1],
        [1,0]
        ])
    Ab[0][0]
    Bb=np.array([
        [1,0],
        [0,1],
        [1,0]
        ])
    Cb=np.array([
        [1,0],
        [0,1],
        [0.5,0.5]
        ])
    return Aa,Ba,Ca,Ab,Bb,Cb

def para_upd(a,b,c,one,two,thr,Aa,Ba,Ca,Ab,Bb,Cb):
    
    #パラメータ更新b
    for i in range (3):
        for j in range(2):
            b[i][j]=Ab[i][j]*one+Bb[i][j]*two+Cb[i][j]*thr
            a[i][j]=Aa[i][j]*one+Bb[i][j]*two+Cb[i][j]*thr
        #正規化
        uuub=1/(b[i][0]+b[i][1])
        uuua=1/(a[i][0]+a[i][1])

        b[i][0]=b[i][0]*uuub
        b[i][1]=b[i][1]*uuub

        a[i][0]=a[i][0]*uuua
        a[i][1]=a[i][1]*uuua
        
    
    return a,b

    

def main():
    roop=100
    a,b,c=first_matrix()
    Aa,Ba,Ca,Ab,Bb,Cb=case_prob()
    bef_a=a[0][1]
    #bef_b=b
    #print(bef_a)
    #np.set_printoptions(precision=5)
    for su in range(roop):
        one,two,thr=prob_calc(a,b,c)
        a,b=para_upd(a,b,c,one,two,thr,Aa,Ba,Ca,Ab,Bb,Cb)
        #print(bef_a)
        if su>=1:
            if ((bef_a-a[0][1])**2)**0.5<0.00000000001:
                
                break
        bef_a=a[0][1]
        bef_b=b
    
    a = np.round(a, decimals=4)
    print("a=")
    print(a)
    b = np.round(b, decimals=4)
    print("b=")
    print(b)



    
if __name__ == "__main__":
    main()
