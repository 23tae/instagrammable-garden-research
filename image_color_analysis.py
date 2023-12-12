import sys
import os

if len(sys.argv) < 5:
    print("<Usage>\npython3 image_color_analysis.py <tag> <username> <file1_name> <file2_name>")
    sys.exit(1)

tag = sys.argv[1]
username = sys.argv[2]

user_path = os.path.join('./result', tag, 'properties', username)


def get_color_data(file_path):
    color_data = []
    with open(file_path, "r") as f:
        lines = f.readlines()
        fraction = 0.0
        r = 0.0
        g = 0.0
        b = 0.0
        for line in lines:
            if line.startswith("Properties:"):
                continue
            elif line.startswith('\ta:'):
                color_data.append(
                    {"fraction": fraction, "r": r, "g": g, "b": b})
                continue
            elif line.startswith("fraction"):
                fraction = float(line.split()[1])
            else:
                if line.startswith('\tr:'):
                    r = float(line.split(':')[1].strip())
                elif line.startswith('\tg:'):
                    g = float(line.split(':')[1].strip())
                elif line.startswith('\tb:'):
                    b = float(line.split(':')[1].strip())
    return color_data


def calculate_average_rgb(data):
    total_r, total_g, total_b = 0, 0, 0
    total_pixels = 0

    for entry in data:
        total_r += entry['r'] * entry['fraction']
        total_g += entry['g'] * entry['fraction']
        total_b += entry['b'] * entry['fraction']
        total_pixels += entry['fraction']

    average_r = total_r / total_pixels
    average_g = total_g / total_pixels
    average_b = total_b / total_pixels

    return average_r, average_g, average_b


file1_name = sys.argv[3]
file2_name = sys.argv[4]

file1_fullname = file1_name + ".txt"
file2_fullname = file2_name + ".txt"

file1_image_name = file1_name + ".jpg"
file2_image_name = file2_name + ".jpg"

file1_path = os.path.join(user_path, file1_fullname)
file2_path = os.path.join(user_path, file2_fullname)

# Get color data for both files
file1_colors = get_color_data(file1_path)
file2_colors = get_color_data(file2_path)


# Calculate average RGB values for each file
average_rgb_1 = calculate_average_rgb(file1_colors)
average_rgb_2 = calculate_average_rgb(file2_colors)

# Compare average RGB values
print("Average RGB values for", file1_image_name, average_rgb_1)
print("Average RGB values for", file2_image_name, average_rgb_2)

# Compare colorfulness based on average RGB values
if sum(average_rgb_1) > sum(average_rgb_2):
    print(file1_image_name, "is potentially more colorful than", file2_image_name)
else:
    print(file2_image_name,
          "may have a more dominant color palette compared to", file1_image_name)
