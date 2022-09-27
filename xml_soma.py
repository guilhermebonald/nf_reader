import untangle
import os
from time import sleep

# directory files

files_set = os.listdir()

# list 

values = []

for arquivo in files_set:
    if '.xml' in arquivo:
        # xml parse file
        xml_file = untangle.parse(arquivo)
        # path
        total_path = xml_file.nfeProc.NFe.infNFe.total.ICMSTot
        # tag value
        nf_value = float(total_path.vNF.cdata)
        values.append(nf_value)


print(f"--- Notas somadas: {len(values)} ---\n--- Total: R${sum(values)} ---")
sleep(60)