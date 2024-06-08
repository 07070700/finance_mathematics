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

    def statePrice(self,t):
        n_t = self.T-t
        
        tilde_p = (1+self.r*self.h - self.d)/ (self.u - self.d)
        tilde_q = 1-tilde_p
        
        discount = 1 / (1 + self.r) ** n_t
        
        coefs = []
        for i in range(n_t + 1):
            coef = (tilde_p ** (n_t - i)) * (tilde_q** i)  # 각 항의 계수 계산
            coefs.append(coef)  # 리스트에 계수 추가
        
        coeff = np.array(coefs) * discount
        
        return coeff
    
    
    def valueAt(self,t,option_type ='E'):
        coef = self.statePrice(t)
        
        if option_type =='A':
            VT = self.American()[:,-1]
        
        else:
            VT = self.European()[:,-1]
        
        result = np.dot(coef,VT)
        
        return result
        
                
            