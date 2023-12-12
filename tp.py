class VotreClasseAutomate:
    def __init__(self):
        self.S = set()
        self.X = set()
        self.I = {}
        self.F = set()

    def add_instruction(self, Si, w, Sj):
        assert Si in self.S
        assert Sj in self.S
        assert all(map(lambda char: char in self.X, w))
        
        if self.I.get(Si, None):
            if self.I[Si].get(w, None):
                self.I[Si][w].add(Sj)
            else:
                self.I[Si][w] = {Sj}
        else:
            self.I[Si] = {w: {Sj}}

    def delete_instruction(self, Si, w, Sj):
        assert Si in self.S
        assert Sj in self.S
        assert all(map(lambda char: char in self.X, w))

        if self.I.get(Si, None):
            if self.I[Si].get(w, None):
                self.I[Si][w].remove(Sj)
                if not self.I[Si][w]:
                    del self.I[Si][w]
                    if not self.I[Si]:
                        del self.I[Si]

    def add_final_state(self, state):
        self.F.add(state)

    # Méthode eliminate_empty_words ici...
    

    def eliminate_empty_words(self):
        empty_symbol = ""  # Symbole vide à éliminer

        transitions_to_delete = []  # Transitions à supprimer
        transitions_to_add = []     # Nouvelles transitions à ajouter
        states_to_update_final = set()  # États à mettre à jour comme finaux

        for Si in self.S:
            for w in self.I.get(Si, {}):
                if w == empty_symbol:
                    for Sj in self.I[Si][w]:
                        transitions_to_delete.append((Si, w, Sj))  # Ajout des transitions à supprimer
                        for symbol in self.X:
                            if symbol != empty_symbol and self.I.get(Sj, {}).get(symbol, None) :
                                transitions_to_add.append((Si, symbol, Sj))  # Ajout des nouvelles transitions

                        if Sj in self.F:  # Vérification pour mettre à jour l'état final
                            states_to_update_final.add(Si)

        # Suppression des transitions contenant des symboles vides
        for transition in transitions_to_delete:
            Si, w, Sj = transition
            self.delete_instruction(Si, w, Sj)

        # Ajout des nouvelles transitions
        for transition in transitions_to_add:
            Si, symbol, Sj = transition
            self.add_instruction(Si, symbol, Sj)

        # Mise à jour des états finaux
        for state in states_to_update_final:
            self.add_final_state(state)


# Création d'une instance de VotreClasseAutomate
automate = VotreClasseAutomate()

# Ajout d'états, de transitions, etc. (adapter cela selon votre structure d'automate)
automate.S = {'S1', 'S2', 'S3'}
automate.X = {'a', 'b', 'c'}
automate.add_instruction('S1', "", 'S2')
automate.add_instruction('S2', 'a', 'S3')
automate.add_instruction('S2', 'b', 'S3')
automate.add_instruction('S1', "", 'S3')
automate.add_final_state('S3')

# Affichage de l'automate avant la transformation
print("Automate avant transformation:")
print("États:", automate.S)
print("Transitions:", automate.I)
print("États finaux:", automate.F)

# Appel de la méthode eliminate_empty_words
automate.eliminate_empty_words()

# Affichage de l'automate après la transformation
print("\nAutomate après transformation:")
print("États:", automate.S)
print("Transitions:", automate.I)
print("États finaux:", automate.F)
