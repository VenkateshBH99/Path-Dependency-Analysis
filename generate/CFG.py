flag=True
for exit_ in curr_block.exits:
    flag=False
    if exit_.target in visited:
        ind=visited.index(exit_.target)
        cond[ind]="lh"
        continue

assert  visited

while to_visit:
    block = to_visit.pop(0)
    visited.add(block)
    print(block.id)
    for exit_ in block.exits:
        if exit_.target in visited or exit_.target in to_visit:
            continue
        to_visit.append(exit_.target)
assert visited


flag=True
for exit_ in curr_block.exits:
    flag=False
    if exit_.target not in visited:
        ind=visited_main.index(exit_.target)
        if cond_main[ind]=='lh':
            visited.append(exit_.target)
            arr.append(exit_.target.id)
            brr.append(exit_.target)
            path.append(arr)
            path_block.append(brr)
            continue
        path_dfs(exit_.target,list(arr),list(brr),visited_main,cond_main)
    else:
        arr.append(exit_.target.id)
        brr.append(exit_.target)
        path.append(arr)
        path_block.append(brr)
if flag:
    path.append(arr)
    path_block.append(brr)

assert path_bloxk









