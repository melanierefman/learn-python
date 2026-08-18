# Apliksai todo list sederhana menggunakan python
# manfaatkan list untuk menyimpan, mengubah, dan menghapus data

def tambah_todo(todo_list, todo):
    todo_list.append(todo)
    print(f'Todo "{todo}" berhasil ditambahkan.')
    
def hapus_todo(todo_list, todo):
    if todo in todo_list:
        todo_list.remove(todo)
        print(f'Todo "{todo}" berhasil dihapus.')
    else:
        print(f'Todo "{todo}" tidak ditemukan.')
        
def ubah_todo(todo_list, old_todo, new_todo):
    if old_todo in todo_list:
        index = todo_list.index(old_todo)
        todo_list[index] = new_todo
        print(f'Todo "{old_todo}" berhasil diubah menjadi "{new_todo}".')
    else:
        print(f'Todo "{old_todo}" tidak ditemukan.')

def tampilkan_todo(todo_list):
    if todo_list:
        print("Daftar Todo:")
        for index, todo in enumerate(todo_list, start=1):
            print(f"{index}. {todo}")
    else:
        print("Tidak ada todo yang tersimpan.")
        
if __name__ == "__main__":
    todo_list = []
    
    while True:
        print("\nMenu:")
        print("1. Tambah Todo")
        print("2. Hapus Todo")
        print("3. Ubah Todo")
        print("4. Tampilkan Todo")
        print("5. Keluar")
        
        pilihan = input("Pilih menu (1-5): ")
        
        if pilihan == "1":
            todo = input("Masukkan todo: ")
            tambah_todo(todo_list, todo)
        elif pilihan == "2":
            todo = input("Masukkan todo yang ingin dihapus: ")
            hapus_todo(todo_list, todo)
        elif pilihan == "3":
            old_todo = input("Masukkan todo yang ingin diubah: ")
            new_todo = input("Masukkan todo baru: ")
            ubah_todo(todo_list, old_todo, new_todo)
        elif pilihan == "4":
            tampilkan_todo(todo_list)
        elif pilihan == "5":
            print("Terima kasih telah menggunakan aplikasi todo list.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")