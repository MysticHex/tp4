import matplotlib.pyplot as plt
import sqlite3
from prettytable import PrettyTable

conn = sqlite3.connect('TPAndika.db')
cursor = conn.cursor()

def make_table():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS table_buku (
            id_buku INTEGER PRIMARY KEY AUTOINCREMENT,
            judul TEXT NOT NULL,
            penulis TEXT NOT NULL,
            tahun_terbit INTEGER,
            genre TEXT,
            stok INTEGER NOT NULL
        );
    """)
    conn.commit()

def insert_book(judul, penulis, tahun_terbit, genre, stok):
    query = f"INSERT INTO table_buku VALUES(NULL,'{judul}', '{penulis}', {tahun_terbit}, '{genre}', {stok});"
    conn.execute(query)
    conn.commit()

def tampil_book():
    cursor.execute('SELECT * FROM table_buku')

    results = cursor.fetchall()

    table = PrettyTable(field_names=['id_buku', 'judul', 'penulis', 'tahun_terbit', 'genre', 'stok'])
    for row in results:
        table.add_row(row)

    print(table)

def delete_book(id_buku):
    query = f"DELETE FROM table_buku WHERE id_buku={id_buku};"
    conn.execute(query)
    conn.commit()
    conn.close()

def statistic():
    query = "SELECT genre, SUM(stok) as total_stok FROM table_buku GROUP BY genre;"
    df = pd.read_sql_query(query, conn)
    plt.figure(figsize=(10, 6))
    plt.bar(df['genre'], df['total_stok'], color='skyblue')
    plt.xlabel('Genre')
    plt.ylabel('Total Stok')
    plt.title('Total Stok by Genre')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

while True:
    pilihan=int(input("Masukan menu: "))

    match pilihan:
        case 1:
            make_table()
        case 2:
            judul=input("Masukan Judul\t:")
            penulis=input("Masukan Penulis\t:")
            tahun_terbit=int(input("Masukan tahun terbit\t:"))
            genre=input("Masukan Genre\t:")
            stok=int(input("Masukan Stok\t:"))
            insert_book(judul,penulis,tahun_terbit,genre,stok)
        case 3:
            tampil_book()
        case 4:
            id_buku=int(input("Masukan id buku"))
            delete_book(id_buku)
        case 5:
            statistic()
        case 6:
            break
    print("\n")