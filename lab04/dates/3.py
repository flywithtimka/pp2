from datetime import datetime
current_datetime = datetime.now()
clean_datetime = current_datetime.replace(microsecond=0)
print("Original Datetime:", current_datetime)
print("Datetime Without Microseconds:", clean_datetime)
