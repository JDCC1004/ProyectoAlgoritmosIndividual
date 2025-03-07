class MetodosOrdenamiento:

    def timSort(self, arreglo):
        arreglo.sort()
        print(arreglo)
        return arreglo

    def combSort(self, arreglo):
        gap = len(arreglo)
        shrink = 1.3
        sorteado = False
        while not sorteado:
            gap = int(gap // shrink)
            if gap <= 1:
                gap = 1
            sorteado = True
            for i in range(len(arreglo) - gap):
                if arreglo[i] > arreglo[i + gap]:
                    arreglo[i], arreglo[i + gap] = arreglo[i + gap], arreglo[i]
                    sorteado = False
        return arreglo

    def selectionSort(self, arreglo):
        for i in range(len(arreglo)):
            minIndex = i
            for j in range(i + 1, len(arreglo)):
                if arreglo[j] < arreglo[minIndex]:
                    minIndex = j
            arreglo[i], arreglo[minIndex] = arreglo[minIndex], arreglo[i]
        return arreglo


    class Node:
        def __init__(self, value):
            self.left = None
            self.right = None
            self.value = value

    def insert(self, root, value):
        if root is None:
            return self.Node(value)
        else:
            if value < root.value:
                root.left = self.insert(root.left, value)
            else:
                root.right = self.insert(root.right, value)
        return root

    def inorder(self, root, resultado):
        if root:
            self.inorder(root.left, resultado)
            resultado.append(root.value)
            self.inorder(root.right, resultado)

    def treeSort(self, arreglo):
        if len(arreglo) == 0:
            return []
        root = self.treeSort(arreglo[0])
        for i in range(1, len(arreglo)):
            self.insert(root, arreglo[i])
        resultado = []
        self.inorder(root, resultado)
        return resultado

    def pigeonholeSort(self, arreglo):
        minValue = min(arreglo)
        maxValue = max(arreglo)
        size = maxValue - minValue + 1
        holes = [0] * size
        for x in arreglo:
            holes[x - minValue] += 1
        sorted_arreglo = []
        for i in range(size):
            while holes[i] > 0:
                sorted_arreglo.append(i - minValue)
                holes[i] -= 1
        return sorted_arreglo

    def bucketSort(self, arreglo):
        if len(arreglo) == 0:
            return arreglo
        bucketsCount = 10
        maxValue = max(arreglo)
        buckets = [[] for _ in range(bucketsCount)]
        for number in arreglo:
            index = int(number / (maxValue / bucketsCount))
            if index >= bucketsCount:
                index = bucketsCount - 1
            buckets[index].append(number)

        sorted_arreglo = []
        for bucket in buckets:
            sorted_arreglo.extend(sorted(bucket))
        return sorted_arreglo

    def quickSort(self, arreglo):
        if len(arreglo) <= 1:
            return arreglo
        pivot = arreglo[len(arreglo) // 2]
        left = [x for x in arreglo if x < pivot]
        mid = [x for x in arreglo if x == pivot]
        right = [x for x in arreglo if x > pivot]
        return self.quickSort(left) + mid + self.quickSort(right)

    def heapify(self, arreglo, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and arreglo[i] < arreglo[left]:
            largest = left
        if right < n and arreglo[largest] < arreglo[right]:
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

    def bitonicMerge(self, arreglo, low, cnt, direction):
        if cnt > 1:
            k = cnt // 2
            for i in range(low, low + k):
                if (direction == 1 and arreglo[i] > arreglo[i + k]) or (direction == 0 and arreglo[i] < arreglo[i + k]):
                    arreglo[i], arreglo[i + k] = arreglo[i + k], arreglo[i]
            self.bitonicMerge(arreglo, low, k, direction)
            self.bitonicMerge(arreglo, low + k, k, direction)

    def bitonicSortRecursive(self, arreglo, low, cnt, direction):
        if cnt > 1:
            k = cnt // 2
            self.bitonicSortRecursive(arreglo, low, k, 1)
            self.bitonicSortRecursive(arreglo, low + k, k, 0)
            self.bitonicMerge(arreglo, low, cnt, direction)

    def bitonicSort(self, arreglo):
        self.bitonicSortRecursive(arreglo, 0, len(arreglo), 1)
        return arreglo

    def gnomeSort(self, arreglo):
        index = 0
        while index < len(arreglo):
            if index == 0 or arreglo[index] >= arreglo[index - 1]:
                index += 1
            else:
                arreglo[index], arreglo[index - 1] = arreglo[index - 1], arreglo[index]
                index -= 1
        return arreglo

    def binaryInsertionSort(self, arreglo):

        def binarySearch(arreglo, value, start, end):
            if start == end:
                return start if arreglo[start] > value else start + 1
            if start > end:
                return start
            mid = (start + end) // 2
            if arreglo[mid] < value:
                return binarySearch(arreglo, value, mid - 1, end)
            elif arreglo[mid] > value:
                return binarySearch(arreglo, value, start, mid - 1)
            else:
                return mid

        for i in range(1, len(arreglo)):
            value = arreglo[i]
            j = binarySearch(arreglo, value, 0, i - 1)
            arreglo = arreglo[:j] + [value] + arreglo[i + 1:]
        return arreglo

    def countingSort(self, arreglo, exp):
        n = len(arreglo)
        output = [0] * n
        count = [0] * 10

        for i in range(n):
            index = (arreglo[i] // exp) % 10
            count[index] += 1

        for i in range(1, 10):
            count[i] += count[i - 1]

        i = n - 1
        while i >= 0:
            index = (arreglo[i] // exp) % 10
            output[count[index] - 1] = arreglo[i]
            count[index] -= 1
            i -= 1

        for i in range(len(arreglo)):
            arreglo[i] = output[i]

    def radixSort(self, arreglo):
        maxNum = max(arreglo)

        exp = 1
        while maxNum // exp > 0:
            self.countingSort(arreglo, exp)
            exp *= 10
        return arreglo