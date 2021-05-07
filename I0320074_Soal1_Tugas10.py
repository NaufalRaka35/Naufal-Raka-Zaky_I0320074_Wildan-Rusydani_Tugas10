judul = " Silahkan Isi Biodata Dibawah "
print(judul.center(70, "="))
nama = input("Nama :")
usia = input("Usia :")
alamat = input("Alamat:")
teks = "Nama: {}\nUsia: {}\nAlamat: {}".format(nama, usia, alamat)
file_data = open("file.txt", "w")
file_data.write(teks)
file_data.close()

judul = " Silahkan Isi Biodata Dibawah "
print(judul.center(70, "="))
nama = input("Nama :")
usia = input("Usia:")
alamat = input("Alamat:")
teks = "Nama: {}\nUsia: {}\nAlamat: {}".format(nama, usia, alamat)
file_data = open("file.txt", "a")
file_data.write(teks)
file_data.close()