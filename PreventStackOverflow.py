# Put below snippet in your code and then put @bootstrap over recursive function. And replace instances of return with yield. 
# If a function does not return anything still write yield at the end.
# If you are calling another function from within, do it with yield.

from types import GeneratorType
def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to
    return wrappedfunc

# Example

@bootstrap
def dfs(visited, graph, node, arr, brr, ans):
    if node not in visited:
        visited.add(node)
        for neighbour in graph[node]:
            arr.append(arr[-1] + neighbour[1])
            brr.append(brr[-1] + neighbour[2])
            ans[neighbour[0]] = bisect.bisect_right(brr, arr[-1]) - 1
            yield dfs(visited, graph, neighbour[0], arr, brr, ans)
    arr.pop()
    brr.pop()
    yield