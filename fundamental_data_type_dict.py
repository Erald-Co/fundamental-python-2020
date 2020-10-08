kamus = {'anak': 'son', 'istri': 'wife', 'ayah': 'father', 'ibu': 'mother'}

print("/nData ini dikirimkan oleh server Gojek untuk memberikan info driver di sekitar pemakai aplikasi")
data_dari_server_gojek = {
    'tanggal': '2020-06-10',
    'driver_list': [{'nama': 'Eko', 'jarak': 100}, {'nama': 'Dwi', 'jarak': 10}, {'nama': 'Tri', 'jarak': 1000},
                    {'nama': 'Catur', 'jarak': 200}]
}

print(data_dari_server_gojek)
print("Driver di sekitar anda {}".format(data_dari_server_gojek['driver_list']))
print("Jarak driver {} adalah {}".format(data_dari_server_gojek['driver_list'][0]['nama'], data_dari_server_gojek[
    'driver_list'][0]['jarak']))
