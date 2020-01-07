def coboara(heap):
    'functia coboara primul element din heap'
    poz=0
    l=len(heap)
    'ca sa nu iasa cu indicile din heap in while am facut un vector auxiliar care sa imi umple restul pana la 3*l+3 cu -1 '
    auxv=[-1]
    for i in range(1,l+2): auxv.append(-1)
    heap+=auxv+auxv+[-1]
    while heap[poz]<max(heap[3*poz+1],heap[3*poz+2],heap[3*poz+3]):
        for i in range(1,4):
            if heap[3*poz+i]== max(heap[3*poz+1],heap[3*poz+2],heap[3*poz+3]):
                aux=heap[poz]
                heap[poz]=heap[3*poz+i]
                heap[3*poz+i]=aux
                poz=3*poz+i
                break
    del heap[l:]
    return heap
