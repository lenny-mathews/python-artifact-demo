from datetime import datetime

print ("Python artifacts demo")

with open ("result.txt","w") as file:
  file.write ("Hello from GitHubs\n")
  file.write ("Thiis file is created in Git\n")
  file.write (f"This file is generated on {datetime.now()}\n")

print (" Result.txt file created sucessfully")

  
  
