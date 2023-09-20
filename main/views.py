from django.shortcuts import render, redirect
from .models import UserNew
from .models import MasterJabatan
from .models import MasterLokasi
from .models import MasterOrganisasi
from .models import MasterPegawai
from .models import MasterTahun

from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth.hashers import make_password

# Create your views here.
def login(request):
    return render(request, 'auth/login.html')

def dash(request):
    return render(request, 'dashboard/index.html')

def laporan(request):
    return render(request, 'laporan/laporan.html')

def master(request):
    return render(request, 'master/master.html')

def spt(request):
    return render(request, 'spt/spt.html')

def sppd(request):
    return render(request, 'sppd/input_sppd.html')

def jabatan(request):
    jabatan = MasterJabatan.objects.all()
    contex = {
        'jabatan' : jabatan
    }
    return render(request, 'master/master_jabatan.html', contex)

def addJabatan(request):
    if request.method == "POST":
        jabatan = request.POST.get('jabatan')

        insert = MasterJabatan()
        insert.jabatan = jabatan

        insert.save()

        return redirect('SPPD:jabatan')

def editJabatan(request, idedit=""):
    if request.method == "POST":
        
        jabatan = request.POST['jabatanedit']
        MasterJabatan.objects.filter(id=idedit).update(jabatan = jabatan)
        return redirect('SPPD:jabatan')

def hapusJabatan(request, idedit):
    hapus = MasterJabatan.objects.get(id=idedit)

    hapus.delete()
    return redirect('SPPD:jabatan')

def kegiatan(request):
    return render(request, 'master/master_kegiatan.html')

def lokasi(request):
    lokasi = MasterLokasi.objects.all()
    contex = {
        'lokasi' : lokasi
    }
    return render(request, 'master/master_lokasi.html', contex)

def addLokasi(request):
    if request.method == "POST":
        kd_lokasi = request.POST.get('kd_lokasi')
        urai = request.POST.get('urai')

        insert = MasterLokasi()
        insert.kd_lokasi = kd_lokasi
        insert.urai = urai

        insert.save()

        return redirect('SPPD:lokasi')

def editLokasi(request, idedit=""):
    if request.method == "POST":
        
        kd_lokasi = request.POST['lokEdit']
        urai = request.POST['uraiEdit']
        MasterLokasi.objects.filter(id=idedit).update(kd_lokasi = kd_lokasi, urai = urai )
        return redirect('SPPD:lokasi')

def hapusLokasi(request, idedit):
    hapus = MasterLokasi.objects.get(id=idedit)

    hapus.delete()
    return redirect('SPPD:lokasi')


def organisasi(request):
    organisasi = MasterOrganisasi.objects.all().order_by('id_organisasi').values()
    contex = {
        'organisasi' : organisasi
    }
    return render(request, 'master/master_organisasi.html',contex)

def addOrganisasi(request):
    if request.method == "POST":
        kode_organisasi = request.POST.get('kd_orgs')
        tahun = request.POST.get('tahun')
        urai = request.POST.get('urai')

        insert = MasterOrganisasi()
        insert.kode_organisasi = kode_organisasi
        insert.urai = urai

        insert.save()

        return redirect('SPPD:organisasi')

def editOrganisasi(request, idedit=""):
    if request.method == "POST":
        kode_organisasi = request.POST['orgsEdit']
        urai = request.POST['uraiEdit']

        MasterOrganisasi.objects.filter(id_organisasi=idedit).update(kode_organisasi = kode_organisasi, urai = urai)

        return redirect('SPPD:organisasi')

def hapusOrganisasi(request, idedit):
    hapus = MasterOrganisasi.objects.get(id_organisasi=idedit)

    hapus.delete()
    return redirect('SPPD:organisasi')


def pegawai(request):
   pegawai = MasterPegawai.objects.all().order_by('nip').values()
   contex = {
        'pegawai' : pegawai
    }
   
   return render(request, 'master/master_pegawai.html',contex)

def addPegawai(request):
    if request.method == "POST":
        nip = request.POST.get('nip')
        nama = request.POST.get('nama')
        golongan = request.POST.get('golongan')
        no_hp = request.POST.get('nohp')
        eselon = request.POST.get('eselon')
        alamat = request.POST.get('alamat')
        pangkat = request.POST.get('pangkat')
        email = request.POST.get('email')
        
        insert = MasterPegawai()
        insert.nip = nip
        insert.nama = nama
        insert.golongan = golongan
        insert.no_hp = no_hp
        insert.eselon = eselon
        insert.alamat = alamat
        insert.pangkat = pangkat
        insert.email = email

        insert.save()

        return redirect('SPPD:pegawai')
    
def editPegawai(request, idedit=""):
    if request.method == "POST":
        nip = request.POST.get('nip')
        nama = request.POST.get('nama')
        golongan = request.POST.get('golongan')
        no_hp = request.POST.get('nohp')
        eselon = request.POST.get('eselon')
        alamat = request.POST.get('alamat')
        pangkat = request.POST.get('pangkat')
        email = request.POST.get('email')

        MasterPegawai.objects.filter(nip=idedit).update(nip = nip, nama = nama, golongan = golongan, no_hp = no_hp, eselon = eselon, alamat = alamat, pangkat = pangkat, email = email)

        return redirect('SPPD:pegawai')
    
def hapusPegawai(request, idedit):
    hapus = MasterPegawai.objects.get(nip=idedit)

    hapus.delete()
    return redirect('SPPD:pegawai')

def pengesah(request):
    return render(request, 'master/master_pengesah.html')

def ssh(request):
    return render(request, 'master/master_ssh.html')

def tahun(request):
    tahun = MasterTahun.objects.all().order_by('id').values()
    contex = {
        'tahun' : tahun
    }
    return render(request, 'master/master_tahun.html', contex)

def addTahun(request):
    if request.method == "POST":
        tahun = request.POST.get('tahun')
        status = request.POST.get('status')

        insert = MasterTahun()
        insert.tahun = tahun
        insert.status = status

        insert.save()

        return redirect('SPPD:tahun')

def editTahun(request, idedit=""):
    if request.method == "POST":
        tahun = request.POST['thnEdit']
        status = request.POST['statusEdit']

        MasterTahun.objects.filter(id=idedit).update(tahun = tahun, status = status)

        return redirect('SPPD:tahun')

def hapusTahun(request, idedit):
    hapus = MasterTahun.objects.get(id=idedit)

    hapus.delete()
    return redirect('SPPD:tahun')

def loginUser(request):

    if request.method == 'GET':
        contex = {
            'title' : 'Login'
        }   
        return render(request, 'auth/login.html', contex)
    if request.method == 'POST':

        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('SPPD:dash')
        else:
            return redirect('SPPD:login')


def addUser(request):
    contex = {
        'title' : 'Add User'
    }

    if request.method == "POST":
        nama = request.POST.get('nama')
        email = request.POST.get('email')
        password = request.POST.get('password')

        insert = UserNew()
        insert.email = email
        insert.nama = nama
        insert.set_password(password)
        insert.save()

        return redirect('SPPD:login')

    return render(request, 'auth/addUser.html', contex)