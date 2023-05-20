total_days = 999

years = total_days // 365

remaining_days = total_days - (years * 365)

months = remaining_days // 30

days = remaining_days - (months * 30)

print(f"{years} years, {months} months, {days} days")