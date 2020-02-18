
import collections
def earliest_ancestor(ancestors, starting_node):
    q = collections.deque()
    q.append((starting_node, 1))
    min_id = (99999, 1)
    level = 0
    while q:
        level += 1
        for _ in range(len(q)):
            node, cur_lev = q.popleft()
            parents = [i[0] for i in ancestors if i[1] == node]
            if parents:
                for parent in parents:
                    q.append((parent, level))
            else:
                if cur_lev > min_id[1]:
                    min_id = (node, cur_lev)
                elif cur_lev == min_id[1]:
                    min_id = min(min_id, (node, cur_lev), key=lambda t: t[0])
                if not q:
                    break
    return min_id[0] if level > 1 else -1