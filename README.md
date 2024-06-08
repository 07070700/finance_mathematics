# **FINANCE MATHEMATHICS**

## Discrete Model

In Finance we can devide into the two categories.  
* Underlying Asset : financial asset which  a derivatives is based.
*  Derivatives : a finance contract whose value depends on an underlying asset. For example, Forward, Futures, Option, Swap ...

People use Derivatives to hedge a risk of our portpolio, increase leverage or speculate(투기) an asset's movement. 

In the documents, we calculate **the value and payoff of Call option and Put option among Derivative**.

The code cover 
* Multi-period
* one- risky asset
* binominal model (we assume omega(state space) has up and down only).



<!-- crl + alt = multi cusor -->
>**$S_i$**: stock price at time i  
**$r$** : Interest rate of a year 
**$T$** : Maturity   
**$n$** :  The number of interest payments per T  
**$u$** :  up  
**$d$** :  down  
**$h$** :  $\frac{T}{n}$  
**$K$** :  Forward price

Using the information above, we can caculate **Risky Neutral Probobability**. 

The Risky neutral probability is derived from the assumption that the value of option at maturity and the payoff of matured option are equal.

Therefore, Risky neutral probability represents the probablity of potential future outcomes adjusted for risk.


$$\tilde{p} = \frac{(1+r)-d}{u-d}$$
$$\tilde{q} = \frac{u-(1+r)}{u-d}$$

First, we calculate call and put option of contingent claim. Contingent claim is a no arbitrage derivative. 


We want to know the value of contingent claim at time(t).

**Call option**  
: long position

 $$V(T) = S(T)(\omega) - K$$


**Put option**  
:short position

 $$V(T) = K- S(T)(\omega)$$



$$V(t) = \tilde{p} V(t+1)(\omega_1) + \tilde{q}V(t+1)(\omega_2)$$


m is the number of states at Maturity T

$$V(0) = (\tilde{p} + \tilde{q})^T * 

\begin{equation}
   \begin{pmatrix} 
   V_{T}(\omega_1)  \\
   \vdots \\
   V_{T}(\omega_{m-1})  \\
   V_{T}(\omega_{m})  \\
   \end{pmatrix} 
\end{equation}$$
