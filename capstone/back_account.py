# Sistem Bank Account sederhana menggunakan OOP
# Minimal fitur: cek saldo, tarik saldo, setor saldo

# class untuk buat object
class BankAccount:
    # constructor untuk inisialisasi object
    def __init__(self, account_number, account_holder, initial_balance=0):
        # atribut untuk menyimpan data akun
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = initial_balance

    # method untuk cek saldo
    def cek_saldo(self):
        print(f"Saldo saat ini: Rp {self.balance}") # encapsulation, data balance tidak bisa diakses langsung dari luar class

    def tarik_saldo(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Berhasil menarik Rp {amount}. Saldo baru: Rp {self.balance}")
        else:
            print("Saldo tidak mencukupi.")

    def setor_saldo(self, amount):
        self.balance += amount
        print(f"Berhasil menyetor Rp {amount}. Saldo baru: Rp {self.balance}")

if __name__ == "__main__":
    account = BankAccount("123456789", "John Doe", 100000) #ini objectnya
    
    while True:
        print("\nMenu:")
        print("1. Cek Saldo")
        print("2. Tarik Saldo")
        print("3. Setor Saldo")
        print("4. Keluar")
        
        pilihan = input("Pilih menu (1-4): ")
        
        if pilihan == "1":
            account.cek_saldo()
        elif pilihan == "2":
            amount = float(input("Masukkan jumlah yang ingin ditarik: "))
            account.tarik_saldo(amount)
        elif pilihan == "3":
            amount = float(input("Masukkan jumlah yang ingin disetor: "))
            account.setor_saldo(amount)
        elif pilihan == "4":
            print("Terima kasih telah menggunakan sistem bank account.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")