from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime

# ---------------------------
# Database setup
# ---------------------------
DATABASE_URL = "sqlite:///inventory_mesin.db"  # SQLite lokal
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

# ---------------------------
# Tabel User
# ---------------------------
class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    role = Column(String, default="user")  # "admin" atau "user"

# ---------------------------
# Tabel Mesin
# ---------------------------
class Mesin(Base):
    __tablename__ = "mesin"
    id = Column(Integer, primary_key=True)
    kode_mesin = Column(String, unique=True, nullable=False)
    nama_mesin = Column(String)
    brand = Column(String)
    sg = Column(String)
    nomor_dokumen = Column(String)
    jumlah_mesin = Column(Integer, default=0)
    harga_mesin = Column(Float, default=0.0)
    tanggal_pemasukan = Column(DateTime, default=datetime.now)
    tanggal_penjualan = Column(DateTime, nullable=True)
    tanggal_sewa = Column(DateTime, nullable=True)
    jumlah_sewa = Column(Integer, default=0)
    tanggal_dikembalikan = Column(DateTime, nullable=True)
    jumlah_mesin_kembali = Column(Integer, default=0)
    kondisi_mesin = Column(String, default="Baik")
    keterangan = Column(String, nullable=True)

# ---------------------------
# Tabel History
# ---------------------------
class History(Base):
    __tablename__ = "history"
    id = Column(Integer, primary_key=True)
    mesin_id = Column(Integer)
    aksi = Column(String)
    waktu = Column(DateTime, default=datetime.now)

# ---------------------------
# Buat tabel jika belum ada
# ---------------------------
Base.metadata.create_all(engine)

# ---------------------------
# Fungsi tambah user (opsional)
# ---------------------------
def tambah_user(username, password, role="user"):
    exist = session.query(User).filter_by(username=username).first()
    if exist:
        print(f"User {username} sudah ada!")
        return
    u = User(username=username, password=password, role=role)
    session.add(u)
    session.commit()
    print(f"User {username} berhasil ditambahkan dengan role {role}!")
