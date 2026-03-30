def bfs(g,start):
    q=[start]; seen={start}; out=[]
    while q:
        n=q.pop(0); out.append(n)
        for nb in sorted(g.adj.get(n,[])):
            if nb not in seen:
                seen.add(nb); q.append(nb)
    return out

def dfs(g,start):
    st=[start]; seen=set(); out=[]
    while st:
        n=st.pop()
        if n in seen: continue
        seen.add(n); out.append(n)
        st.extend(sorted(g.adj.get(n,[]), reverse=True))
    return out
