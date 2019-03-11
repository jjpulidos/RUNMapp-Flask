from Conn import connection_Mongo
from datetime import datetime
from bson import ObjectId

conn = connection_Mongo()
building_id = {}

cursor = conn["Buildings"].find()
for record in cursor:
    building_id[record["name"]] = ObjectId(record["_id"])

for item in building_id:
    print(item, building_id[item])

# conn["EventsServices"].insert_one({
#    "name ": "Charla «Diplomacia científica: el contexto integral y global acerca del Agua» (Dra. Angélica Gutiérrez-Magness)",
#    "description ": "Conferencista: Dra. Angélica Gutiérrez-Magness, científica de la Administración Nacional Oceánica y Atmosférica (NOAA por sus siglas en inglés) de los Estados Unidos de América y profesora honoraria de la Universidad Nacional de Colombia.",
#    "photo": "link to Google/Drive/Path/Image",
#    "initDate": datetime.now(),
#    "rate":  85 ,
#    "location ": ObjectId(building_id["Edificio Posgrados de Ciencias Humanas"])
# })

#
# conn["EventsServices"].insert_many(
# [
# {
#    "name": "Charla «Diplomacia científica: el contexto integral y global acerca del Agua» (Dra. Angélica Gutiérrez-Magness)",
#    "description": "Conferencista: Dra. Angélica Gutiérrez-Magness, científica de la Administración Nacional Oceánica y Atmosférica (NOAA por sus siglas en inglés) de los Estados Unidos de América y profesora honoraria de la Universidad Nacional de Colombia.",
#    "photo": "link to Google/Drive/Path/Image",
#    "initDate": datetime.today(),
#    "rate":  85.0 ,
#    "location": building_id["Edificio Posgrados de Ciencias Humanas"]
# },{
#    "name": "Gran Debate: Prospectiva del movimiento estudiantil",
#    "description": "Extendemos la siguiente invitación de la Facultad de Ciencias Económicas",
#    "photo": "link to Google/Drive/Path/Image",
#    "initDate": datetime.today(),
#    "rate":  66.0 ,
#    "location": building_id["Edificio de Ciencias Económicas"]
# }, {
#    "name": "Congreso Internacional en Inteligencia Artificial",
#    "description": "El Departamento de Ingeniería de Sistemas con apoyo de  los grupos de Investigación ALIFE y MIDAS están organizando el Congreso Internacional en Aplicaciones en Inteligencia Artificial durante el 2 y 3 de Noviembre. Este evento de talla internacional contará con expertos en Inteligencia Artificial de Brasil, México, Dinamarca, Argentina y Colombia",
#    "photo": "link to Google/Drive/Path/Image",
#    "initDate": datetime.today(),
#    "rate":  64.0 ,
#    "location": building_id["Edificio Ciencia y Tecnología (CyT)"]
# }, {
#    "name": "Feria Educativa China en la U.N",
#    "description": "La embajada de China y la universidad nacional de Colombia invitan.",
#    "photo": "link to Google/Drive/Path/Image",
#    "initDate": datetime.today(),
#    "rate":  74.0 ,
#    "location": building_id["Edificio Posgrados de Ciencias Humanas"]
# }, {
#    "name": "XIII JORNADA COMFIE.",
#    "description": "Revise y estudie los proyectos de estudiantes de todas las carreras de primeros semestres",
#    "photo": "link to Google/Drive/Path/Image",
#    "initDate": datetime.today(),
#    "rate":  79.0 ,
#    "location": building_id["Edificio Ciencia y Tecnología (CyT)"]
# }, {
#    "name": "El Futuro de la Salud en Colombia: Foro con Candidatos a la Cámara de Representantes",
#    "description": "Extendemos la siguiente invitación de la Asociación Colombiana Médica Estudiantil (ACOME) y la Asociación Nacional de Internos y Residentes (ANI)",
#    "photo": "link to Google/Drive/Path/Image",
#    "initDate": datetime.today(),
#    "rate":  95.0 ,
#    "location": building_id["Escuela de Medicina"]
# }, {
#    "name": "Conjuro de ríos",
#    "description": "Se presenta una prueba de artista en una configuración simplificada de la obra Río por asalto realizada por Clemencia Echeverri especialmente para la próxima Bienal de Shanghai, coincidiendo con las inquietudes planteadas en Selva Cosmopolítica, uno de los aportes a dicha Bienal desde la colaboración de María Belén Sáez de Ibarra.",
#    "photo": "link to Google/Drive/Path/Image",
#    "initDate": datetime.today(),
#    "rate":  89.0 ,
#    "location": building_id["Museo de Arte"]
# }, {
#    "name": "Gloria de Antonio Vivaldi con coro y orquesta",
#    "description": "Obra de arte conceptual, compuesta de palabras que deben ser transformadas en voces; miles de textos extraídos de prensa y diferentes libros, realizada con la intención de denunciar el imperialismo norteamericano –al que se compara con el nazismo–, y la responsabilidad de la religión en la justificación de los crímenes contra la humanidad",
#    "photo": "link to Google/Drive/Path/Image",
#    "initDate": datetime.today(),
#    "rate":  85.0 ,
#    "location": building_id["León de Greiff"]
# }, {
#    "name": "Divertimento No. 4 de Mozart con las Orquestas Batuta Bogotá",
#    "description": "El inicio de esta temporada de conciertos de la FNB contará con la participación de las principales agrupaciones sinfónicas de la Red en Bogotá, interpretando obras del repertorio sinfónico universal y Navidad Negra del compositor colombiano José Barros, entre otras. Como invitada especial, se presentará la agrupación de Ensamble de vientos y percusión del centro orquestal de la localidad de Puente Arand",
#    "photo": "link to Google/Drive/Path/Image",
#    "initDate": datetime.today(),
#    "rate":  93.0 ,
#    "location": building_id["León de Greiff"]
# }, {
#    "name": "Concierto Sinfónico Coral / Fundación Nacional Batuta",
#    "description": "La Fundación Nacional Batuta y el BNP Paribas presentan este concierto dentro del marco del reconocimiento Dream – up otorgado por el BNP Paribas a la Fundación Nacional Batuta, en el que más de 15.00 voces de niños, niñas, jóvenes y adolescentes de la ciudad de Bogotá y el municipio de Soacha se unen para interpretar un repertorio que incluye obras de música colombiana y del mundo, que van desde el unísono hasta el canto a varias voces, a capela y con acompañamiento instrumental bajo la dirección del maestro Ramón González.",
#    "photo": "link to Google/Drive/Path/Image",
#    "initDate": datetime.today(),
#    "rate":  78.0 ,
#    "location": building_id["León de Greiff"]
# }, {
#    "name": "El testigo",
#    "description": "Más de 50.00 fotografías organizadas en cuatro salas que representan distintas dinámicas del conflicto armado en Colombia",
#    "photo": "link to Google/Drive/Path/Image",
#    "initDate": datetime.today(),
#    "rate":  93.0 ,
#    "location": building_id["Museo de Arte"]
# }
# ])