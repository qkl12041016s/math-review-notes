"""Symbolic/numerical checks for added formulas, examples and boundaries."""
from pathlib import Path
from itertools import product
import json
import sympy as s

OUT=Path(__file__).resolve().parents[1]
checks=[]

def equal(name,left,right):
    difference=s.simplify(left-right)
    if difference!=0:
        difference=s.trigsimp(difference)
    if difference!=0:
        difference=s.simplify(s.trigsimp((left-right).rewrite(s.sin)))
    assert difference==0,(name,difference)
    checks.append({'name':name,'result':'passed'})

def truth(name,value):
    assert bool(value),name
    checks.append({'name':name,'result':'passed'})

def main():
    x,t=s.symbols('x t',real=True)
    u=s.Function('u')(x);v=s.Function('v')(x);w=s.Function('w')(x)
    equal('two-factor first derivative',s.diff(u*v,x),s.diff(u,x)*v+u*s.diff(v,x))
    equal('three-factor first derivative',s.diff(u*v*w,x),s.diff(u,x)*v*w+u*s.diff(v,x)*w+u*v*s.diff(w,x))
    F=s.Function('F')
    for n in [1,2,3]:
        if n==1: expected=s.diff(F(u),u)*s.diff(u,x)
        if n==2: expected=s.diff(F(u),u,2)*s.diff(u,x)**2+s.diff(F(u),u)*s.diff(u,x,2)
        if n==3: expected=s.diff(F(u),u,3)*s.diff(u,x)**3+3*s.diff(F(u),u,2)*s.diff(u,x)*s.diff(u,x,2)+s.diff(F(u),u)*s.diff(u,x,3)
        equal(f'chain rule order {n}',s.diff(F(u),x,n),expected)
    positive=s.symbols('positive',positive=True)
    composite=positive**2+1
    basic=[
        (s.exp(composite),2*positive*s.exp(composite)),
        (s.log(composite),2*positive/composite),
        (s.sqrt(composite),positive/s.sqrt(composite)),
        (s.sin(composite),2*positive*s.cos(composite)),
        (s.cos(composite),-2*positive*s.sin(composite)),
        (s.tan(composite),2*positive/s.cos(composite)**2),
        (s.cot(composite),-2*positive/s.sin(composite)**2),
        (s.sec(composite),2*positive*s.sec(composite)*s.tan(composite)),
        (s.csc(composite),-2*positive*s.csc(composite)*s.cot(composite)),
        (s.atan(composite),2*positive/(1+composite**2)),
        (s.acot(composite),-2*positive/(1+composite**2)),
        (composite**s.sin(positive),composite**s.sin(positive)*(s.cos(positive)*s.log(composite)+2*positive*s.sin(positive)/composite)),
    ]
    for i,(expression,answer) in enumerate(basic):equal(f'composite table example {i+1}',s.diff(expression,positive),answer)
    h=s.sin(x)/2
    equal('arcsin composite',s.diff(s.asin(h),x),s.diff(h,x)/s.sqrt(1-h*h))
    equal('arccos composite',s.diff(s.acos(h),x),-s.diff(h,x)/s.sqrt(1-h*h))
    equal('chain example log sine squared',s.diff(s.log(1+s.sin(3*x)**2),x),6*s.sin(3*x)*s.cos(3*x)/(1+s.sin(3*x)**2))
    equal('chain second derivative example',s.diff(s.sin(x*x),x,2),2*s.cos(x*x)-4*x*x*s.sin(x*x))
    for n in range(1,7):
        leibniz=sum(s.binomial(n,k)*s.diff(u,x,k)*s.diff(v,x,n-k) for k in range(n+1))
        equal(f'Leibniz n={n}',s.diff(u*v,x,n),leibniz)
    equal('three factors second derivative',s.diff(u*v*w,x,2),
          s.diff(u,x,2)*v*w+u*s.diff(v,x,2)*w+u*v*s.diff(w,x,2)
          +2*s.diff(u,x)*s.diff(v,x)*w+2*s.diff(u,x)*v*s.diff(w,x)+2*u*s.diff(v,x)*s.diff(w,x))
    for n in range(3,7):
        equal(f'x^3 times f order {n}',s.diff(x**3*u,x,n),
              x**3*s.diff(u,x,n)+3*n*x*x*s.diff(u,x,n-1)+3*n*(n-1)*x*s.diff(u,x,n-2)+n*(n-1)*(n-2)*s.diff(u,x,n-3))
    expressions=[
        ((x*x+1)*s.sin(x),2*x*s.sin(x)+(x*x+1)*s.cos(x),1),
        ((x*x+1)*s.sin(x),2*s.sin(x)+4*x*s.cos(x)-(x*x+1)*s.sin(x),2),
        (x*s.exp(x)*s.sin(x),s.exp(x)*((x+1)*s.sin(x)+x*s.cos(x)),1),
        (s.exp(x*x)*s.sin(3*x),2*x*s.exp(x*x)*s.sin(3*x)+3*s.exp(x*x)*s.cos(3*x),1),
        ((1+x)*s.exp(2*x),4*(x+2)*s.exp(2*x),2),
        (x*s.sin(x)*s.cos(x),s.sin(x)*s.cos(x)+x*(s.cos(x)**2-s.sin(x)**2),1),
    ]
    for i,(expr,answer,n) in enumerate(expressions): equal(f'product example {i+1}',s.diff(expr,x,n),answer)
    for f in [t**2,s.exp(t),1+t]:
        G=s.integrate((x-t)*f,(t,0,x))
        equal('moving integral '+str(f),s.diff(G,x),s.integrate(f,(t,0,x)))
        H=s.integrate(f.subs(t,x*t),(t,0,x),conds='none')
        answer=2*f.subs(t,x*x)-s.integrate(f,(t,0,x*x))/x**2
        equal('xt kernel '+str(f),s.diff(H,x),answer)
    equal('moving upper and lower limits',s.diff(s.integrate(x+t*t,(t,x,x*x)),x),2*x**5+2*x*x-2*x)
    q,p=s.symbols('q p',positive=True)
    C=100+10*q+q*q
    equal('minimum average cost derivative',s.diff(C/q,q).subs(q,10),0)
    equal('average equals marginal at minimum',(C/q).subs(q,10),s.diff(C,q).subs(q,10))
    equal('profit maximum',(50*q-C).subs(q,20),300)
    D=120-2*p
    equal('unit demand elasticity at revenue maximum',(-p*s.diff(D,p)/D).subs(p,30),1)
    n=s.symbols('n',integer=True,nonnegative=True)
    for a,b,z in [(s.Rational(4,5),10,0),(-s.Rational(1,2),3,0),(2,1,4)]:
        a,b,z=map(s.sympify,(a,b,z))
        fixed=b/(1-a);seq=fixed+a**n*(z-fixed)
        equal(f'difference recurrence a={a}',seq.subs(n,n+1),a*seq+b)
        equal(f'difference initial a={a}',seq.subs(n,0),z)
    seq=2**n*(1+3*n/2)
    equal('resonant difference recurrence',seq.subs(n,n+1),2*seq+3*2**n)
    equal('cobweb first period',45-s.Rational(1,2)*20,35)
    equal('cone lateral area',2*s.pi*s.integrate(x*s.sqrt(2),(x,0,1)),s.pi*s.sqrt(2))
    A,H,h,rho,g=s.symbols('A H h rho g',positive=True)
    equal('pumping work',rho*g*A*s.integrate(H-x,(x,0,h)),rho*g*A*(H*h-h*h/2))
    equal('pressure center depth',s.integrate(x*x,(x,0,h))/s.integrate(x,(x,0,h)),2*h/3)
    a,L=s.symbols('a L',positive=True)
    equal('rod force integral',s.integrate(1/(a+x)**2,(x,0,L)),1/a-1/(a+L))
    r,R=s.symbols('r R',positive=True)
    equal('disk moment factor',2*s.pi*s.integrate(r**3,(r,0,R)),s.pi*R**4/2)
    equal('paraboloid solid volume',2*s.pi*s.integrate((2-r*r)*r,(r,0,s.sqrt(2))),2*s.pi)
    y=s.symbols('y',real=True)
    P=-y/(x*x+y*y);Q=x/(x*x+y*y)
    equal('zero curl away from origin',s.diff(Q,x)-s.diff(P,y),0)
    eps=s.symbols('eps',positive=True)
    circle={x:eps*s.cos(t),y:eps*s.sin(t)}
    form=P.subs(circle)*s.diff(circle[x],t)+Q.subs(circle)*s.diff(circle[y],t)
    equal('small circle integral',s.integrate(s.simplify(form),(t,0,2*s.pi)),2*s.pi)
    for k in range(1,7):
        equal(f'x squared Fourier coefficient {k}',2/s.pi*s.integrate(x*x*s.cos(k*x),(x,0,s.pi)),s.Rational(4*(-1)**k,k**2))
    equal('sum 1/n^2',s.zeta(2),s.pi**2/6)
    equal('alternating square reciprocal sum',s.dirichlet_eta(2),s.pi**2/12)
    B=s.Matrix([[1,2],[0,1]])
    truth('non-symmetric principal minors positive',B[0,0]>0 and B.det()>0)
    z=s.Matrix([1,-1]);equal('non-symmetric quadratic zero direction',(z.T*B*z)[0],0)
    truth('symmetric part semidefinite',set(((B+B.T)/2).eigenvals())=={0,2})
    for matrix in [s.diag(1,2,3),s.diag(0,2,3),s.Matrix([[2,1],[0,2]]),s.Matrix([[0,1],[0,0]]),s.diag(1,1,2,4)]:
        eigen=[]
        for val,multiplicity in matrix.eigenvals().items(): eigen.extend([val]*multiplicity)
        trace=sum(s.prod(eigen[:i]+eigen[i+1:]) for i in range(len(eigen)))
        equal('adjugate trace '+str(matrix.tolist()),s.trace(matrix.adjugate()),trace)
    sample=[s.Rational(21,10),s.Rational(24,10),s.Rational(28,10)]
    lower,upper=max(sample)-1,min(sample)
    equal('location-uniform lower feasible bound',lower,s.Rational(18,10))
    equal('location-uniform upper feasible bound',upper,s.Rational(21,10))
    truth('location-uniform MLE not unique',lower<upper)
    truth('sample maximum invalid location parameter',max(sample)>upper)
    equal('normal sign-mixture variance',s.Rational(1,2)*0+s.Rational(1,2)*4,2)
    truth('normal sign mixture has nonzero atom',s.Rational(1,2)>0)
    report={'checks':len(checks),'passed':len(checks),'scope':'本轮新增乘法及复合求导、积分、经济与差分、Fourier、线代与MLE关键算例；不声称重算了全部原书习题','items':checks}
    (OUT/'build/verification').mkdir(parents=True,exist_ok=True)
    (OUT/'build/verification/math_checks.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
    print(len(checks),'symbolic and boundary checks passed')

if __name__=='__main__': main()
