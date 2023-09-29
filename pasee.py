price_poojai = 399
price_kids = 200
print("------------------------------------------\n")
poojai = int(input("Enter the number of adults : "))
kiddo = int(input("\nEnter the number of kids    : "))
rapma = int(input("\nEnter that you recive          : "))


Total_price = ((poojai * price_poojai)+(kiddo * price_kids))
callsomthing = rapma - Total_price
PASEE = Total_price * 7/100
Net_price = Total_price + PASEE
print("------------------------------------------\n")

print("Total price             = {} Baht\n".format(Total_price))
print("VAT 7%                = {} Baht\n".format(PASEE))
print("Net Price               = {} Baht\n".format(Net_price))
print("change                 =  {} Baht\n".format(callsomthing))
print("------------------------------------------\n")
print("Powered By Nattawatt Hongthong Group 3 Silde 48\n")
print("------------------------------------------\n")