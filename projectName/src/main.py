import os
from datetime import datetime

# Define the path for version.md in the output folder
output_dir = "projectName/output"
output_file = os.path.join(output_dir, "version.md")

# Ensure the output folder exists
os.makedirs(output_dir, exist_ok=True)

# Get the current date and time
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Write the current date and time to version.md
with open(output_file, "w") as f:
    f.write(f"# Version Information\n\n")
    f.write(f"Date and Time: {current_time}\n")

print(f"Date and time written to {output_file}")
