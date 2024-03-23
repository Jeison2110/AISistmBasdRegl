"""
Creado por:
    IdBanner:100098659
    Nombre: Esperanza Castro Lombana 

    IdBanner:100096167
    Nombre: Jeison Valencia Sanchez

    Fecha: 2024-03-20,  ©/ todos los derechos reservados
    Corporación Universitaria Iberoamericana

    Escribir en Python las instrucciones para el desarrollo de un sistema inteligente que a partir de una base de
    conocimiento escrito en reglas lógicas, desarrolle la mejor ruta para moverse desde un punto A y un punto B en 
    el sistema de transporte masivo local.
"""

# Bibliotecas utilizadas
import networkx as nx # Manejo de grafos
import matplotlib.pyplot as plt # Graficas

# Creamos el grafo que contendra el diccionario de base de conocimientos logicas y reglas de distancia
G = nx.DiGraph()

# Agregamos los nodos a modo de estaciones 
G.add_node('Bello')
G.add_node('Madera')
G.add_node('Centromed')
G.add_node('Poblado')
G.add_node('Itagui')
G.add_node('Sabaneta')
G.add_node('Estrella')

# Agregamos las relaciones que contendran las logicas y reglas de las distancias entre las estaciones del transporte
G.add_edge('Bello', 'Madera', weight=5, Costo=1600, TiempoViaje=18, TipoTransporte="Bus")
G.add_edge('Madera', 'Bello', weight=5, Costo=1600, TiempoViaje=18, TipoTransporte="Bus")

G.add_edge('Bello', 'Centromed', weight=10, Costo=2100, TiempoViaje=28, TipoTransporte="Bus")
G.add_edge('Centromed', 'Bello', weight=10, Costo=2100, TiempoViaje=28, TipoTransporte="Bus")

G.add_edge('Madera', 'Centromed', weight=3, Costo=1500, TiempoViaje=15, TipoTransporte="Bus")
G.add_edge('Centromed', 'Madera', weight=3, Costo=1500, TiempoViaje=15, TipoTransporte="Bus")

G.add_edge('Madera', 'Poblado', weight=15, Costo=3000, TiempoViaje=40, TipoTransporte="Bus")
G.add_edge('Poblado', 'Madera', weight=15, Costo=3000, TiempoViaje=40, TipoTransporte="Bus")

G.add_edge('Centromed', 'Itagui', weight=8, Costo=1900, TiempoViaje=25, TipoTransporte="Bus")
G.add_edge('Itagui', 'Centromed', weight=8, Costo=1900, TiempoViaje=25, TipoTransporte="Bus")

G.add_edge('Centromed', 'Sabaneta', weight=11, Costo=2300, TiempoViaje=30, TipoTransporte="Bus")
G.add_edge('Sabaneta', 'Centromed', weight=11, Costo=2300, TiempoViaje=30, TipoTransporte="Bus")

G.add_edge('Centromed', 'Estrella', weight=14, Costo=2600, TiempoViaje=35, TipoTransporte="Bus")
G.add_edge('Estrella', 'Centromed', weight=14, Costo=2600, TiempoViaje=35, TipoTransporte="Bus")

G.add_edge('Poblado', 'Itagui', weight=6, Costo=1700, TiempoViaje=22, TipoTransporte="Bus")
G.add_edge('Itagui', 'Poblado', weight=6, Costo=1700, TiempoViaje=22, TipoTransporte="Bus")

G.add_edge('Poblado', 'Sabaneta', weight=9, Costo=2000, TiempoViaje=27, TipoTransporte="Bus")
G.add_edge('Sabaneta', 'Poblado', weight=9, Costo=2000, TiempoViaje=27, TipoTransporte="Bus")

G.add_edge('Itagui', 'Sabaneta', weight=5, Costo=1600, TiempoViaje=18, TipoTransporte="Bus")
G.add_edge('Sabaneta', 'Itagui', weight=5, Costo=1600, TiempoViaje=18, TipoTransporte="Bus")

G.add_edge('Sabaneta', 'Estrella', weight=3, Costo=1500, TiempoViaje=15, TipoTransporte="Bus")
G.add_edge('Estrella', 'Sabaneta', weight=3, Costo=1500, TiempoViaje=15, TipoTransporte="Bus")


# Le mostramos al usuario las estaciones disponibles del transporte masivo
print("""--==========Bienvenido Al Transporte Masivo BUSMED==========--
Actual mentes el transporte cuenta con las siguientes estaciones:""")
for Estaciones in G.nodes:
    print(f"Estacione: {Estaciones}")


print("\n")
# Validamos que el usuario ingrese las estaciones de origen y fin correctamente
while True:    
    EstacionA = str(input("Ingrese la estacion de inicio: "))
    EstacionB = str(input("Ingrese la estacion final: "))

    EstacionInicio = EstacionA.title().lstrip().rstrip()
    EstacionFinal = EstacionB.title().lstrip().rstrip()

    if EstacionInicio not in G.nodes():
        print ("La estacion de inicio no corresponde con una estacion valida del sistema BUSMED")  
    elif EstacionFinal not in G.nodes():
        print ("La estacion de destino no corresponde con una estacion valida del sistema BUSMED")            
    else:
        break


# Agregamos las etiquetas de las aristas con sus distnaicas 
Etiquetas = {(u, v): G[u][v]['weight'] for u, v in G.edges()}


# Creamos el grafico utilizando biblioteca de nx
pos = nx.spring_layout(G)


# Uitlizamos el algoritmo de dijkstra para encontrar el camino mas corto
Ruta = nx.dijkstra_path(G, EstacionInicio, EstacionFinal)


# Imprimimos las estaciones de parada con cada uno se sus atributos y adicional el total del recorrido
print("\n")
DistanciaTotal = 0
CostoTotal = 0
TiempoViajeTotal = 0
print(f"""El camino mas corto desde la estacion: "{EstacionInicio}" hasta la estacion: "{EstacionFinal}" es: """)
for i, Parada in enumerate(Ruta):
    print(f"""Estacion: "{Parada}" """)
    if i < len(Ruta) - 1:
        SiguienteParada = Ruta[i+1]
        print(f" - Distancia: {G[Parada][SiguienteParada]['weight']} km")
        print(f" - Costo: ${G[Parada][SiguienteParada]['Costo']}")
        print(f" - Tiempo de viaje: {G[Parada][SiguienteParada]['TiempoViaje']} Minutos")
        print(f" - Tipo de transporte: {G[Parada][SiguienteParada]['TipoTransporte']}")

        DistanciaTotal += G[Parada][SiguienteParada]['weight']
        CostoTotal += G[Parada][SiguienteParada]['Costo']
        TiempoViajeTotal += G[Parada][SiguienteParada]['TiempoViaje']



print(f"""Desde:"{EstacionInicio}" hasta:"{EstacionFinal}"\nLa distancia total del viaje es: {DistanciaTotal}Km, con un costo total de:${CostoTotal} y un tiempo de viaje de {TiempoViajeTotal} Minutos""") 
print("Gracias por utilizar nuestro sistema.")


# Resaltamos en el grafico el camino mas carto encontrado por el algoritmo de dijkstra
EtiquetasRutas = [(Ruta[i], Ruta[i+1]) for i in range(len(Ruta)-1)]
nx.draw_networkx_edges(G, pos, edgelist = EtiquetasRutas, width = 3, edge_color='Red')


# Mostramos en el grafico los nodos (Estaciones) y  las aristas (Distancias)
nx.draw_networkx_nodes(G, pos)
nx.draw_networkx_edges(G, pos)
nx.draw_networkx_edge_labels(G, pos, edge_labels=Etiquetas)


# Agregamos etiquetas a los nodos (Estaciones)
nx.draw_networkx_labels(G, pos)


# Mostramos en pantalla el grafico
plt.title(f"""Grafo para el camino mas corto entre las estaciones de:\n"{EstacionInicio}" y "{EstacionFinal}" """)
plt.show()
