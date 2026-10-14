import sys

with open('docs/petstore.yaml', 'r') as f:
    lines = f.readlines()

new_lines = []
skip = False
for i, line in enumerate(lines):
    if '<<<<<<< HEAD' in line:
        new_lines.append('    <SecurityDefinitions passwordFlow implicitFlow clientCredentialsFlow authorizationCodeFlow></SecurityDefinitions>\n')
        skip = True
        continue
    if '=======' in line and skip:
        continue
    if '>>>>>>> origin/main' in line and skip:
        skip = False
        continue
    if skip:
        continue
    new_lines.append(line)

content = "".join(new_lines)

target_desc = 'description: The number of items to skip before starting to collect the result set (zero-based)'
replacement_desc = 'description: The number of items to skip before starting to collect the result set (zero-based, defaults to 0)'

status_pos = content.find('operationId: findPetsByStatus')
if status_pos != -1:
    offset_pos = content.find('name: offset', status_pos)
    if offset_pos != -1:
        desc_pos = content.find(target_desc, offset_pos)
        if desc_pos != -1 and desc_pos - offset_pos < 100:
            content = content[:desc_pos] + replacement_desc + content[desc_pos + len(target_desc):]

with open('docs/petstore.yaml', 'w') as f:
    f.write(content)
