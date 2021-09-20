import pandas as pd
from config.configuration import engine
import ast

def Autores():
    """
    Calls the database in MySQl and returns all the authors in a json format.
    """
    query = f"""
    SELECT nombre FROM Autor
    """
    datos = pd.read_sql_query(query,engine)
    return datos.to_json(orient="records")


def Frases():
    """
    Calls the database in MySQl and returns all the phrases in a json format.
    """
    query= f"""
    SELECT Frase FROM Frases
    """
    datos = pd.read_sql_query(query,engine)
    return datos.to_json(orient="records")

def Campo():
    """
    Calls the database in MySQl and returns the different areas where the authors 
    moved in.
    """
    query = f"""
    SELECT Campo FROM Campo;
    """
    datos = pd.read_sql_query(query,engine)
    return datos.to_json(orient='records')


def frase_Autor(name):
    """
    You can put the name of the author you want and this returns his name, the area
    where he moves in, the year he was born and his phrases.
    """
    query = f"""
    SELECT nombre, año_nacimiento, Frases.Frase, Campo.Campo
    FROM Autor
    INNER JOIN Frases ON Autor_idAuthor= idAuthor
    INNER JOIN Campo ON idCampo = Campo_idCampo 
    WHERE nombre = '{name}'
    """
    datos = pd.read_sql_query(query,engine)
    return datos.to_json(orient="records")

def limpia(algo):
    """
    This function takes away the repeated things of the dictionary and returns a dictionary
    with a unique name, the unique area, and the year when the author was born and all his phrases
     """
    algo = ast.literal_eval(algo)
    dic={}
    dic['Frase']=[]
    for x in algo:
        dic['nombre']=x['nombre']
        dic['año_nacimiento']=x['año_nacimiento']
        dic['Campo']=x['Campo']
        dic['Frase'].append(x['Frase'])
    return dic

def A_C():
    """
    This function gives all the imformation about the authors that were boen before the year 0.
    """
    query = f"""
    SELECT nombre, año_nacimiento, Frases.Frase, Campo.Campo
    FROM Autor
    INNER JOIN Frases ON Autor_idAuthor= idAuthor
    INNER JOIN Campo ON idCampo = Campo_idCampo
    WHERE año_nacimiento LIKE '%%c'
    """
    datos = pd.read_sql_query(query,engine)
    return datos.to_json(orient="records")


def check(tabla,string):
    """
    Function tha verifies if a table has certain strings. It checks if the Autor exists, if the Campo exits,
    and if the phrase exists.
    """
    if tabla == "Autor":
        query = list(engine.execute(f"SELECT nombre FROM Autor WHERE nombre = '{string}'"))
        if len(query) > 0:
            return True
        else:
            return False
        
    elif tabla == "Campo":
        query = list(engine.execute(f"SELECT Campo FROM Campo WHERE Campo = '{string}'"))
        if len(query) > 0:
            return True
        else:
            return False
    
    elif tabla == "Frases":
        query = list(engine.execute(f"SELECT Frase FROM Frases WHERE Frase = '{string}'"))
        if len(query) > 0:
            return True
        else:
            return False

def insertar_Campo(string):
    """
    Calls the check function to see if the Campo exists, if the Campo exists
    it returns este campo ya existe and if it doesn´t, it inserts the new Campo.
    """
    if check("Campo", string):
        return "Este campo ya existe"
    else:
        engine.execute(f"INSERT INTO Campo (Campo) VALUES ('{string}');")

def insertar_datos_autor1(nombre, año_nacimiento,Campo ):
    """
    Calls the function check to see if the Autor, allready exists, if it doesn´t,
    it adds his new name and the year he was born in.
     """

    if check("Campo", Campo): 
        if check("Autor", nombre):
            return "el autor existe"
        else:
            query = list(engine.execute(f"SELECT  idCampo FROM Campo WHERE Campo = '{Campo}'"))
            e = query[0][0]
            engine.execute(f"INSERT INTO Autor (nombre,año_nacimiento, Campo_idCampo) VALUES ('{nombre}', '{año_nacimiento}', '{e}');")
    else:
        return "El Campo no existe, meteleo en la función de arriba"


def insertar_frase(nombre, año_nacimiento, Campo, Frase):
    """
    Calls the function check to see if the Frase, allready exists, if it doesn´t,
    it adds his new na and the year he was born in.
     """
    if check("Campo", Campo): 
        if check("Autor", nombre):
            if check("Frases", Frase ):
                return "la frase ya esta en el datbase"
            else:
                query = list(engine.execute(f"SELECT  idAuthor FROM Autor WHERE nombre = '{nombre}'"))
                e = query[0][0]
                engine.execute(f"INSERT INTO Frases (Frase, Autor_idAuthor) VALUES ('{Frase}', '{e}');")
    