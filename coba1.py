"""
latihan dictionary, json
"""

sukses = dict()
sukses['satu']='one1'
sukses['dua']='two'
sukses['tiga']='three'
sukses['cabang']={'ranting':'pohon', 'dahan': 'kiri'}
print(sukses)
print(sukses['cabang'])
print(f"adalah {sukses['cabang']['ranting']} {sukses['cabang']['dahan']}")
sukses1= {'satu':'one', 'dua': 'two', 'tiga': 'three'}
print(f"dua adalah {sukses1['dua']}")
