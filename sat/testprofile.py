from axioms import *
from config import *
from explain import *
from literals import *
from properties import *
from utils import *




if __name__ == "__main__":
    graphs = generate_graph_subsets([cnfIrreflexivity, cnfTransitivity, cnfCompleteness])
    config.update_graphs(graphs)

    match = 0
    mismatch = 0
    duplicates = 0

    all_profiles = []

    for E in allProfiles():
        E_dec = profileIntToProfile(E)
        E_rec = profileToProfileInt(E_dec)

        if E == E_rec:
            match += 1
        else:
            mismatch += 1
            print(E, "\n\n", E_rec)

        if E_dec in all_profiles:
            duplicates += 1
        all_profiles.append(E_dec)



    print(f"{match} MATCHES, {mismatch} MISMATCHES")
    print(f"{duplicates} DECODED DUPLICATES")