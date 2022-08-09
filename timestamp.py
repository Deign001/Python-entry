#Boto3 is the AWS - Software Development Kit (SDK) - for Python
import boto3

#Module used for finding our timezone attributes
import pytz

#Module used for finding our timestamp attributes
from datetime import date, datetime, time

#variable and function code
today = date.today()

#attributes
print("Month: ", today.month)
print("Day: ", today.day)
print("Year: ", today.year)

print("The current times are: ")

dt_us_central = datetime.now(pytz.timezone('America/Mexico_City'))
print("US Central DateTime:", dt_us_central.strftime("%Y:%m:%d %H:%M:%S %Z %z"))

dt_us_pacific = datetime.now(pytz.timezone('America/Tijuana'))
print("US Pacific timezone DateTime:", dt_us_pacific.strftime("%Y:%m:%d %H:%M:%S %Z %z"))

dt_us_eastern = datetime.now(pytz.timezone('America/New_York'))
print("US Eastern timezone DateTime:", dt_us_eastern.strftime("%Y:%m:%d %H:%M:%S %Z %z"))

dt_us_mountain = datetime.now(pytz.timezone('America/Chihuahua'))
print("US Mountain timezone DateTime:", dt_us_mountain.strftime("%Y:%m:%d %H:%M:%S %Z %z"))
