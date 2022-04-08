import decimal #so u can use decimals

print("Welcome to Dawnys DHC Calculator.")
DHC1 = decimal.Decimal(input('Enter DHC Ammount: '))

print("")#this is js to make it look good

DHCAfterTax1 = DHC1 * decimal.Decimal('1.42857')#times the inputted number by 1.42857
print("Tax Section:")
print('DHC With Tax:', int(DHCAfterTax1) + 2)#adds 2 to make it more accurate

print("")#this is js to make it look good

DHCExtra1 = float(DHC1)
DHCTax1 = (30/100) * DHCExtra1 #calculating for drop (30%)
DHC333 = DHCExtra1 - DHCTax1
print("Drop Section:")
print("DHC After Drop:", int(DHC333))
DHCTax2 = DHC1/40000 #this is for the time to takes to drop
print("Estimated time to drop:", int(DHCTax2),"minutes")

print("")#this is js to make it look good

print("Information") #super epic info
print("You can drop...")
print("28,000 per minute")
print("7,000 per 15 seconds")

print("")#this is js to make it look good

print("Credits:")
print("Made by tiny toes#8633 on Discord")
print("Inspired by remorse#9230 on Discord")