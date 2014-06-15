# Lukas Schwab, 6/15/14
# github.com/lukasschwab
# lukas.schwab@gmail.com

#-----------------------#

# Note that in CSS3 there's a better implementation:
# 	http://www.sitepoint.com/javascript-generate-lighter-darker-color/

#-----------------------#

# Input the color that marks 100%, in hex form
clr100=str(input('Enter the hex value for the 100 percet color.     '))
# Split into a list of the component 2-digit numbers
clrlist=[clr100[i:i+2] for i in range(0, len(clr100), 2)]

# Input the percentage you're looking for
pct=input('Enter the percentage, without a percent sign.     ')
pct=float(100-pct)
pct=pct/100

# Final color to 0
clrf=""

# Iterate to scale every item in the list
for s in clrlist:
	dec=int(s,16)

	# Find difference between this value and pure white
	dif=255-dec

	# Add a normalized value to get you pct closer to full white
	modded=dec+int(pct*dif)

	# Convert back to hex.
	modded=hex(modded)[2:]
	# Make sure it's two digits
	if len(modded) < 2:
		modded2="0"
		modded2+=str(modded)
		modded=modded2

	# Concatonate to the string.
	clrf+=str(modded)

print '#' + clrf