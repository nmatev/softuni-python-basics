pages = int(input())
pages_for_one_hour = int(input())
total_days = int(input())

# // знак за челочислено деление
total_time_needed = pages // pages_for_one_hour
pages_a_day = total_time_needed // total_days

print(total_time_needed)
print(pages_a_day)