

#MuhamadSyarifudin
#5200411347

#Menghitung Kapasitas Total Ram & Total Petabit
TotalRam = int(input("Kapasitas total RAM (MBps): "))
TotalBlok = int(input("Blok/unit: "))

TotalPetabit = TotalRam/TotalBlok

print("Total Petabit:",TotalPetabit)
print("Kapasitas Per Petabit :",TotalPetabit)

#Total Ram Dipakai & Tidak Terpakai
PS = int(input("Ram yang digunakan oleh Program 1: "))
PD = int(input("Ram yang digunakan oleh Program 2: "))

TotalRT = PS + PD
TotalTD = TotalRam - (PS + PD)
print("Totak Ram yang terpakai: ",TotalRT,"MBps")
print("Total Ram yang tidak terpakai: ",TotalTD,"MBps")

#Jumlah Blok Bernilai 1 dan 0

JumlahBS = PS/TotalPetabit
JumlahBN = TotalBlok-JumlahBS

print("Jumlah Blok Bernilai 1: ",JumlahBS)
print("Jumlah Blok Bernilai 0: ",JumlahBN)