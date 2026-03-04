V1=int(input("Your Weight in KG:"))
V2=float(input("Your Height in Meters:"))

if V1/(V2*V2) < 18.5:
    print("You are currently underweight. Your body is asking for strength, not criticism. This is not weakness this is potential energy waiting to be built. Focus on Nutritious food Strength training Proper sleep Your journey is not about gaining weight. It is about building power.Small improvements every day. Stay consistent.,Your BMI is:",V1/(V2*V2))

elif V1/(V2*V2) > 18.5 and V1/(V2*V2) < 24.9 :
   print("You are in the healthy range. This is balance. This is discipline. This is consistency showing results.Your BMI: " ,V1/(V2*V2))

elif V1/(V2*V2) > 25.00 and V1/(V2*V2) <29.9 :
    print("You are slightly above the healthy range. BMI:",V1/(V2*V2))
else :
    print("Obease,BMI: ",V1/(V2*V2))
