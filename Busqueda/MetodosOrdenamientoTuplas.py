class MetodosOrdenamientoTuplas:

    def comparar(self, a, b):
        if a[1] > b[1]:
            return True
        elif a[1] == b[1]:
            return a[0] < b[0]
        else:
            return False
        
    def timSort(self, arreglo):
        return sorted(arreglo, key=lambda x: (-x[1], x[0]))
    
    def combSort(self, arreglo):
        n = len(arreglo)
        gap = n
        shrink = 1.3
        sorted = False

        while not sorted:
            gap = int(gap / shrink)
            if gap <= 1:
                gap = 1
            sorted = True
            i = 0

            while i + gap < n:
                if not self.comparar(arreglo[i], arreglo[i + gap]):
                    arreglo[i], arreglo[i + gap] = arreglo[i + gap], arreglo[i]
                    sorted = False
                i += 1
        return arreglo
    
    def selectionSort(self, arreglo):
        n = len(arreglo)
        for i in range(n):
            max_idx = i
            for j in range(i + 1, n):
                if self.comparar(arreglo[j], arreglo[max_idx]):
                    max_idx = j
            arreglo[i], arreglo[max_idx] = arreglo[max_idx], arreglo[i]
        return arreglo
    
    def quickSort(self, arreglo):
        if len(arreglo) <= 1:
            return arreglo
        else:
            pivot = arreglo[0]
            left = [x for x in arreglo[1:] if self.comparar(x, pivot)]
            right = [x for x in arreglo[1:] if not self.comparar(x, pivot)]
            return self.quickSort(left) + [pivot] + self.quickSort(right)
        
    def heapify(self, arreglo, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and self.comparar(arreglo[left], arreglo[largest]):
            largest = left

        if right < n and self.comparar(arreglo[right], arreglo[largest]):
            largest = right

        if largest != i:
            arreglo[i], arreglo[largest] = arreglo[largest], arreglo[i]
            self.heapify(arreglo, n, largest)

    def heapSort(self, arreglo):
        n = len(arreglo)

        for i in range(n // 2 - 1, -1, -1):
            self.heapify(arreglo, n, i)
        for i in range(n - 1, 0, -1):
            arreglo[i], arreglo[0] = arreglo[0], arreglo[i]
            self.heapify(arreglo, i, 0)
        return arreglo
    
    def gnomeSort(self, arreglo):
        n = len(arreglo)
        index = 0

        while index < n:
            if index == 0:
                index += 1
            if self.comparar(arreglo[index], arreglo[index - 1]):
                index += 1
            else:
                arreglo[index], arreglo[index - 1] = arreglo[index - 1], arreglo[index]
                index -= 1
        return arreglo
    
    def binaryInsertionSort(self, arreglo):
        def binarySearch(arreglo, key, start, end):
            if start == end:
                if self.comparar(key, arreglo[start]):
                    return start
                else:
                    return start + 1
            if start > end:
                return start
            
            mid = (start + end) // 2
            if self.comparar(key, arreglo[mid]):
                return binarySearch(arreglo, key, start, mid-1)
            else:
                return binarySearch(arreglo, key, mid+1, end)
            
        for i in range(1, len(arreglo)):
            key = arreglo[i]
            j = binarySearch(arreglo, key, 0, i-1)
            arreglo = arreglo[:j] + [key] + arreglo[j:i] + arreglo[i+1:]
        return arreglo
    
    def bubbleSort(self, arreglo):
        n = len(arreglo)
        for i in range(n):
            for j in range(0, n-i-1):
                if not self.comparar(arreglo[j], arreglo[j+1]):
                    arreglo[j], arreglo[j+1] = arreglo[j+1], arreglo[j]
        return arreglo
    
    def bitonicSort(self, arreglo):
        def compAndSwap(arreglo, i, j, dire):
            if (dire == 1 and ((arreglo[i][1] < arreglo[j][1]) or (arreglo[i][1] == arreglo[j][1] and arreglo[i][0] > arreglo[j][0]))) or \
                (dire == 0 and ((arreglo[i][1] > arreglo[j][1]) or (arreglo[i][1] == arreglo[j][1] and arreglo[i][0] < arreglo[j][0]))):
                arreglo[i], arreglo[j] = arreglo[j], arreglo[i]

        def bitonicMerge(arreglo, low, cnt, dire):
            if cnt > 1:
                k = cnt // 2
                for i in range(low, low + k):
                    compAndSwap(arreglo, i, i + k, dire)
                bitonicMerge(arreglo, low, k, dire)
                bitonicMerge(arreglo, low + k, k, dire)

        def bitonicSortRec(arreglo, low, cnt, dire):
            if cnt > 1:
                k = cnt // 2
                bitonicSortRec(arreglo, low, k, 1)
                bitonicSortRec(arreglo, low + k, k, 0)
                bitonicMerge(arreglo, low, cnt, dire)

        n = len(arreglo)
        bitonicSortRec(arreglo, 0, n, 1)
        return arreglo
    
    def pigeonholeSort(self, arreglo):
        if not arreglo:
            return arreglo
        
        minValue = min(arreglo, key=lambda x: x[1])[1]
        maxValue = max(arreglo, key=lambda x: x[1])[1]
        size = maxValue - minValue + 1

        holes = [[] for _ in range(size)]

        for item in arreglo:
            holes[item[1] - minValue].append(item)

        resultado = []

        for hole in reversed(holes):
            if hole:
                resultado.extend(sorted(hole, key=lambda x: x[0]))
        return resultado
    
    def bucketSort(self, arreglo):
        if not arreglo:
            return arreglo
        
        maxValue = max(arreglo, key=lambda x: x[1])[1]
        buckets = [[] for _ in range(maxValue + 1)]

        for item in arreglo:
            buckets[item[1]].append(item)

        resultado = []
        for bucket in buckets:
            if bucket:
                resultado.extend(sorted(bucket, key=lambda x: x[0]))
        return resultado
    
    def radixSort(self, arreglo):
        if not arreglo:
            return arreglo
        
        maxValue = max(arreglo, key=lambda x: x[1])[1]
        exp = 1
        n = len(arreglo)

        output = [0] * n

        while maxValue // exp > 0:
            count = [0] * 10

            for i in range(n):
                count[(arreglo[i][1] // exp) % 10] += 1

            for i in range(8, -1, -1):
                count[i] += count[i+1]

            for i in range(n-1, -1, -1):
                index = (arreglo[i][1] // exp) % 10
                count[index] -= 1
                output[count[index]] = arreglo[i]

            arreglo = output[:]
            exp *= 10

        i = 0
        while i < len(arreglo):
            j = i
            while j < len(arreglo) and arreglo[i][1] == arreglo[j][1]:
                j += 1
            arreglo[i:j] = sorted(arreglo[i:j], key=lambda x: x[0])
            i = j
        return arreglo
    
    @staticmethod
    def treeSort(arreglo):
        class Node:
            def __init__(self, key):
                self.left = None
                self.right = None
                self.val = key

        def insert(root, key):
            if root is None:
                return Node(key)
            if (key[1] > root.val[1]) or (key[1] == root.val[1] and key[0] < root.val[0]):
                root.left = insert(root.left, key)
            else:
                root.right = insert(root.right, key)
            return root
        
        def inorder(root, res):
            if root is not None:
                inorder(root.left, res)
                res.append(root.val)
                inorder(root.right, res)

        def treeSort(self, arreglo):
            if not arreglo:
                return arreglo
            
            root = None
            for key in arreglo:
                root = insert(root, key)

            result = []
            inorder(root, result)
            return result