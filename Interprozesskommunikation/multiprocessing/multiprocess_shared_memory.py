from multiprocessing import Process, Value, Array


class WorkerProcess(Process):
    """
    Stellt einen simplen Worker-Prozess dar,
    welcher einen geteilten Wert speichert und ein
    geteiltes Array verändert.
    """
    def __init__(self, v, arr):
        """
        Initialisiert die Basisklasse Process
        :param v: ein geteilter Wert
        :param arr: ein geteiltes Array
        """
        Process.__init__(self)
        self.v = v
        self.arr = arr

    def run(self):
        """
        Ändert den Wert und das Array
        :return: None
        """
        self.v.value = 1234
        for i in range(len(self.arr)):
            self.arr[i] = -self.arr[i]


if __name__ == "__main__":
    v = Value('d', 0.0)
    arr = Array('i', range(10))
    worker = WorkerProcess(v, arr)
    worker.start()
    worker.join()
    print(v.value)
    print(arr[:])