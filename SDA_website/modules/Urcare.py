def urca(heap,x):
    'functia il baga pe x in heap'
    l=len(heap)
    heap.append(x)
    poz =l
    while heap[int((poz-1)/3)]<x and poz>0:
        heap[poz]=heap[int((poz-1)/3)]
        heap[int((poz-1)/3)]=x
        poz =int((poz-1)/3)
    return heap