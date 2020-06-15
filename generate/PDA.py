class PDA:
    def __init__(self):

        self.visited=[]
        self.vis_name=[]
        self.cond=[]
        self.path=[]
        self.path_block=[]


    def bfs(self):
        visited = set()
        to_visit = [self.root.entryblock]

        while to_visit:
            block = to_visit.pop(0)
            visited.add(block)
            print(block.id)
            for exit_ in block.exits:
                if exit_.target in visited or exit_.target in to_visit:
                    continue
                to_visit.append(exit_.target)
        assert visited

    def dfs(self,curr_block):
        self.visited.append(curr_block)
        self.cond.append(None)
        self.vis_name.append(curr_block.id)
        flag=True
        for exit_ in curr_block.exits:
            flag=False
            if exit_.target in self.visited:
                ind=self.visited.index(exit_.target)
                self.cond[ind]="lh"
                continue
            self.dfs(exit_.target)
        if flag:
            ind=self.visited.index(curr_block)
            self.cond[ind]="le"

    def path_dfs(self,curr_block,arr,brr,visited_main,cond_main):


        self.visited.append(curr_block)
        arr.append(curr_block.id)
        brr.append(curr_block)
        flag=True
        for exit_ in curr_block.exits:
            flag=False
            if exit_.target not in self.visited:
                ind=visited_main.index(exit_.target)
                if cond_main[ind]=='lh':
                    self.visited.append(exit_.target)
                    arr.append(exit_.target.id)
                    brr.append(exit_.target)
                    self.path.append(arr)
                    self.path_block.append(brr)
                    continue
                self.path_dfs(exit_.target,list(arr),list(brr),visited_main,cond_main)
            else:
                arr.append(exit_.target.id)
                brr.append(exit_.target)
                self.path.append(arr)
                self.path_block.append(brr)
        if flag:
            self.path.append(arr)
            self.path_block.append(brr)







