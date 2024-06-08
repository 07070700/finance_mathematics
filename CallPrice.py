import numpy as np

class CallOption:
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
    
    def European(self):
        St = self.S_tree()
        tilde_p = (1+self.r*self.h - self.d)/ (self.u - self.d)
        tilde_q = 1-tilde_p
        
        Ep = np.zeros((self.n+1,self.n+1))
        for i in range(self.n+1):
            Ep[i,self.n] = max(St[i,self.n]-self.K,0)
            
        
        for i in range(self.n-1,-1,-1):
            for j in range(i+1):
                Ep[j,i] = 1+(1+self.r*self.h)*(tilde_p*Ep[j,i+1]+ tilde_q*Ep[j+1,i+1])
        
        return Ep
        
    def American(self):
        St = self.S_tree()
        tilde_p = (1+self.r*self.h - self.d)/ (self.u - self.d) #up
        tilde_q = 1-tilde_p #down
        
        Ap = np.zeros((self.n+1,self.n+1))
        for i in range(self.n+1):
            Ap[i,self.n] = max(St[i,self.n]-self.K,0)
        
        for i in range(self.n-1,-1,-1):
            for j in range(i+1):
                Ap[j,i] = max(max(St[i,self.n]-self.K,0), 1+(1+self.r*self.h)*(tilde_p*Ap[j,i+1]+ tilde_q*Ap[j+1,i+1]))
        
        return Ap
    
    def statePrice(self,t):
        n_t = self.T-t
        
        tilde_p = (1+self.r*self.h - self.d)/ (self.u - self.d)
        tilde_q = 1-tilde_p
        
        coef = [1] # (p+q)**0
        for i in range(1,n_t+1):
            next_coef = [0] *(len(coef) + 1)
            for j in range(len(coef)):
                next_coef[j] += coef[j]*tilde_p
                next_coef[j+1] += coef[j]*tilde_q
            coef = next_coef 
        
        return np.array(coef)
    
    def valueAt(self,t,option_type ='E'):
        coef = self.statePrice(t)
        
        if option_type =='A':
            V_T = self.American()[:,-1]
        
        else:
            V_T = self.European()[:,-1]
        
        result = np.dot(coef,V_T)
        
        return result
        
    
    
                
        
        