import numpy as np

class putOption:
    def __init__(self, S0, r, u, d, K, T, n):
        self.S0 = S0 
        self.r = r
        self.u = u
        self.h = T/n
        self.d = d
        self.T = T
        self.K = K
        self.n = n
    
    
    def S_tree(self):
        St = np.zeros((self.n+1,self.n+1))
        for i in range(self.n+1):
            for j in range(i+1):
                St[j,i] = self.S0*(self.u**(i-j))*(self.d**(j))
        return St
    
    def European(self, St):
        tilde_p = (1+self.r*self.h - self.d)/ (self.u - self.d)
        tilde_q = 1-tilde_p
        
        Ep = np.zeros((self.n+1,self.n+1))
        for i in range(self.n+1):
            Ep[i,self.n] = max(self.K-St[i,self.n],0)
            
        
        for i in range(self.n-1,-1,-1):
            for j in range(i+1):
                Ep[j,i] = 1+(1+self.r*self.h)*(tilde_p*Ep[j,i+1]+ tilde_q*Ep[j+1,i+1])
        
        return Ep
        
    def American(self, St):
        tilde_p = (1+self.r*self.h - self.d)/ (self.u - self.d)
        tilde_q = 1-tilde_p
        
        Ap = np.zeros((self.n+1,self.n+1))
        for i in range(self.n+1):
            Ap[i,self.n] = max(self.K-St[i,self.n],0)
        
        for i in range(self.n-1,-1,-1):
            for j in range(i+1):
                Ap[j,i] = max(max(self.K-St[i,self.n],0), 1+(1+self.r*self.h)*(tilde_p*Ap[j,i+1]+ tilde_q*Ap[j+1,i+1]))
        
        return Ap
                
            