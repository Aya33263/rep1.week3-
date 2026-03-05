from datetime import datetime
import pytz

# 1. Define the timezone
tz_INDIA = pytz.timezone('Asia/Kolkata')

# 2. Pass the timezone into the now() method
# This fixes the error where now() defaults to your local computer time
now_method = datetime.now(tz_INDIA)

# 3. Format the string
currentTime = now_method.strftime("%H:%M:%S")

print("Current India Time =", currentTime)
