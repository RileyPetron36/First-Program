def convert_hours_to_minutes_seconds(hours):

  minutes = hours * 60
  seconds = hours * 3600
  return minutes, seconds

hours_input = float(input("Enter the number of hours to convert: "))

minutes_output, seconds_output = convert_hours_to_minutes_seconds(hours_input)

print(f"{hours_input} hours is equal to {minutes_output} minutes.")
print(f"{hours_input} hours is equal to {seconds_output} seconds.")