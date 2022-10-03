from lib2to3.pytree import Node
from select import select


class NodeTabungan:
    no_rekening = None
    nama = None
    saldo = None
    next = None
 
    def __init__(self, no_rekening, nama, saldo=0):
        self.no_rekening = no_rekening
        self.nama = nama
        self.saldo = saldo
        self.next = None

class SLNC:
    def __init__(self):
        self._head = None
        self._tail = None
        self._next = None
        self._size = 0
    
    def __len__(self):
        return self._size
    
    def isEmpty(self):
        return self._size == 0
    
    def insert_head(self, norek, name, jumlah):
        baru = NodeTabungan(norek,name,jumlah)
        if self.isEmpty() == True:
            self._head = baru
            self._tail = baru
            self._tail._next = None
        else:
            baru._next = self._head
            self._head = baru
        self._size += 1

    # def delete(self, index):
    #     temp = self._head
    #     if temp != None:
    #         if(temp.data == index):
    #             self._head = self._next
    
    def print(self):
        if self.isEmpty() == False:
            bantu = self._head
            while(bantu!=None):
                print("Norek: ",bantu.no_rekening, " ",end='')
                print()
                print("Nama: ",bantu.nama," ",end='')
                print()
                print("Saldo: ",bantu.saldo," ",end='')
                print()
                bantu = bantu._next
            print()
        else:
            print("Kosong")
    
    def filter(self, jumlah):
        hitung = 0
        # if self.no_rekening < jumlah :
        self.nama = None
        self.no_rekening = None
        self.saldo = None
        # hitung += 1
        print("Rekening yang berhasil dihapus sebanyak ",hitung," buah")
        print()

    def update(self, persen):
        if persen > 100 or persen < 0:
            print("Maaf  besaran persen harus diantara 0-100")
        else:
            bantu = self._head
            while(bantu!=None):
                self._head.no_rekening = bantu.no_rekening + (bantu.no_rekening*(persen/100))
                bantu = bantu._next
            print("Semua saldo rekening berhasil ditambah sebanyak ",persen,"%")
            print()

slnc=SLNC()
slnc.insert_head(201,"Hanif", 250000)
slnc.insert_head(110,"Yudha", 150000)
slnc.print()
slnc.filter(100)
slnc.print()
slnc.update(200)
slnc.update(50)
slnc.print()