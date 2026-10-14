import sys
import re

with open('docs/petstore.yaml', 'r') as f:
    content = f.read()

# Resolve SecurityDefinitions conflict
conflict_re = re.compile(r'<<<<<<< HEAD\n(.*?)\n=======\n(.*?)\n>>>>>>> origin/main', re.DOTALL)
def resolve_security(match):
    return '    <SecurityDefinitions passwordFlow implicitFlow clientCredentialsFlow authorizationCodeFlow deviceCodeFlow jwtBearerFlow></SecurityDefinitions>'

content = conflict_re.sub(resolve_security, content)

# Update descriptions
target_desc = 'description: The number of items to skip before starting to collect the result set (zero-based)'
replacement_desc = 'description: The number of items to skip before starting to collect the result set (zero-based, defaults to 0)'

for op in ['findPetsByStatus', 'findPetsByTags']:
    op_pos = content.find(f'operationId: {op}')
    if op_pos != -1:
        offset_pos = content.find('name: offset', op_pos)
        if offset_pos != -1:
            desc_pos = content.find(target_desc, offset_pos)
            if desc_pos != -1 and desc_pos - offset_pos < 100:
                content = content[:desc_pos] + replacement_desc + content[desc_pos + len(target_desc):]

with open('docs/petstore.yaml', 'w') as f:
    f.write(content)
