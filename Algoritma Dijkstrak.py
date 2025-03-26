import tkinter as tk
from tkinter import ttk
import heapq

def dijkstra(graph, start, end):
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]
    shortest_path = {node: None for node in graph}

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_node == end:
            break

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                shortest_path[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    path = []
    current_node = end
    while current_node is not None:
        path.append(current_node)
        current_node = shortest_path[current_node]
    path = path[::-1]  # Membalik urutan lintasan
    return distances[end], path
graph = {
'G1': {'G2': 700, 'G16': 750,'G19':550},
'G2': {'G3': 550, 'G1':700},
'G3': {'G4': 130,'G19':700,'G2': 550},
'G4': {'G5': 1000,'G3': 130},
'G5': {'G6': 2000,'G22':1050,'G4':1000},
'G6': {'G7': 700, 'G5': 2000},
'G7': {'G8': 700, 'G24': 850, 'G6': 700},
'G8': {'G9': 260, 'G25': 250, 'G7':700},
'G9': {'G10': 500, 'G28': 450, 'G8': 260},
'G10': {'G11': 750, 'G9': 500},
'G11': {'G12': 450, 'G28': 500, 'G29': 500, 'G10':750},
'G12': {'G13': 250, 'G11':450},
'G13': {'G14': 400, 'G30': 600, 'G32': 300, 'G12':250},
'G14': {'G15': 700, 'G35': 100, 'G13': 400},
'G15': {'G35': 350, 'G36': 800, 'G14': 700},
'G16': {'G17': 550, 'G1': 750},
'G17': {'G20': 1000, 'G18': 400, 'G16': 550},
'G18': {'G17': 400, 'G19': 350, 'G22': 1000},
'G19': {'G3': 700, 'G1': 550, 'G18': 350},
'G20': {'G21': 500, 'G22': 400, 'G17': 1000},
'G21': {'G20': 500, 'G23': 400, 'G26': 1100},
'G22': {'G5': 1050, 'G24': 2000,'G18':1000,'G20': 400},
'G23': {'G24': 350, 'G27': 800, 'G21': 400},
'G24': {'G7': 850, 'G25': 250, 'G28': 800,'G23':350,'G22':2000},
'G25': {'G24': 250, 'G8': 250},
'G26': {'G27': 200, 'G21': 1100},
'G27': {'G26': 200, 'G28': 600, 'G29': 600,'G23':800},
'G28': {'G9': 450, 'G11': 500, 'G27': 600,'G24':800},
'G29': {'G11': 500, 'G30': 50, 'G27': 600},
'G30': {'G13': 600, 'G31': 450, 'G29': 50},
'G31': {'G33': 300, 'G32': 250, 'G30': 450},
'G32': {'G13': 300, 'G34': 300, 'G31': 250},
'G33': {'G36': 450, 'G34': 350, 'G31': 300},
'G34': {'G33': 350, 'G35': 50, 'G32': 300},
'G35': {'G14': 100, 'G15': 350, 'G34':50},
'G36': {'G15':800, 'G33':450},
}
# Nama titik
node_names = {
'G1': 'Persimpangan Jl. Ketaren (UNIMED)',
'G2': 'Persimpangan rumah sakit haji',
'G3': 'Persimpangan Jl. Willem Iskandar no. 20',
'G4': 'Persimpangan Jl. Tuasan 194-198',
'G5': 'Persimpangan Jl. Tempuling',
'G6': 'Persimpangan Jl. Gunung Krakatau',
'G7': 'Persimpangan Jl. KH. Syeikh Abdul Wahab Rokan 41-43',
'G8': 'Persimpangan Jl. KL. Yos Sudarso 50-51',
'G9': 'Persimpangan Jl. KL. Yos Sudarso 24',
'G10': 'Persimpangan Adipura Monumen',
'G11': 'Persimpangan Jl.Sikambing',
'G12': 'Persimpangan Jl. Damar',
'G13': 'Persimpangan Jl. Sekip ',
'G14': 'Persimpangan Jl. Pabrik Tenun',
'G15': 'Kampus Universitas Prima Indonesia',
'G16': 'Persimpangan Jl.Letda Sujono',
'G17': 'Persimpangan Jl. Pancing No.209',
'G18': 'Persimpang Jl. Perjuangan',
'G19': 'Persimpangan Jl.William Iskandar ps. V',
'G20': 'Simpang Empat Lampu Merah Aksara',
'G21': 'Persimpangan Jl. Rakyat No.46',
'G22': 'Persimpangan Jl. Sutomo Ujung no. 28 d',
'G23': 'Persimpangan Jl. Pelita IV',
'G24': 'Persimpangan Jl. Hm. Said',
'G25': 'Persimpangan jalan Sutomo Ujung no. 183-199',
'G26': 'Persimpangan Jl. HM. Said no. 88',
'G27': 'Persimpangan Jl. Sutomo no. 30',
'G28': 'Persimpangan Jl. KH. Syeikh Abdul Wahab Rokan No.12',
'G29': 'Persimpangan  Jl. KL. Yos Sudarso 50-51',
'G30': 'Persimpangan Adipura Monumen',
'G31': 'Persimpangan Jl. KL. Yos Sudarso 24',
'G32': 'Persimpangan Jl.Sikambing',
'G33': 'Persimpangan Jl. Damar',
'G34': 'Persimpangan Jl. Rantang',
'G35': 'Persimpangan Jl. Gelas',
'G36': 'Persimpangan Jl Ayahanda',
}
# Fungsi untuk menghitung jalur terpendek
def calculate():
    start = start_entry.get()
    end = end_entry.get()
    
    if start not in graph or end not in graph:
        result_var.set("Titik awal atau titik tujuan tidak valid.")
        return
    
    distance, path = dijkstra(graph, start, end)
    path_text = '-'.join(path)
    named_path = [node_names[node] for node in path]
    named_path_text = '\n'.join([f"{i+1}. {name}" for i, name in enumerate(named_path)])
    result_var.set(f"JARAK: {distance} meter\nLINTASAN: {path_text}\n\nNama Jalan:\n" + named_path_text)

# Membuat window Tkinter
root = tk.Tk()
root.title("Algoritma Dijkstra")
root.geometry("400x400")

# Membuat frame utama
mainframe = ttk.Frame(root, padding="10 10 10 10")
mainframe.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Label dan entry untuk titik awal
start_label = ttk.Label(mainframe, text="START (TITIK AWAL):")
start_label.grid(column=1, row=1, sticky=tk.W)
start_entry = ttk.Entry(mainframe, width=15)
start_entry.grid(column=2, row=1, sticky=(tk.W, tk.E))

# Label dan entry untuk titik tujuan
end_label = ttk.Label(mainframe, text="DESTINASI (TITIK TUJUAN):")
end_label.grid(column=1, row=2, sticky=tk.W)
end_entry = ttk.Entry(mainframe, width=15)
end_entry.grid(column=2, row=2, sticky=(tk.W, tk.E))

# Tombol untuk menghitung jalur
calculate_button = ttk.Button(mainframe, text="Hitung", command=calculate)
calculate_button.grid(column=2, row=3, sticky=tk.W)

# Label untuk menampilkan hasil
result_var = tk.StringVar()
result_label = ttk.Label(mainframe, textvariable=result_var, wraplength=350, justify=tk.LEFT)
result_label.grid(column=1, row=4, columnspan=2, sticky=(tk.W, tk.E))

# Padding untuk semua child dalam frame utama
for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

# Fokus pada entry titik awal
start_entry.focus()

# Mengikat tombol 'Return' (Enter) ke fungsi hitung
root.bind('<Return>', lambda event: calculate())

# Menjalankan aplikasi
root.mainloop()