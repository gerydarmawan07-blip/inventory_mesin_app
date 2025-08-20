from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.types import Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

# Buat database SQLite di folder data/
engine = create_engine("sqlite:///data/inventory.db", echo=False)
Base = declarative_base()
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()

# ---------------------------
# Tabel User
# ---------------------------
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    role = Column(String, default="user")  # admin / user

# ---------------------------
# Tabel Mesin
# ---------------------------
class Mesin(Base):
    __tablename__ = "mesin"
    id = Column(Integer, primary_key=True, index=True)
    kode_mesin = Column(String, unique=True, index=True, nullable=False)
    nama_mesin = Column(String, nullable=False)
    brand = Column(String, nullable=True)
    sg = Column(String, nullable=True)
    nomor_dokumen = Column(String, nullable=True)
    jumlah_mesin = Column(Integer, default=0)
    harga_mesin = Column(Float, default=0.0)
    tanggal_pemasukan = Column(Date, nullable=True)
    tanggal_penjualan = Column(Date, nullable=True)
    tanggal_sewa = Column(Date, nullable=True)
    jumlah_sewa = Column(Integer, default=0)
    tanggal_dikembalikan = Column(Date, nullable=True)
    jumlah_mesin_kembali = Column(Integer, default=0)
    kondisi_mesin = Column(String, nullable=True)
    keterangan = Column(String, nullable=True)

# ---------------------------
# Tabel History
# ---------------------------
class History(Base):
    __tablename__ = "history"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False)
    action = Column(String, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)

# Buat tabel jika belum ada
Base.metadata.create_all(bind=engine)
