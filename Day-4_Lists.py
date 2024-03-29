

states_of_india = ["Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh",
          "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand", "Karnataka",
          "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram",
          "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana",
          "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal", "Andaman and Nicobar Islands",
          "Chandigarh", "Dadra and Nagar Haveli and Daman and Diu", "Delhi", "Lakshadweep",
          "Puducherry"]

states_of_india[0] = "Telangana" # replace with other strings from start to end
states_of_india[-2] = "Telangana" # replace with other strings from end to start

states_of_india.append("Telangana")
states_of_india.extend(["Telangana", "Delhi"])
states_of_india.insert(2,"Telangana")
count_new_state = states_of_india.count("Telangana")
print(states_of_india)
print(count_new_state)
print(len(states_of_india))

index = states_of_india[38] - 1
print(index)