temp_F = [24.3, 69.2, 26.8, 71.2, 29.3, 72.8, 27.0, 71.7, 30.3, 73.4]
min_val= min(temp_F)
max_val= max(temp_F) 
temp_scaled = [(x - min_val) / (max_val - min_val) for x in temp_F]
formatted_scaled =[round(x,2) for x in temp_scaled]   
print(formatted_scaled)

# Output: [0.0, 0.91, 0.05, 0.96, 0.1, 0.99, 0.05, 0.97, 0.12, 1.0]