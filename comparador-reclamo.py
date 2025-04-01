import pandas as pd

sigma_reclamo=pd.read_xml("C:\\Users\\12078794\\Documents\\SIGMA\\Reclamo\\reclamo SIGMA.xml")
reclamo_banco=pd.read_xml("C:\\Users\\12078794\\Documents\\SIGMA\\Reclamo\\reclamo-banco.xml")

print(sigma_reclamo.__len__())
print(reclamo_banco.__len__())

print("-------------------------------------------")

identificadores_sigma= sigma_reclamo.get("numero_identificador")
identificadores_banco=reclamo_banco.get("numero_identificador")
print(identificadores_sigma.__len__())
print(identificadores_banco.__len__())
print(set(identificadores_banco.tolist())-set(identificadores_sigma.tolist()))      
