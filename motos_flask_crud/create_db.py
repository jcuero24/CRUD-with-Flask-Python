import sqlite3

conn = sqlite3.connect('motos.db')
conn.execute('''
CREATE TABLE IF NOT EXISTS motos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    modelo TEXT NOT NULL,
    marca TEXT NOT NULL,
    velocidad_maxima INTEGER NOT NULL
)
''')

# Lista de las 30 motos más rápidas del mundo
motos = [
    ('Dodge Tomahawk', 'Dodge', 560),
    ('Kawasaki Ninja H2R', 'Kawasaki', 400),
    ('MTT Turbine Superbike Y2K', 'MTT', 365),
    ('Lightning LS-218', 'Lightning', 351),
    ('Kawasaki Ninja H2', 'Kawasaki', 337),
    ('Ducati Superleggera V4', 'Ducati', 330),
    ('Suzuki Hayabusa', 'Suzuki', 312),
    ('BMW S1000RR', 'BMW', 303),
    ('MV Agusta F4 RC', 'MV Agusta', 302),
    ('Aprilia RSV4 1100 Factory', 'Aprilia', 305),
    ('Ducati Panigale V4 R', 'Ducati', 305),
    ('Suzuki GSX-R1000', 'Suzuki', 299),
    ('Yamaha YZF-R1M', 'Yamaha', 299),
    ('Honda CBR1000RR-R Fireblade SP', 'Honda', 299),
    ('Kawasaki Ninja ZX-14R', 'Kawasaki', 299),
    ('BMW HP4 Race', 'BMW', 299),
    ('MV Agusta Brutale 1000 Serie Oro', 'MV Agusta', 302),
    ('Bimota Tesi H2', 'Bimota', 299),
    ('Norton V4 SS', 'Norton', 300),
    ('Ducati 1199 Panigale R', 'Ducati', 299),
    ('Energica Ego', 'Energica', 240),
    ('Confederate FA-13 Combat Bomber', 'Confederate', 257),
    ('Kawasaki ZZR1400', 'Kawasaki', 299),
    ('Honda VFR1200F', 'Honda', 299),
    ('Ducati Diavel', 'Ducati', 270),
    ('MV Agusta F4 LH44', 'MV Agusta', 302),
    ('BMW M1000RR', 'BMW', 306),
    ('Yamaha MT-10 SP', 'Yamaha', 299),
    ('Kawasaki Ninja 1000SX', 'Kawasaki', 299),
    ('Harley-Davidson LiveWire', 'Harley-Davidson', 177)
]

# Insertar las motos en la base de datos
conn.executemany('INSERT INTO motos (modelo, marca, velocidad_maxima) VALUES (?, ?, ?)', motos)
conn.commit()
conn.close()
