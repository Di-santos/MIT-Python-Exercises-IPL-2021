def tree_max(arvore):
    if len(arvore['children']) == 0:
        return arvore['value']

    else:
        nums = []
        inicial = arvore['value']
        nums.append(inicial)

        for ramo in arvore['children']:
            max_ramo = tree_max(ramo)  
            nums.append(max_ramo)

    return max(nums)

def binary_tree_max(arvore):
    return tree_max(arvore)
