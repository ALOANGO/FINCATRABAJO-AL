# -*- coding: utf-8 -*-
"""metrocuadrado.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1joWjZwRMSxZ1d9ejte90oC7wypwMm7oS
"""

import requests
import pandas as pd

def metrocuadrado (cities):

              def metrocuadrado_scrap(ciudad):

                        # URL de la solicitud
                        url = f"https://www.metrocuadrado.com/rest-search/search?realEstateBusinessList=venta&city={ciudad}&realEstateTypeList=apartamento,casa&from=0&size=50"
                        headers={'X-Api-Key': 'P1MfFHfQMOtL16Zpg36NcntJYCLFm8FqFfudnavl'}
                        r=requests.get(url, headers=headers)


                        datacruda=r.json()["results"]

                        area=[]
                        cuartos=[]
                        titulo=[]
                        oferta=[]
                        garajes=[]
                        tocadores=[]
                        precio=[]
                        vlradmin=[]
                        vlrarriendo=[]
                        tipoinmueble=[]
                        nombrecontructor=[]
                        nombreproyecto=[]
                        barrio=[]
                        comuna=[]
                        ciudad=[]
                        zona=[]
                        propid=[]
                        contactnumber=[]
                        estadoinmueble=[]
                        idempresa=[]
                        descripcion=[]
                        link=[]


                        for e in datacruda:
                          try:
                              area.append(e.get('marea',None))
                              cuartos.append(e['mnrocuartos'])
                              titulo.append(e['title'])
                              oferta.append(e['mtiponegocio'])
                              garajes.append(e['mnrogarajes'])
                              tocadores.append(e['mnrobanos'])
                              precio.append(e['mvalorventa'])
                              vlradmin.append(e.get('data', {}).get('mvaloradministracion', None))

                              vlrarriendo.append(e['mvalorarriendo'])
                              tipoinmueble.append(e['mtipoinmueble']['nombre'])
                              nombrecontructor.append(e['mnombreconstructor'])
                              nombreproyecto.append(e['mnombreproyecto'])
                              barrio.append(e['mbarrio'])
                              comuna.append(e['mnombrecomunbarrio'])
                              ciudad.append(e['mciudad']['nombre'])
                              propid.append(e['midinmueble'])
                              contactnumber.append(e['contactPhone'])
                              estadoinmueble.append(e['mestadoinmueble'])
                              idempresa.append(e['midempresa'])
                              descripcion.append(e['data']['murldetalle'])
                              link.append(e['data']['murldetalle'])
                              zona.append(e['mzona']['nombre'])

                          except:
                              zona.append("null")




                        df={'area':area,
                            'cuartos':cuartos,
                            'titulo':titulo,
                            'oferta':oferta,
                            'garajes':garajes,
                            'tocadores':tocadores,
                            'precio':precio,
                            'vlradmin':vlradmin,
                            'vlrarriendo':vlrarriendo,
                            'tipoinmueble':tipoinmueble,
                            'nombrecontructor':nombrecontructor,
                            'nombreproyecto':nombreproyecto,
                            'barrio':barrio,
                            'comuna':comuna,
                            'ciudad':ciudad,
                            'zona':zona,
                            'propid':propid,
                            'contactnumber':contactnumber,
                            'estadoinmueble':estadoinmueble,
                            'idempresa':idempresa,
                            'descripcion':descripcion,
                            'link':link}

                        dfconsolidado=pd.DataFrame(df)

                        #Organizar columna de link
                        dfconsolidado["link"]="https://www.metrocuadrado.com"+dfconsolidado.descripcion

                        return dfconsolidado

              dfs=[]

              for c in cities:
                try:
                 dfs.append(metrocuadrado_scrap(c))
                except:
                  continue


             #Concatenar tablas extraidas
              dfdefinit=pd.concat(dfs, ignore_index=True)


              #eliminar duplicados de columna propid
              dfdefinit.drop_duplicates(['propid'], inplace=True)
              dfdefinit.reset_index(drop=True, inplace=True)

              return dfdefinit

cities=["Medellin",	"Bello","Itagui",	"Envigado",	"Sabaneta",	"Estrella",	"Caldas",	"Copacabana",	"Girardota",	"Barbosa",	"Rionegro",	"Viboral",	"Retiro",	"Ceja",	"Marinilla",	"Penol",	"Guatape",	"Vicente",	"union",	"Guarne",	"Cocorna",	"Apartado",	"Turbo",	"Carepa",	"Chigorodo",	"Necocli",	"Arboletes",]
datametrocuadrado=metrocuadrado(cities)

datametrocuadrado.to_csv("metroc2.csv", index=False)