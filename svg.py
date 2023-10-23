from bs4 import BeautifulSoup

# Read the SVG content from a text file
with open("input.svg", "r") as file:
    svg_text = file.read()

# Create a BeautifulSoup object
soup = BeautifulSoup(svg_text, 'html.parser')

path_elements = soup.find_all('path')
for i, path in enumerate(path_elements, start=1):
    path['class'] = f'path-{i}'

clip_paths = soup.find_all('clipPath')

for clip_path in clip_paths:

    child_path = clip_path.find('path')

    if child_path:
        # Add the child path element to the main SVG tag
        svg_tag = soup.find('svg')
        svg_tag.append(child_path)

    # Remove the clipPath element
    clip_path.decompose()
# Convert the modified soup back to an SVG string
modified_svg = str(soup)

# Save the modified SVG content to another text file
with open("output.svg", "w") as file:
    file.write(modified_svg)