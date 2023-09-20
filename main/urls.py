from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf.urls.static import static

app_name = 'SPPD'
urlpatterns = [
    path('', views.loginUser, name='login'),
    path('adduser/', views.addUser, name='adduser'),
    path('master_jabatan/tambah/', views.addJabatan, name='tambah'),
    path('master_jabatan/hapus/<int:idedit>', views.hapusJabatan, name='hapus'),
    # path('form_edit/', views.form_edit, name='formEdit'),
    path('master_jabatan/edit/<int:idedit>', views.editJabatan, name='editData'),
    # master lokasi
    path('master_lokasi/', views.lokasi, name='lokasi'),
    path('master_lokasi/tambah/', views.addLokasi, name='tambah'),
    path('master_lokasi/hapus/<int:idedit>', views.hapusLokasi, name='hapus'),
    path('master_lokasi/edit/<int:idedit>', views.editLokasi, name='editData'),
    # master Organisasi
    path('master_organisasi/', views.organisasi, name='organisasi'),
    path('master_organisasi/tambah/', views.addOrganisasi, name='tambah'),
    path('master_organisasi/hapus/<int:idedit>', views.hapusOrganisasi, name='hapus'),
    path('master_organisasi/edit/<int:idedit>', views.editOrganisasi, name='editData'),
    # master Pegawai
    path('master_pegawai/', views.pegawai, name='pegawai'),
    path('master_pegawai/tambah/', views.addPegawai, name='tambah'),
    path('master_pegawai/hapus/<int:idedit>', views.hapusPegawai, name='hapus'),
    path('master_pegawai/edit/<int:idedit>', views.editPegawai, name='editData'),


    path('master_tahun/', views.tahun, name='tahun'),
    path('master_tahun/tambah/', views.addTahun, name='tambah'),
    path('master_tahun/hapus/<int:idedit>', views.hapusTahun, name='hapus'),
    path('master_tahun/edit/<int:idedit>', views.editTahun, name='editData'),
    # path('data/', views.read, name='read'),

    path('dash/', views.dash, name='dash'),
    path('laporan/', views.laporan, name='laporan'),
    path('master/', views.master, name='master'),
    path('spt/', views.spt, name='spt'),
    path('sppd/', views.sppd, name='sppd'),
    path('master_jabatan/', views.jabatan, name='jabatan'),
    path('master_kegiatan/', views.kegiatan, name='kegiatan'),
    path('master_pengesah/', views.pengesah, name='pengesah'),
    path('master_ssh/', views.ssh, name='ssh'),
    
]