seasons = {
    1: 'Winter', 2: 'Winter', 3: 'Spring',
    4: 'Summer', 5: 'Summer', 6: 'Summer',
    7: 'Monsoon', 8: 'Monsoon', 9: 'Autumn',
    10: 'Autumn', 11: 'Autumn', 12: 'Winter'
}
month = int(input("Enter the month number (1-12): "))
season = seasons.get(month, 'Invalid month number')
if month < 1 or month > 12: print("Invalid month number")
else: print("The season is:", season)
