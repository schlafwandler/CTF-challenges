#!/usr/bin/env python

Yei1oHai2shaa7oonieD       =   "R" 
Feo9thouN6zaegei0un5       =   "w"
eigh2goong0oogh0uW2b       =   "_"
coo9Do1zeeyae5aequee       =   "M"
IboshaiHusiewaezool7       =   "C"
iJ8yekaiquootoobooph       =   "{"
yahth9tuFei3eexaisha       =   "T"
Thee4co8ateinie3mah4       =   "5"
their0eecah3pah4hiSh       =   "}"
ohshaChaingoowoo7Ou6       =   "z"
fees4Quoo2geij2achau       =   "G"

def bie1aibeathae6pieTh6(ceiqueiD8EePeechuj8g,eeH9ohYaitiYohKai7pa):
    eid0zahca1quauthaKoi = []
    uoYah1ahh2Eijah6eitu = 0

    ####################
    tested_char = -1;
    ####################

    while True:
        Ki8Hie7otaed7zae9eV4 = ceiqueiD8EePeechuj8g[uoYah1ahh2Eijah6eitu]

        if Ki8Hie7otaed7zae9eV4 == Yei1oHai2shaa7oonieD:
            eid0zahca1quauthaKoi += [ord(ceiqueiD8EePeechuj8g[uoYah1ahh2Eijah6eitu+1])]
            uoYah1ahh2Eijah6eitu += 2
        elif Ki8Hie7otaed7zae9eV4 == Feo9thouN6zaegei0un5:
            eid0zahca1quauthaKoi.pop()
            uoYah1ahh2Eijah6eitu += 1
        elif Ki8Hie7otaed7zae9eV4 == eigh2goong0oogh0uW2b:
            xei2eeWair6iePae4uoh = eid0zahca1quauthaKoi[-1]
            ohziekie8Iewohgae7ah = eid0zahca1quauthaKoi[-2]
            del eid0zahca1quauthaKoi[-1]
            del eid0zahca1quauthaKoi[-1]
            eid0zahca1quauthaKoi += [(xei2eeWair6iePae4uoh + ohziekie8Iewohgae7ah)&0xff]
            uoYah1ahh2Eijah6eitu += 1
        elif Ki8Hie7otaed7zae9eV4 == coo9Do1zeeyae5aequee:
            xei2eeWair6iePae4uoh = eid0zahca1quauthaKoi.pop()
            ohziekie8Iewohgae7ah = eid0zahca1quauthaKoi[-1]
            eid0zahca1quauthaKoi = eid0zahca1quauthaKoi[:-1]
            eid0zahca1quauthaKoi += [(xei2eeWair6iePae4uoh - ohziekie8Iewohgae7ah)&0xff]
            uoYah1ahh2Eijah6eitu += 1
        elif Ki8Hie7otaed7zae9eV4 == IboshaiHusiewaezool7:
            xei2eeWair6iePae4uoh = eid0zahca1quauthaKoi[-1]
            del eid0zahca1quauthaKoi[-1]
            ohziekie8Iewohgae7ah = eid0zahca1quauthaKoi[-1]
            del eid0zahca1quauthaKoi[-1]
            eid0zahca1quauthaKoi += [xei2eeWair6iePae4uoh ^ ohziekie8Iewohgae7ah]
            uoYah1ahh2Eijah6eitu += 1
        elif Ki8Hie7otaed7zae9eV4 == iJ8yekaiquootoobooph:
            ####################
            print("Testing password[%d]"%(eid0zahca1quauthaKoi[-1]))
            tested_char = eid0zahca1quauthaKoi[-1]
            ####################
            eid0zahca1quauthaKoi += [ord(eeH9ohYaitiYohKai7pa[eid0zahca1quauthaKoi[-1]])]
            del eid0zahca1quauthaKoi[-2]
            uoYah1ahh2Eijah6eitu += 1
        elif Ki8Hie7otaed7zae9eV4 == yahth9tuFei3eexaisha:
            xei2eeWair6iePae4uoh = eid0zahca1quauthaKoi.pop()
            ohziekie8Iewohgae7ah = eid0zahca1quauthaKoi.pop()
            eid0zahca1quauthaKoi += range(0,1)
            eid0zahca1quauthaKoi[-1] = xei2eeWair6iePae4uoh | ohziekie8Iewohgae7ah
            ####################
            if len(eid0zahca1quauthaKoi) == 1:
                print("or %d,%d"%(xei2eeWair6iePae4uoh,ohziekie8Iewohgae7ah))
                if eid0zahca1quauthaKoi[-1]:
                    # status byte is non-zero, so the last check has failed
                    print("Test of byte %d failed, retrying"%(tested_char))
                    return tested_char
            ####################
            uoYah1ahh2Eijah6eitu += 1
        elif Ki8Hie7otaed7zae9eV4 == Thee4co8ateinie3mah4:
            eid0zahca1quauthaKoi += [eid0zahca1quauthaKoi[-1]]
            uoYah1ahh2Eijah6eitu += 1
        elif Ki8Hie7otaed7zae9eV4 == their0eecah3pah4hiSh:
            xei2eeWair6iePae4uoh = eid0zahca1quauthaKoi[-1]
            del eid0zahca1quauthaKoi[-1]
            if xei2eeWair6iePae4uoh:
                uoYah1ahh2Eijah6eitu += ord(ceiqueiD8EePeechuj8g[uoYah1ahh2Eijah6eitu+1])
            else:
                uoYah1ahh2Eijah6eitu += 2
        elif Ki8Hie7otaed7zae9eV4 == ohshaChaingoowoo7Ou6:
            ####################
            print("reached end without failing")
            print("my job here is done")
            return -1
            ####################
            return eid0zahca1quauthaKoi.pop()
            uoYah1ahh2Eijah6eitu += 1
        elif Ki8Hie7otaed7zae9eV4 == fees4Quoo2geij2achau:
            eid0zahca1quauthaKoi[-1] = ~eid0zahca1quauthaKoi[-1]
            uoYah1ahh2Eijah6eitu += 1
        else:
            uoYah1ahh2Eijah6eitu += 1
        uoYah1ahh2Eijah6eitu = uoYah1ahh2Eijah6eitu % len(ceiqueiD8EePeechuj8g)

def main():
    print("The password is the flag!")
    print("Password:")
    password = raw_input()
    password += " "*128

    correct = bie1aibeathae6pieTh6(code,password)

    if correct:
        print("######################################")
        print("###   Correct! This is the flag!   ###")
        print("######################################")
    else:        
        print("Wrong. Try again.")

code = """R\x00RMR\x00{MTR\x9eR\x1e{_R\x11CAApV2TR\x01{RRMTR\x02{R*CRgCTR\r{Z3IDRhMTR\x03{RCMTR\x14{R\x98_TR\x05{R\x17CRTCotac4TR\x07{R\x1fCfRYCTENR\x18{R\x90_TR\x08{R{MTR?R!9hVc{_3NnR\xbcCTR\n{RnMTR\x0b{6dlRoMTR\x0e{ReMTR\xa2R\x1c{_R\x07CTR\x0f{R\x8e_TR\x10{R\xa1_OeTR\x11{R\x90_TR\x12{R\x87_TR\x13{R\x8c_TR"R\x1b{_R\x85CTR\x15{WR\x91_TR\x0c{RtMSP2PITR\x16gZ{R\x92dXtSp_TR\x17{R\xa1O_TRTR\x06{MTR\x04{RDMTR\x9eR\x19{_DvSR\x10WE0VCTRLR\x1a{_R\xbbCTR\xa4YAlR\x1dJF7{_R\x17CTR\t{RaMTR\x92R\x1f{_R\x01CTR\x16R {_R\x88CTa}\x05R\x01zR\x00Qz"""

####################
import string
def brute_force():
    password = " "*128

    failing_char = 0
    last_failing_char = -1
    while failing_char != -1:
        print("Testing password %s"%(password))
        failing_char = bie1aibeathae6pieTh6(code,password)
        if failing_char != last_failing_char:
            search_space = iter(string.printable)
            last_failing_char = failing_char
        # ugly but working
        password = list(password)
        password[failing_char] = search_space.next()
        password = "".join(password)
    print(password)



####################

if __name__=="__main__":
    #main()
    brute_force()

