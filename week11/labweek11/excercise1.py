def sss(a,b,c,d):
    return a - b - c - d
def ssp(a,b,c,d):
    return a - b - c + d
def ssm(a,b,c,d):
    return a - b - c * d

def sps(a,b,c,d):
    return a - b + c - d
def spp(a,b,c,d):
    return a - b + c + d
def spm(a,b,c,d):
    return a - b + c * d

def sms(a,b,c,d):
    return a - b * c - d
def smp(a,b,c,d):
    return a - b * c + d
def smm(a,b,c,d):
    return a-b*c*d


def pss(a,b,c,d):
    return a + b - c - d
def psp(a,b,c,d):
    return a + b - c + d
def psm(a,b,c,d):
    return a + b - c * d

def pps(a,b,c,d):
    return a + b + c - d
def ppp(a,b,c,d):
    return a + b + c + d
def ppm(a,b,c,d):
    return a + b + c * d

def pms(a,b,c,d):
    return a + b * c - d
def pmp(a,b,c,d):
    return a + b * c + d
def pmm(a,b,c,d):
    return a+b*c*d


def mss(a,b,c,d):
    return a * b - c - d
def msp(a,b,c,d):
    return a * b - c + d
def msm(a,b,c,d):
    return a * b - c * d

def mps(a,b,c,d):
    return a * b + c - d
def mpp(a,b,c,d):
    return a * b + c + d
def mpm(a,b,c,d):
    return a * b + c * d

def mms(a,b,c,d):
    return a * b * c - d
def mmp(a,b,c,d):
    return a * b * c + d
def mmm(a,b,c,d):
    return a*b*c*d

def main():
    
    
    a = int(input("input int :"))
    b = int(input("input int :"))
    c = int(input("input int :"))
    d = int(input("input int :"))
    
    
    resdict = {}
    resdict["sss"] = sss(a,b,c,d)
    resdict["ssp"] = ssp(a,b,c,d)
    resdict["ssm"] = ssm(a,b,c,d)
    
    resdict["sps"] = sps(a,b,c,d)
    resdict["spp"] = spp(a,b,c,d)
    resdict["spm"] = spm(a,b,c,d)
  
    resdict["sms"] = sms(a,b,c,d)
    resdict["smp"] = smp(a,b,c,d)
    resdict["smm"] = smm(a,b,c,d)
    
    resdict["pss"] = pss(a,b,c,d)
    resdict["psp"] = psp(a,b,c,d)
    resdict["psm"] = psm(a,b,c,d)
    
    resdict["pps"] = pps(a,b,c,d)
    resdict["ppp"] = ppp(a,b,c,d)
    resdict["ppm"] = ppm(a,b,c,d)

    resdict["pms"] = pms(a,b,c,d)
    resdict["pmp"] = pmp(a,b,c,d)
    resdict["pmm"] = pmm(a,b,c,d)
    
    resdict["mss"] = mss(a,b,c,d)
    resdict["msp"] = msp(a,b,c,d)
    resdict["msm"] = msm(a,b,c,d)
    
    resdict["mps"] = mps(a,b,c,d)
    resdict["mpp"] = mpp(a,b,c,d)
    resdict["mpm"] = mpm(a,b,c,d)
    
    resdict["mms"] = mms(a,b,c,d)
    resdict["mmp"] = mmp(a,b,c,d)
    resdict["mmm"] = mmm(a,b,c,d)
    
    for x,y in resdict.items():
        print(x,":",y)
    
main()