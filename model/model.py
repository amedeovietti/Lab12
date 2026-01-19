import networkx as nx
from database.dao import DAO

class Model:
    def __init__(self):
        """Definire le strutture dati utili"""
        self.G = nx.Graph()



    def build_weighted_graph(self, year: int):
        """
        Costruisce il grafo pesato dei rifugi considerando solo le connessioni con campo `anno` <= year passato
        come argomento.
        Il peso del grafo è dato dal prodotto "distanza * fattore_difficolta"
        """
        connessioni = DAO.leggiConnessioni(year)        # [{'id_rifugio1': 1, 'id_rifugio2': 2}, {'id_rifugio1': 1, 'id_rifugio2': 3}, ...]
        for d in connessioni:
            peso = DAO.trovaPeso(d)
            self.G.add_edge(d["id_rifugio1"], d["id_rifugio2"], weight = peso)


    def get_edges_weight_min_max(self):
        """
        Restituisce min e max peso degli archi nel grafo
        :return: il peso minimo degli archi nel grafo
        :return: il peso massimo degli archi nel grafo
        """
        M = 0
        m = 1000
        for n1,n2,weight in self.G.edges(data=True):            # weight è un dizionario di attributi {'weight': 7}
            if weight['weight'] > M:
                M = weight['weight']
        for n1,n2,weight in self.G.edges(data=True):
            if weight['weight'] < m:
                m = weight['weight']
        return m, M


    def count_edges_by_threshold(self, soglia):
        """
        Conta il numero di archi con peso < soglia e > soglia
        :param soglia: soglia da considerare nel conteggio degli archi
        :return minori: archi con peso < soglia
        :return maggiori: archi con peso > soglia
        """
        m_count = 0
        M_count = 0
        for n1,n2,weight in self.G.edges(data=True):            # weight è un dizionario di attributi {'weight': 7}
            if weight['weight'] > soglia:
                M_count += 1
        for n1,n2,weight in self.G.edges(data=True):
            if weight['weight'] < soglia:
                m_count += 1
        return m_count, M_count


    """Implementare la parte di ricerca del cammino minimo"""
    # TODO
