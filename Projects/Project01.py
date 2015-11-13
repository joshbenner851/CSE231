pop = 318651218
num_seconds_in_year = 365*24*60*60
years = input("Enter how many years")
Years = int(years)
deaths = num_seconds_in_year/13 * Years
births = num_seconds_in_year/7 * Years
immigrants = num_seconds_in_year/40 * Years
final_pop = int(pop - deaths + births + immigrants)
print("population after ", Years , " is ", final_pop)


