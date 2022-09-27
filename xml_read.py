import untangle
import os
from time import sleep
import pandas as pd

# directory files

files_set = os.listdir()

empresas = []
nf_n = []
nf_v = []

print("--- Lendo arquivos XML ---")

for arquivo in files_set:
    if ".xml" in arquivo:
        # xml parse file
        xml_file = untangle.parse(arquivo)
        # paths
        ide_path = xml_file.nfeProc.NFe.infNFe.ide
        emit_path = xml_file.nfeProc.NFe.infNFe.emit
        total_path = xml_file.nfeProc.NFe.infNFe.total.ICMSTot
        # tag values
        nf_value = total_path.vNF.cdata
        nf_v.append(float(nf_value))

        nf_number = ide_path.nNF.cdata
        nf_n.append(nf_number)

        nf_name = emit_path.xNome.cdata
        empresas.append(nf_name)

print("--- Criando XLSX ---")
data = {"Empresa": empresas, "N°": nf_n, "Valor": nf_v}

df = pd.DataFrame.from_dict(data=data)
df.to_excel("Relatorio.xlsx")
sleep(2)