
#Muhamad Syarifudin
#5200411347

class RoundRobin:

    def ProsesData(self, no_of_processes):
        proses = []
        for i in range(no_of_processes):
            tenggat = []
            prosesKe = str(input("Memasukan Aplikasi : "))
            burstTime = int(input(f"Memasukan Burst Time Untuk Memproses {prosesKe}: "))
            tenggat.extend([prosesKe, 0, burstTime, 0, burstTime])

            proses.append(tenggat)
        quantumTime = int(input("Memasukan Quantum Time : "))
        RoundRobin.schedulingProcess(self, proses, quantumTime)

    def schedulingProcess(self, proses, quantumTime):
        Mulai = []
        selesai = []
        ekseskusiProses = []
        urutan = []
        s_time = 0
        while 1:
            temp = []
            for i in range(len(proses)):
                if proses[i][1] <= s_time and proses[i][3] == 0:
                    present = 0
                    if len(urutan) != 0:
                        for k in range(len(urutan)):
                            if proses[i][0] == urutan[k][0]:
                                present = 1

                    if present == 0:
                        temp.extend([proses[i][0], proses[i][1], proses[i][2], proses[i][4]])
                        urutan.append(temp)
                        temp = []

                    if len(urutan) != 0 and len(ekseskusiProses) != 0:
                        for k in range(len(urutan)):
                            if urutan[k][0] == ekseskusiProses[len(ekseskusiProses) - 1]:
                                urutan.insert((len(urutan) - 1), urutan.pop(k))

            if len(urutan) == 0:
                break
            if len(urutan) != 0:
                if urutan[0][2] > quantumTime:

                    Mulai.append(s_time)
                    s_time = s_time + quantumTime
                    e_time = s_time
                    selesai.append(e_time)
                    ekseskusiProses.append(urutan[0][0])
                    for j in range(len(proses)):
                        if proses[j][0] == urutan[0][0]:
                            break
                    proses[j][2] = proses[j][2] - quantumTime
                    urutan.pop(0)
                elif urutan[0][2] <= quantumTime:

                    Mulai.append(s_time)
                    s_time = s_time + urutan[0][2]
                    e_time = s_time
                    selesai.append(e_time)
                    ekseskusiProses.append(urutan[0][0])
                    for j in range(len(proses)):
                        if proses[j][0] == urutan[0][0]:
                            break
                    proses[j][2] = 0
                    proses[j][3] = 1
                    proses[j].append(e_time)
                    urutan.pop(0)
        t_time = RoundRobin.calculateTurnaroundTime(self, proses)
        w_time = RoundRobin.calculateWaitingTime(self, proses)
        RoundRobin.printData(self, proses, t_time, w_time, ekseskusiProses)

    def calculateTurnaroundTime(self, proses):
        total_putaran_waktu = 0
        for i in range(len(proses)):
            putaran_waktu = proses[i][5] - proses[i][1]

            total_putaran_waktu = total_putaran_waktu + putaran_waktu
            proses[i].append(putaran_waktu)
        rataTurnTime = total_putaran_waktu / len(proses)

        return rataTurnTime

    def calculateWaitingTime(self, proses):
        total_waktu_tunggu = 0
        for i in range(len(proses)):
            waktu_tunggu = proses[i][6] - proses[i][4]

            total_waktu_tunggu = total_waktu_tunggu + waktu_tunggu
            proses[i].append(waktu_tunggu)
        rataWaitTime = total_waktu_tunggu / len(proses)

        return rataWaitTime

    def printData(self, proses, rataTurnTime, rataWaitTime, ekseskusiProses):
        proses.sort(key=lambda x: x[0])

        print(
            "prosesKe  Arrival_Time  Rem_burstTime   Completed  Original_burstTime  Completion_Time  Waktu_Berputar  Waktu_Tunggu")
        for i in range(len(proses)):
            for j in range(len(proses[i])):
                print(proses[i][j], end="\t\t\t\t")
            print()
        print(f'Rata-Rata Waktu Berputar: {rataTurnTime}')
        print(f'Rata-Rata Waktu Tunggu: {rataWaitTime}')
        print(f'Urutan Proses: {ekseskusiProses}')


if __name__ == "__main__":
    no_of_processes = int(input("Memasukan Jumlah Proses : "))
    rr = RoundRobin()
    rr.ProsesData(no_of_processes)