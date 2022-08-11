"""
cob coba aja nih
"""

def ekstraksi_data():

    hasil = dict()
    hasil['tanggal'] = '24 Agustus 2021'
    hasil['waktu'] = '12:05:52 wib'
    hasil['magnitudo'] = '4.0'
    hasil['lokasi'] = {'ls':1.48, 'bt':134.01}
    hasil['pusat'] = 'Pusat gempa berada di darat 18 KM barat laut Ransiki'
    hasil['dirasakan'] = 'Dirasakan (skala MMI) II-III Manokwari, II-III Ransiki'

    return hasil

def tampilkan_data(result):
    print('Gempa Terakhir Berdasarkan BMKG')
    print(f"Tanggal {result['tanggal']}")
    print(f"Waktu {result['waktu']}")
    print(f"Magnitudo {result['magnitudo']}")
    print(f"Lokasi : LS = {result['lokasi'] ['ls']}, BT = {result['lokasi'] ['bt']}")
    print(f"{result['pusat']}")
    print(f"{result['dirasakan']}")


#if __name__ == '__main__':
    print('Aplikasi Utama')
    result = ekstraksi_data()
    tampilkan_data(result)
