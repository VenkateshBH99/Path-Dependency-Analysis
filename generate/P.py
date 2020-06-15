from generate.staticfg.builder import CFGBuilder
from generate.PDA import PDA
from graphviz import Digraph
from itertools import combinations





class prop:
    def __init__(self,u):
        self.u=u
        self.flag=False
        self.t1=-1
        self.t2=-1
class Graph:
    def __init__(self,G):
        self.graph=[]
        for i in G:
            self.graph.append(i)
        self.V=[prop(i) for i in range(len(G))]
        self.time=-1
        self.T=[]




    def dfs(self,u):
        self.V[u].flag=True
        self.time+=1
        self.V[u].t1=self.time
        for i in self.graph[u]:
            if self.V[i].flag==False:
                self.dfs(i)

        self.time+=1
        self.V[u].t2=self.time
        self.T.append([self.V[u].t1,self.V[u].t2,u])


class Generate:
    def __init__(self,filename):
        self.cfg= CFGBuilder().build_from_file(filename, 'generate/'+filename)
        self.p=PDA()
        self.p.dfs(self.cfg.entryblock)
        # cfg.__iter__()
        self.Dict_edge,self.Dict_node=self.cfg.build_visual('generate/exampleCFG', 'pdf')
    def SCC(self,GR,G,Q,SUM_g):

        Summarized_nodes=[]
        gr=Graph(GR)
        for i in range(len(gr.V)):
            if gr.V[i].flag==False:
                gr.dfs(i)

        gr.T.sort(key=lambda k:k[1])
        while gr.T:
            q=gr.T.pop()
            g=Graph(G)
            g.dfs(q[2])
            # print(g.T)
            Summarized_nodes.append([])
            for i in g.T:
                Summarized_nodes[len(Summarized_nodes)-1].append(i[2])
            for i in range(len(g.T)-1):
                gr.T.pop()
            for i in range(len(G)):
                for j in range(len(g.T)):
                    if g.T[j][2] in G[i]:
                        ind=G[i].index(g.T[j][2])
                        G[i].pop(ind)

            print()

        print(Summarized_nodes)

        Sum_Dot=Digraph()


        arr=[[] for i in range(len(Summarized_nodes))]
        for i in range(len(Summarized_nodes)-1,-1,-1):
            for j in Summarized_nodes[i]:
                val="q"+str(j)
                temp=Q[val]
                if len(temp)>=2:
                    value=str(temp[0])+"_"+str(temp[1])
                    if i==len(Summarized_nodes)-1:
                        value2=str(temp[0])
                        arr[i].append(self.Dict_node[value2])
                    if value in self.Dict_edge.keys():
                        for k in self.Dict_edge[value]:
                            arr[i].append(k)
                else:
                    value=str(temp[0])
                    arr[i].append(self.Dict_node[value])
                if i==0:
                    value="Final"
                    arr[i].append(value)


        print(arr)
        name="Q"
        for i in range(len(Summarized_nodes)):
            j=len(Summarized_nodes)-i-1
            temp=name+str(i)
            value=""
            for k in range(len(arr[j])-1):
                value+=arr[j][k]+" ^ "
            if len(arr[j])>=1:
                value+=arr[j][len(arr[j])-1]
            Sum_Dot.node(temp,value)

        name="Q"
        for i in range(len(Summarized_nodes)-1):
            temp=name+str(i)
            temp1=name+str(i+1)
            Sum_Dot.edge(temp,temp1)


        Sum_Dot.render(str(SUM_g)+"_Sum.pdf",view=True)
        # print(arr)
        print(self.Dict_edge)
        print(self.Dict_node)






    def build_Path(self,cfg,g):
        p=PDA()
        p.dfs(cfg.entryblock)
        T=[]
        Q={}
        Connect={}
        End={}
        temp=PDA()
        start=[]
        temp.path_dfs(cfg.entryblock,[],[],p.visited,p.cond)
        T.append(temp.path)
        count=0
        q="q"

        st=temp.path[0][0]

        for j in temp.path:
            value=q+str(count)
            Q[value]=j
            if j[0] not in Connect.keys():
                Connect[j[0]]=[]
            Connect[j[0]].append(value)
            if j[-1] not in End.keys():
                End[j[-1]]=[]
            End[j[-1]].append(value)
            count+=1

        # print(T)
        for i in range(1,len(p.cond)):
            if p.cond[i]=='lh':
                temp=PDA()
                temp.path_dfs(p.visited[i],[],[],p.visited,p.cond)
                T.append(temp.path)
                for j in temp.path:
                    value=q+str(count)
                    Q[value]=j
                    if j[0] not in Connect.keys():
                        Connect[j[0]]=[]
                    Connect[j[0]].append(value)
                    if j[-1] not in End.keys():
                        End[j[-1]]=[]
                    End[j[-1]].append(value)
                    count+=1

        G=[[] for i in range(count)]
        GR=[[] for i in range(count)]


        T1=[]
        final=[]
        for i in Connect:
            for qm in Connect[i]:
                # print(qm)
                f=Q[qm]
                f=f[-1]
                # print(f[-1])
                if i==st:
                    start.append(qm)
                if f in Connect.keys():
                    for qn in Connect[f]:
                        # if qm!=qn:
                        T1.append((qm,qn))
                        a=int(qm.split('q')[1])
                        b=int(qn.split('q')[1])
                        """ original graph"""
                        G[a].append(b)
                        """Reverse graph"""
                        GR[b].append(a)
                else:
                    if qm not in final:
                        final.append(qm)



        # print(T)
        print(Q)
        dot=Digraph()
        for i in Q:
            if i in start and i in final:
                dot.node(i,i+': start & final')
            elif i in start:
                dot.node(i,i+': start')
            elif i in final:
                dot.node(i,i+': final')

            else:
                dot.node(i,i)

        # print(Connect)
        # print(End)

        print(T1)
        ed=[]
        for i in range(len(T1)):
            s=list(T1[i])
            # print(s)
            dot.edge(s[0],s[1])


        dot.render(str(g)+'.pdf',view=True)

        print("start:",start)
        print("final:",final)
        """Strongly Connected Components"""
        self.SCC(GR,G,Q,g)
        print("------------------------")
        g+=1




        for sub in cfg.functioncfgs:
            # print(sub.)
            self.build_Path(cfg.functioncfgs[sub],g)
            g+=1


# build_Path(cfg,1)

