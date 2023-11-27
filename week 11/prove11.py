    
max = 0
min = 99999
max_country = ''
min_country = ''
max_year = 0
min_year = 99999
interest = int(input("Enter the year of interest: "))
max_drop = 0

with open ("life-expectancy.csv") as f:
    header = next(f)
    total = 0.0 
    count = 0
    maxLife_interest = 0
    minLife_interest = 9999
    maxInterest_country = ''
    minInterest_country = ''
    prev_life_exp = None 
    for i in f:
        clean_line = i.strip()
        data = clean_line.split(",")
        entity = data[0]
        code = data[1]
        year = int(data[2])
        life_exp = float(data[3])

        if life_exp > max:
            max = life_exp
            max_country = entity
            max_year = year
        if life_exp < min:
            min = life_exp
            min_country = entity
            min_year = year

        if year == interest:
            total += life_exp
            count += 1
            if life_exp > maxLife_interest:
                maxLife_interest = life_exp
                maxInterest_country = entity
            if life_exp < minLife_interest:
                minLife_interest = life_exp
                minInterest_country = entity

        if prev_life_exp is not None:
            drop = prev_life_exp - life_exp
            if drop > max_drop:
                max_drop = drop
                max_drop_country = entity
                max_drop_year = year

        prev_life_exp = life_exp

    print(f"\nThe overall max life ecpectancy is: {max} from {max_country} in {max_year}")
    print(f"The overall min life expectancy; is: {min} from {min_country} in {min_year}")
    print(f"The largest drop in life expectancy is {max_drop:.2f} and occured in {max_drop_country} in between ({max_drop_year -1}-{max_drop_year})")
    
    print(f"\nFor the year {interest}:")
    print(f"The average life expectancy across all countries was {(total/count):.2f}")
    print(f"The max life expectancy was in {maxInterest_country} with {maxLife_interest}")
    print(f"The min life expectancy was in {minInterest_country} with {minLife_interest}")
