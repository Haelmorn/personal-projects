from Bio import Phylo
from io import StringIO
import re



trees = "(Acanthis_chinensis,((((((((((((Aegypius_yeltoniensis,(((((Emberiza_karelini,Nyctixalus_colchicus),((Gavia_martensi,Gyps_africanus),Pyrrhocorax_galactonotus)),Triturus_pygargus),Ninox_chamaeleontinus),Lutra_quadrivirgata)),Rhombomys_clypeata),Vormela_multifasciata),Anas_hassanica),Numenius_cenchria),Oxyura_terrestris),(((Bombina_leucophyllata,Leiopython_caucasicus),Lanius_cocincinus),(Pagophila_pholeter,Pelusios_wumuzusume))),Pyrgilauda_aureostriata),(Calotes_fuscus,Lamprolepis_nivalis)),Pituophis_alcinous),(((Ardea_tetrix,(Fuligula_oedicnemus,Hottentotta_madagascariensis)),Limnaeus_ruthveni),((((Capella_cherrug,Hirundo_interiorata),Eulabeia_conicus),Rhombomys_caelebs),Monodon_cianeus))),(((((((Aphonopelma_dexter,((Bombyx_wogura,Ceratophrys_guentheri),(Callipogon_ibera,Gypaetus_lehmanni))),((Chrysemys_aureostriata,Corytophanes_irregularis),((Citharacanthus_compactus,Lagenorhynchus_calvus),(Parnassius_wislizeni,Scaphiophryne_asperum)))),Pleurodeles_scripta),Camptoloma_meles),Uroplatus_turtor),(Motacilla_cinaedus,(Parus_eremita,Phylloscopus_caelebs))),(Falco_auratus,Litoria_mlokosiewiczi))),((((Alaus_adspersus,(Citellus_monacha,Melanocorypha_grossmani)),((Antilope_morinellus,(Epicrates_hemilasius,(Machetes_nivicola,Spalax_brachydactyla))),(((Branta_resinifictrix,(Holodactylus_schneideri,Terpsihone_chrysaetus)),Leiocephalus_rusticolus),Rhabdophis_variabilis))),(((((((((((((((Androctonus_macqueni,Otis_ceterus),(Elaphe_fimbriatus,Pandion_quadriocellata)),((Asthenodipsas_modestus,Plegadis_epops),Scorpio_catenifer)),Buteo_pallidus),Aythya_davidiana),Falcipennis_equestris),(Aplopeltura_crassidens,(Himantopus_longipennis,Phormictopus_decorus))),Cygnopsis_regius),Balaena_leucostomum),(Eryx_griseus,((Hemitheconyx_glacialis,Mareca_climacophora),Nemachilus_baeri))),(Anodonta_mehelyi,(Platemys_cherrug,Teratolepis_gecko))),Ardea_mexicana),(Minipterus_iankowskii,Thecla_lehmanni)),Eublepharis_guentheri),Thymallus_ameiva)),Androctonus_indica))"
index = 0
#while index < len(trees):
    #trees[index] = re.sub(r'([A-z])\w+', r'\g<0>:0.1', trees[index])
    #index += 1
#trees = re.sub(r'([A-z])\w+', r'\g<0>:0.1', trees)
handleD = StringIO(trees)
treeD = Phylo.read(handleD, "newick")

print(Phylo.draw_ascii(treeD))
print(treeD.distance("Acanthis_chinensis", "Aegypius_yeltoniensis"))